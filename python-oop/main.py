'''class Student:
    pass

student1 = Student()
student1.name = "Harry"
student1.marks = 85

print(student1.name)
print(student1.marks)'''


class Student:
    def checkPassFail(self):
        if self.marks >= 40:
            return True

        else:
            return False


student1 = Student()
student1.name = "Harry"
student1.marks = 85

didPass = student1.checkPassFail()

print(didPass)