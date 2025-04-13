import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def fare_vendor(vendors, sales, name="fare_vendor.png", scale_factor=1e6, scale_label=" (in millions)"):
    scaled_sales = [sale / scale_factor for sale in sales]
    plt.figure(figsize=(6, 3))
    bars = plt.bar(vendors, scaled_sales, color='skyblue', edgecolor='black')
    plt.title("Total Fare by Vendors", fontsize=16, fontweight='bold')
    plt.xlabel("Vendors", fontsize=14)
    plt.ylabel("Total Sales" + scale_label, fontsize=14)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.yticks(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    ax = plt.gca()
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x:.2f}'))
    for bar in bars:
        yval = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2, 
            yval, 
            f'{yval:.2f}', 
            va='bottom', 
            ha='center', 
            fontsize=10
        )
    plt.tight_layout()
    plt.savefig(name, dpi=300)
    plt.close()


"""
def fare_vendor(vendors, sales, name="fare_vendor.png"):
    plt.bar(vendors, sales)
    plt.title("Total fare by vendors")
    plt.xlabel("Vendors")
    plt.ylabel("Sales")
    plt.savefig(name)
"""
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

"""
if __name__ == '__main__':
    fare_vendor(["VTS", "DDS", "CMT"], [10, 5, 2.5])
"""
