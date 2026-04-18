products=["Phone", "Laptop", "Earphones", "Tablet"]
prices=[20000, 50000, 2000, 30000]
quantity=[1, 2, 3, 1]

total_revenue=0

for i in range(len(products)):
    revenue=prices[i]*quantity[i]
    print(products[i],"Revenue:",revenue)
    total_revenue += revenue
print("Total Revenue:", total_revenue)
