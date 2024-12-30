class Employee:
    
    number_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.number_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        #self.pay = int(self.pay * Employee.raise_amount) this works too, but raise amount wont be changed for individual instances (say 1.08 for emp1 and 1.11 for emp2) 

print(f"Now the total number of employees is {Employee.number_of_employees}.")

emp = Employee("John", "Green", 15000)

print(Employee.raise_amount)
print(emp.raise_amount)

Employee.raise_amount = 1.08

print(Employee.raise_amount)
print(emp.raise_amount)

emp.raise_amount = 1.11

print(Employee.raise_amount)
print(emp.raise_amount)

print(emp.pay)
emp.apply_raise()
print(emp.pay)

print(f"But now after welcoming {emp.fullname()} to the company the total number of employees is {Employee.number_of_employees}.")