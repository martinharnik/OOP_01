class Employee:
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
    #    self.email = first + "." + last + "@company.com"

    @property # This changes a method into an attribute. It does the same thing as the above email property.
    def email(self):
        return f"{self.first}.{self.last}@company.com"

    @property # This changes a method into an attribute
    def fullname(self):
        return f'{self.first} {self.last}'       
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Employee deleted!")
        self.first = None
        self.last = None

emp = Employee("John", "Green")

print(emp.first)
print(emp.email)
print(emp.fullname)

emp.fullname = ("Tim Brown")

print(emp.first)
print(emp.email)
print(emp.fullname)

del emp.fullname
