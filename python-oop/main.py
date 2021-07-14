'''class Student:
    pass

student1 = Student()
student1.name = "Harry"
student1.marks = 85

print(student1.name)
print(student1.marks)'''


'''class Student:
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
print(didPass)'''

class complex:
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
print('imag =', result.imag)