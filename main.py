from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import array, col
import graph.map.draw as draw_mod
import graph.bar_char as bar
import sys

CONF = SparkConf() \
        .setAppName("NYCtaxiData") \
        .setMaster("local[*]") \
        .set("spark.driver.memory", "10g")

SC = SparkContext(conf=CONF)
SPARK = SparkSession(SC)
                                                                

def parse_years(years):
    l = []
    if "-" not in years:
        l.append((years, SPARK.read.parquet(f"data/{years}/*")))
    else:
        actives = years.split("-")
        for y in s:
            l.append((y, SPARK.read.parquet(f"data/{y}/*")))
    return l

def query_trip(all_df):
    for year, df in all_df:
        if year == "2009":
            df_trips = df.select(
                array(
                    array(col("Start_Lon"), col("Start_Lat")),
                    array(col("End_Lon"), col("End_Lat"))
                ).alias("trip")).limit(2500)
         
            trips_list = df_trips.collect()           
            trips_list = [row.trip for row in df_trips.collect()] 
            m = draw_mod.draw_trips_map(trips_list)
        else:
            print("Not finish")

def query_fare_vendor(all_df):
    for year, df in all_df:
        if year == "2009":
            df_fare = df.select("vendor_name",
            "Total_Amt").groupBy("vendor_name").agg(F.sum("Total_Amt").alias("total_fare")).limit(10000)
            rows = df_fare.collect()
            vendors, fares = zip(*[(row.vendor_name, row.total_fare) for row in
                                   rows])            
            bar.fare_vendor(list(vendors), list(fares), "fare_vendor_2009.png")
        elif year == "2010":
            df.printSchema()
            df_fare = df.select("vendor_id",
                                "total_amount").groupby("vendor_id").agg(F.sum("total_amount").alias("total_fare")).limit(10000)
            rows = df_fare.collect()
            vendors, fares = zip(*[(row.vendor_id, row.total_fare) for row in
                                   rows])
            bar.fare_vendor(list(vendors), list(fares), "fare_vendor_2010.png")
        elif year == "2011":
            df_fare = df.select("VendorID",
                                "total_amount").groupby("VendorID").agg(F.sum("total_amount").alias("total_fare")).limit(10000)
            rows = df_fare.collect()
            vendors, fare = zip(*[(row.VendorID, row.total_fare) for row in
                                  rows])
            bar.fare_vendor(list(vendors), list(fare), "fare_vendor_2011.png")
        else:
            print("error")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage is taxi arg1 arg2")
        sys.exit(1)
    if sys.argv[1] == "trip":
        query_trip(parse_years(sys.argv[2]))
    elif sys.argv[1] == "fare":
        query_fare_vendor(parse_years(sys.argv[2]))
    else:
        print("error")
