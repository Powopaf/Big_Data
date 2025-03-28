import matplotlib.pyplot as plt

def fare_vendor(vendors, sales, name="fare_vendor.png"):
    plt.bar(vendors, sales)
    plt.title("Total fare by vendors")
    plt.xlabel("Vendors")
    plt.ylabel("Sales")
    plt.savefig(name)

def trip_time(time, nb_trip, name="trip_time.png"):
    """
    time is a list of timestamp
    nb trip is a list of the number of trip
    nb_trip[0] tell the number of trip made at time[0]
    parse time -> YYYY-MM-DD hh-mm-ss
    """
    plt.bar(time, nb_trip)
    plt.title("Number of trip by hour")
    plt.xlabel("Time")
    plt.ylabel("Number of trip")
    plt.savefig(name)

def 

if __name__ == '__main__':
    fare_vendor(["VTS", "DDS", "CMT"], [10, 5, 2.5])
