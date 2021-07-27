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

    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    def __add__(self, other):
        return self.pay + other.pay


emp_1 = Employee("Thiago", "Ximenes", 50000)
emp_2 = Employee("Test", "User", 60000)

print(emp_1 + emp_2)

# print(repr(emp_1))
# print(str(emp_1))
