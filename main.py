import polars as pl


if __name__ == '__main__':
    # t = pl.read_parquet("DataBase/yellow_tripdata_2009-01.parquet")
    # print(t.filter(pl.col("Passenger_Count") == 1 and pl.col("vendor_name") == "VTS").collect())
    df = (pl.scan_parquet("DataBase/yellow_tripdata_2009-01.parquet"))
    print(df)
    df_vts_1_passenger = df.filter((pl.col("Passenger_Count") == 1) & (pl.col("vendor_name") == "VTS"))
    print(df.filter((pl.col("Passenger_Count") == 1) & (pl.col("vendor_name") == "VTS")).collect())