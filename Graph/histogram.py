import matplotlib.pyplot as plt

def histo(data: list[int], output_name="hitorigram.png"):
    plt.figure(figsize=(8, 6))
    plt.hist(data, len(data), color="blue", edgecolor="black", align="mid")
    plt.xlabel("Passenger Count")
    plt.ylabel("Number of trip")
    plt.title("Passenger Count Distribution")
    plt.xticks(range(min(data, ), max(data) + 1))
    plt.savefig(output_name)
    plt.close()
    print(f"Success creating historigram {output_name}")
    

if __name__ == '__main__':
    d = [1, 2, 1, 3, 1, 4, 2, 1, 2, 1, 1, 1, 3, 2]
    histo(d)
