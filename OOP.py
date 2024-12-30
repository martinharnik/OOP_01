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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # Additional way of constructing an instance
    @classmethod
    def from_string(cls, employee_string):
        first, last, pay = employee_string.split("-")
        return cls(first, last, pay)
    
    # This is a static method
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

new_emp = Employee.from_string("Mark-Brown-18000")
print(new_emp.fullname())

emp = Employee("John", "Green", 15000)

Employee.set_raise_amount(1.06)

print(Employee.raise_amount)
print(emp.raise_amount)

# How static method works
import datetime
my_date = datetime.date(2024, 8, 23)
print(Employee.is_workday(my_date))