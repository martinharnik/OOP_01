class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    
emp = Employee("John", "Green", 15000)

print(emp.email)

# Both do the same thing
print(emp.fullname())
print(Employee.fullname(emp))