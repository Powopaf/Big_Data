from pyspark.sql import SparkSession
from graph.map import draw
import sys

def parse_years(years):
    l = []
    if "-" not in years:
        l.append((years, spark.read.parquet(f"data/{year}/*")))
    else:
        s = years.split("-")
        for y in s:
            l.append((y, spark.read.parquet(f"data/{y}/*")))
    return l


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage is taxi arg1 arg2")
        sys.exit(1)
    if argv[1] == "trip":
        draw_trip(parse_years(argv[2])
    
