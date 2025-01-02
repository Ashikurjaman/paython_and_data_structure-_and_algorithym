class Employee:
    __count = 0
    def __init__(self):
        Employee.__count = Employee.__count +1
    def display(self):
        print(Employee.__count)    

emp = Employee()
emp1 = Employee()

try:
    print(emp.__count)
finally:
    print(emp.display())    
