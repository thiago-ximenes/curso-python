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


class Developer(Employee):
    raise_amount = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employee=None):
        super().__init__(first, last, pay)
        if employee is None:
            self.employee = []
        else:
            self.employee = employee

    def add_employee(self, emp):
        if emp not in self.employee:
            self.employee.append(emp)

    def remove_employee(self, emp):
        if emp in self.employee:
            self.employee.remove(emp) 

    def print_emps(self):
        for emp in self.employee:
            print('-->', emp.fullname())


dev_1 = Developer("Thiago", "Ximenes", 50000, "Python")
dev_2 = Developer("Test", "User", 60000, "JavaScript")

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_employee(dev_2)
mgr_1.remove_employee(dev_1)

# print(dev_1.email)
# print(dev_2.email)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(dev_1.email)
# print(dev_1.prog_lang)

mgr_1.print_emps()