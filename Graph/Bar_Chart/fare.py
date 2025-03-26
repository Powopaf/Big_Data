import matplotlib.pyplot as plt

def fare_vendor(vendors, sales, name="fare.png"):
    plt.bar(vendors, sales)
    plt.title("Total fare by vendors")
    plt.xlabel("Vendors")
    plt.ylabel("Sales")
    plt.savefig(name)

def trip_time(time, nb_trip):
    #TODO
    """
    time is a list of timestamp
    nb trip is a list of the number of trip
    nb_trip[0] tell the number of trip made at time[0]
    parse time -> YYYY-MM-DD hh-mm-ss
    """
    pass

if __name__ == '__main__':
    fare_vendor(["VTS", "DDS", "CMT"], [10, 5, 2.5])
