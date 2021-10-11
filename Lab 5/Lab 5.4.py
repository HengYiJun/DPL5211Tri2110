# Student ID : 1201200318
# Student Name : Heng Yi Jun

def rectangle(width,length):
    rec = width * length
    return rec

def triangle(width,length):
    tri = (width * length)/2
    return tri
i=1
while(i<=2):
    width = float(input("\nEnter width  : "))
    length = float(input("Enter length : "))
    r = rectangle(width,length)
    t = triangle(width,length)
    print("Rectangle area : {:.2f}".format(r))
    print("Triangle area  : {:.2f}".format(t))
    i=i+1