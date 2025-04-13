from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import array, col
import graph.map.draw as draw_mod
import graph.bar_char as bar
import graph.heatMap as hmap
import graph.histogram as hist
import graph.pieChart as pieC
import graph.scatter_plot as scatter
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
        s = years.split("-")
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
                    
            trips_list = [row.trip for row in df_trips.collect()] 
            m = draw_mod.draw_trips_map(trips_list)
        else:
            print("Not finish")

def query_fare_vendor(all_df):
    for year, df in all_df:
        if year == "2009":
            df_fare = df.select("vendor_name",
            "Total_Amt").groupBy("vendor_name").agg(F.sum("Total_Amt").alias("total_fare"))
            rows = df_fare.collect()
            vendors, fares = zip(*[(row.vendor_name, row.total_fare) for row in rows])
            bar.fare_vendor(list(vendors), list(fares), "fare_vendor_2009.png")
        elif year == "2010":
            df.printSchema()
            df_fare = df.select("vendor_id", "total_amount").groupby("vendor_id").agg(F.sum("total_amount").alias("total_fare"))
            rows = df_fare.collect()
            vendors, fares = zip(*[(row.vendor_id, row.total_fare) for row in rows])
            bar.fare_vendor(list(vendors), list(fares), "fare_vendor_2010.png")
        elif year == "2011":
            df_fare = df.select("VendorID", "total_amount").groupby("VendorID").agg(F.sum("total_amount").alias("total_fare"))
            rows = df_fare.collect()
            vendors, fare = zip(*[(row.VendorID, row.total_fare) for row in rows])
            bar.fare_vendor(list(vendors), list(fare), "fare_vendor_2011.png")
        else:
            print("error")

def query_heat(all_df):
    for year, df in all_df:
        if year == "2009":
            df_heat = df.select("Start_Lon", "Start_Lat").limit(5000)
            rows = df_heat.collect()
            heat = [[row.Start_Lat, row.Start_Lon] for row in rows]
            hmap.draw_heat(heat)
        else:
            print("Not finihs")

def query_histo(all_df):
    for year, df in all_df:
        if year == "2009":
            df_hist = df.select("Passenger_Count").limit(10000)
            rows = df_hist.collect()
            nb_passengers = [row.Passenger_Count for row in rows]
            hist.histo(nb_passengers, "nb_passengers2009.png")
        elif year == "2010":
            df_hist = df.select("passenger_count").limit(10000)
            rows = df_hist.collect()
            nb_passengers = [row.passenger_count for row in rows]
            hist.histo(nb_passengers, "nb_passengers2010.png")
        elif year == "2011":
            df_hist = df.select("passenger_count").limit(10000)
            rows = df_hist.collect()
            nb_passengers = [row.passenger_count for row in rows]
            hist.histo(nb_passengers, "nb_passengers2011.png")
        else:
            print("error")

def query_pie(all_df):
    for year, df in all_df:
        if year == "2009":
            df_pie = df.select("Payment_Type").limit(1000000)
            rows = df_pie.collect()
            use = [row.Payment_Type for row in rows]
            pieC.pie_payment(use, "Payment_Type2009.png")
        elif year == "2010":
            df_pie = df.select("payment_type").limit(1000000)
            rows = df_pie.collect()
            use = [row.payment_type for row in rows]
            pieC.pie_payment(use, "Payment_Type2010.png")
        else:
            print("TODO")

def query_scatter(all_df):
    pass

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage is taxi arg1 arg2")
        sys.exit(1)
    if sys.argv[1] == "trip":
        query_trip(parse_years(sys.argv[2]))
    elif sys.argv[1] == "fare":
        query_fare_vendor(parse_years(sys.argv[2]))
    elif sys.argv[1] == "heat":
        query_heat(parse_years(sys.argv[2]))
    elif sys.argv[1] == "hist":
        query_histo(parse_years(sys.argv[2]))
    elif sys.argv[1] == "pay":
        query_pie(parse_years(sys.argv[2]))
    else:
        print("error")
