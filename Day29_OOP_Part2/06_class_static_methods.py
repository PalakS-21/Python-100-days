# @classmethod -> works with the class itself, rather than a particular object.
# it uses cls instead of self.

class Student:
    school = "ABC School"

    @classmethod
    def change_school(cls, new_school): # cls refers to class.
        cls.school = new_school

print(Student.school)

Student.change_school("XYZ School")

print(Student.school)