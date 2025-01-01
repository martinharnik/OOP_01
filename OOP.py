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
        return f'{self.first} {self.last}'
    
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

class Developer(Employee):

    raise_amount = 1.15

    def __init__(self, first, last, pay, programming_language):
        super().__init__(first, last, pay)
        #Employee.__init__(self, first, last, pay) This will also work fine.
        self.programming_language = programming_language

class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def show_employees(self):
        for emp in self.employees:
            print(emp.fullname())         

emp = Employee("John", "Green", 15000)
dev = Developer("Jeff", "Scott", 20000, "Python")
mgr = Manager("Dirk", "Gibbson", 50000)

# Show the full name of the manager
print(mgr.fullname())

# Add employees to the manager
mgr.add_employee(dev)
mgr.add_employee(emp)

# Show the names of employees who report to the manager
mgr.show_employees()

# isinstance function
print(isinstance(mgr, Manager))
print(isinstance(mgr, Employee))
print(isinstance(dev, Manager))

# issubclass function
print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Developer, Manager))


