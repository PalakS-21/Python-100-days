
employee = {
    "emp_name" : "Steve",
    "emp_id" : 212,
    "emp_contact" : +916754839864,
    "emp_dept" : "HR" 
}
print(employee)

# update() -> adds new value
employee.update({
    "emp_salary" : 65000
})

# updated
print("\n", employee)

# also 
employee2 = {
    "emp2_D.O.B" : "22 August 1996"
}

# dict_name.update(dict1_name) -> updates one dictionary with another dictionary value which is not present in first dictionary.

employee.update(employee2)
print("\n", employee) # updates employee2 key value to employee
print("\n", employee2)

print("\n")

# pop() ->  removes specific key

employee.pop("emp_dept")
print(employee)

print("\n")

# popitem() -> removes last inserted item

employee.popitem()
print(employee)

print("\n")

# copy -> makes separate copy

employee3 = employee.copy()
print("employee3 (copy) = ",employee3)


# setdefault(key, value) -> adds if not exist
employee.setdefault("emp_address", "Delhi")
print("\n", employee)


# clear -> empty dictionary
employee.clear()
print("\n", employee) # {}


