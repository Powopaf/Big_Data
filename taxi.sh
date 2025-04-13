#!/bin/bash


Help () {
    echo "taxi trip YYYY-YYYY"
    echo "taxi fare YYYY-YYYY"
    echo "taxi heat YYYY-YYYY"
    echo "taxi hist YYYY-YYYY"
    echo "taxi pay YYYY-YYYY"
}

CheckDate () {
    l=${#1}
    if ! [ $l -eq 4 -o $l -eq 9 ]; then
        Help
        exit 1
    fi
    if [ $l -eq 9 ]; then
        if ! [[ "$1" =~ ^(2009|2010|2011)-(2009|2010|2011)$ ]]; then
            Help
            exit 1
        fi
    fi
}

if [ "$#" -lt 2 -o "$#" -gt 2 ]; then
    Help
    exit 1
fi

if [ "$1" = "trip" ]; then
    CheckDate "$2"
    python3 -m main $1 $2

elif [ "$1" = "fare" ]; then
    CheckDate "$2"
    python3 -m main "$1" "$2"

elif [ "$1" = "heat" ]; then
    CheckDate "$2"
    python3 -m main "$1" "$2"

elif [ "$1" = "hist" ]; then
    CheckDate "$2"
    python3 -m main "$1" "$2"

elif [ "$1" = "pay" ]; then
    CheckDate "$2"
    python3 -m main "$1" "$2"
else
    HELP
    exit 1
fi
exit 0
