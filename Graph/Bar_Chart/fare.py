import matplotlib.pyplot as plt

def fare_vendor(vendors, sales, name="fare.png"):
    plt.bar(vendors, sales)
    plt.title("Total fare by vendors")
    plt.xlabel("Vendors")
    plt.ylabel("Sales")
    plt.savefig(name)

if __name__ == '__main__':
    fare_vendor(["VTS", "DDS", "CMT"], [10, 5, 2.5])
