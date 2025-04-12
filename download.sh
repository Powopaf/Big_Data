#!/usr/bin/env bash

for year in 2009 2010 2011
do
    for month in {01..12}
    do
        if [ -f ./data/${year}/yellow_tripdata_${year}-${month}.parquet ]; then
            echo "File yellow_tripdata_${year}-${month}.parquet Exist"
            continue
        else
            url="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_${year}-${month}.parquet"
            echo "Downloading $url ..."
            wget -c "$url"
            echo "Finish Downloading $url"
            mv "yellow_tripdata_${year}-${month}.parquet" data/${year}/
        fi
    done
done
