# Different print format
name = "John"
profession = "DevOps Engineer"

print("The name of the employee is ", name)
print("The name of the employee is {}".format(name))
print("{} is his job title.".format(profession))
print("The name of the new employee is {} and his job title is {}".format(name, profession))
print(f"The name of the new employee is {name} and his job title is {profession}") # python 3.6 or higher

 # Concatination
print("The name of the new employee is" + " " + name)
