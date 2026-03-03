# match checks cases from top to bottom and stops at the first matching value.
# match-case is a cleaner alternative to if-elif for matching fixed values.

x= int(input("Enter value of x : "))
# x is a variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
        # case with if condition
    case 4:
        print("case is 4")
    case _ if x!=50:
        print("x is not 50")
    case _ if x!=100:
        print("x is not 100")
        # default case -> else 
    case _:
        print("x is", x)    

#Traffic signal

signal_clr = "green"
match signal_clr:
    case "red" :
        print("STOP")
    case "yellow" :
        print("WAIT")
    case "green" :
        print("GO!")
    case _:
        print("Invalid Signal")    


#matching multiple values
day = input("Enter the day : ")

match day:
    case "Saturday" | "Sunday" :
        print("Weekend")
    case _:
        print("Weekday")    

# boolean example
y =  True         #1==True

match y:
    case 0:
        print("False")
    case 1:
        print("One")
    case True:
        print("True")
    case _:
        print("Other")