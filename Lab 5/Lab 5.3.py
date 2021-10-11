# Student ID : 1201200318
# Student Name : Heng Yi Jun

def cm_to_meter(centimeter):
    meter = centimeter / 100
    return meter

def get_cm():
    cm = float(input("Please enter a value for centimeter : "))
    m = cm_to_meter(cm)
    print(" {:.2f} cm is {:.2f} meter ".format(cm,m))

def meter_to_cm(meter):
    centimeter = meter * 100
    return centimeter

def get_meter():
    cm = float(input("Please enter a value for meter : "))
    m = meter_to_cm(cm)
    print(" {:.2f} meter is {:.2f} centimeter ".format(cm,m))

print("======================================")
print("                MENU")
print("======================================")
print("  1.    Convert centimeter to meter")
print("  2.    Convert meter to centimeter")
print("======================================")
choice=int(input("Enter your choice : "))

if(choice==1):
    get_cm()
elif(choice==2):
    get_meter()
else:
    print("Invalid choice")