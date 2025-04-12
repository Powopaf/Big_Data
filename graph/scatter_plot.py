import matplotlib.pyplot as plt

def scatter_time_dist(time, dist, output_file="scatter_time_dist.png"):
    plt.figure(figsize=(8,6))
    plt.title("Trip Duration vs Trip Distance")
    plt.scatter(time, dist)
    plt.xlabel("Duration")
    plt.ylabel("Distance")
    plt.savefig(output_file)
    plt.close()
    print(f"Success creating scatter_time_dist {output_file}")
    

if __name__ == '__main__':
    x = [1, 2, 3, 4, 5]
    y = [5, 4, 3, 2, 1]
    scatter_time_dist(x, y)
