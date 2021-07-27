"""class Student:
    pass

student1 = Student()
student1.name = "Harry"
student1.marks = 85

print(student1.name)
print(student1.marks)"""


"""class Student:
    def checkPassFail(self):
        if self.marks >= 40:
            return True

        else:
            return False

    def __init__ (self, name, marks):
        self.name = name
        self.marks = marks

student1 = Student("Harry", 85)
student2 = Student("Janet", 30)
didPass = student1.checkPassFail()
print(didPass)
didPass = student2.checkPassFail()
print(didPass)"""


"""class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, number):
        real = self.real + number.real
        imag = self.imag + number.imag
        result = complex(real, imag)
        return result


n1 = complex(5, 6)
n2 = complex(-4, 2)
result = n1.add(n2)
print("real =", result.real)
print("imag =", result.imag)"""


class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee("Thiago", "Ximenes", 50000)
emp_2 = Employee("Test", "User", 60000)

# print(emp_1)
# print(emp_2)

# print(emp_1.email)
# print(emp_2.email)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(emp_1.fullname())
# print(emp_2.fullname())

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print(emp_1.__dict__)

# Employee.raise_amount = 1.08

# emp_1.raise_amount = 1.08

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

print(Employee.num_of_emps)