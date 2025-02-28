import pandas as pd



if __name__ == '__main__':
    print("Hello big data")
    df_parquet = pd.read_parquet('/DataBase/*.parquet')
    print(df_parquet[0][0])