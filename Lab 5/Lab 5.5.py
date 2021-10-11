# Student ID : 1201200318
# Student Name : Heng Yi Jun

def get_bonus(unit,salary):
    if(unit>1000):
        bonus=salary * 0.2
    elif(unit>=501 and unit<=1000):
        bonus=salary * 0.1
    else:
        bonus=0
    return bonus

def get_nett_salary(salary,bonus):
    nett = salary + bonus
    return nett

def display(id,salary,unit,ba,nsalary):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("            SALARY SLIP")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Staff ID                :  {}".format(id))
    print("Staff salary            :  RM {:.2f}".format(salary))
    print("Units sold              :  {}".format(unit))
    print("Bonus                   :  RM {:.2f}".format(bonus))
    print("Nett Salary             :  RM {:.2f}".format(nett))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                DATA ENTRY")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
id = int(input("Enter staff id          : "))
salary = float(input("Enter staff salary      : RM "))
unit = int(input("Enter total units sold  : "))
bonus = get_bonus(unit,salary) 
nett = get_nett_salary(salary,bonus) 
display(id,salary,unit,bonus,nett)