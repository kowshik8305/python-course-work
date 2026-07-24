n = "Ravi"
p = 500
def calculate_bill(p):
    tax=p +0.18
    return p+tax
def print_bill(n, total):
    print("customer:",n)
    print ("total Bill:",total)
total=calculate_bill(p)
print_bill(n,total)

