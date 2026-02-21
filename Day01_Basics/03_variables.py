# variable nomenclature : no number at start, 
#                         no special character except (_),
#                         case sensitive.
                        
name = "Palak"
age = 21
eligible = False
print(name)
# name and age are variables here,"Palak" and 21 are the values assigned to variables using assignment operator.
# = -> assignment operator, stores value inside variables.
print(name, age, eligible)
print(type(name))
print(type(age))
print(type(eligible))
print("age is : "+ str(age)) 

movie = "Harry Potter"
year = 2010

print(f"My favourite movie is {movie}.\nIt was released in {year}.")
# here, f" is formatted string