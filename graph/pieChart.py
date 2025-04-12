import matplotlib.pyplot as plt

def pie_payment(pay: list[str], output_file="pie_payment.png"):
    l = ["Cash", "Credit"]
    c = 0
    for i in pay:
        if i.lower() == "cash":
            c += 1
    sizes = [c, len(pay) - c]
    plt.figure(figsize=(8, 6))
    plt.title("Proportion of payment method used")
    plt.pie(sizes, labels=l, autopct='%1.1f%%')
    plt.savefig(output_file)
    plt.close()
    print(f"Success creating pie chart {output_file}")



if __name__ == '__main__':
    a = [
    "Cash", "Credit", "CASH", "credit", "Credit", "cash", 
    "Cash Payment", "credit card", "CREDIT", "Cash transfer",
    "Credit line", "cash deposit", "cash", "CREDIT PAYMENT", 
    "credit transaction", "Cash withdrawal", "Credit refund", 
    "cashback", "credit balance", "CREDIT PURCHASE" ]
    pie_payment(a)

