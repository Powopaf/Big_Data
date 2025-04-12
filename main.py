from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import array, col
import graph.map.draw as draw_mod
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
            
            df_trips = df.select(array(array(col("Start_Lon"),
                                             col("Start_Lat")),
                                       array(col("End_Lon"),
                                             col("End_Lat"))).alias("trip")).repartition(100)
            buff_size = 50
            buff = []
            m = None
            for row in df_trips.toLocalIterator():
                buff.append(row.trip)
                if len(buff) == buff_size:
                    if m is None:
                        m = draw_mod.draw_trips_map(buff)
                        
                    else:
                        m = draw_mod.draw_trips_map(buff, m)
                    buff = []
            if buff:
                 m = draw_mod.draw_trips_map(buff, m)
        else:
            print("Not finish")

if __name__ == '__main__':
    print(dir(draw_mod))
    if len(sys.argv) != 3:
        print("Usage is taxi arg1 arg2")
        sys.exit(1)
    if sys.argv[1] == "trip":
        query_trip(parse_years(sys.argv[2]))
    
