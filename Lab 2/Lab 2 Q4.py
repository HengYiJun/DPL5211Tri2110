# Student ID: 1201200318
# Student Name: Heng Yi Jun

bprice = 1.50
gprice = 5.60

print("Invoice for Fruits Purchase")
print("---------------------------------")

banana = float(input("Enter the quantity (comb) of bananas bought : "))
grape = float(input("Enter the amount (kg) of grape bought : "))

btotal = banana * bprice
gtotal = grape *  gprice
total = btotal + gtotal

print("Item                Qty        Price      Total")
print("Banana (combs)      {}        RM{:.2f}    RM{:.2f}".format(banana,bprice,btotal))
print("Grape  (kg)         {}        RM{:.2f}    RM{:.2f}".format(grape,gprice,gtotal))

print("Total : RM{:.2f}".format(total))