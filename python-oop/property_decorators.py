class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp_1 = Employee("Thiago", "Ximenes")
# emp_1.last = "Lima"
emp_1.fullname = "Thiago Lima"


print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

print(emp_1.first)
