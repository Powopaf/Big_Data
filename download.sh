#!/usr/bin/env bash

for year in 2009 2010 2011
do
    for month in {01..12}
    do
        url="https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_${year}-${month}.parquet"

        echo "Downloading $url ..."
        ./wgetui.sh "$url"
        echo "Finish Downloaging $url  
    done
done
