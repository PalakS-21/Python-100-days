class Person:
    name = "Palak"
    occupation = "Software Engineer"

    def info(self):
        print(f"{self.name} is a {self.occupation}.")
        # self -> current object being createed

a = Person() # object
b = Person()

# a.name = "Ron"
# a.occupation = "HR"
print(a.name, a.occupation)

a.info()

a.name = "harry"
a.occupation = "Accountant"

b.name = "Ritika"
b.occupation = "Dancer"

a.info()
b.info()