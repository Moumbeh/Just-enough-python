# variable assignments
var1 = "python" # String (looks nice) But the all work
var2=75         # integer (ugly)
var3 =3.5       # flot    (ok but could be nice)

# print variables
print(var1)
print(var2)
print(var3)

# multiple assignments
a = b = c = 50 # they will have the same value

print(a)
print(b)
print(c)

# multiple assignments to multiple variables
w, x, y, z = "green", "red", 5, 12.5

# print variable with a string
print('Variable w value is ', w)
print('Variable x value is ', x)
print("variable y value is ", y)
print("Variable z value is ", z)

# check variables type
print(type(w))
print(type(x))
print(type(y))
print(type(z))

# check variable type with a string
print("Variable w is ", type(w))
print("Variable x is ", type(x))
print("Variable y is ", type(y))
print("Variable z is ", type(z))

# data types
# string
str1 = "red"
str2 = 'green'
str3 = ''' yellow '''
str4 = """ multiple string """

# numbers
num1 = 123
flt2 = 3.5

# list (array in other languages) collection of multi datatype, enclosed in square brackets
first_list = [str1, "DevOps", num1, 1.0] # space is not compulsory but it's nice

# print list
print(first_list)

# Tuple/ collection of multi datatype, enclosed in round bracket. tuple is immutable meaning you can edit a list but cant edit a tuple but you can override
first_tuple = (str1, "DevOps", num1, 1.0) # space is not compulsory but it's nice

# print tuple
print(first_tuple)

# dictionary/ Elements in a dictionary are always in pairs(key:value), curly brackets
first_dictionary = {"Name":"John", "Weight":80, "Exercise":["Boxing", "Dancing", "Jogging","Running"]}

# print dictionary
print(first_dictionary)

# lets print data types
print("Variable first_list is a:", type(first_list))
print("Variable first_tuple is a:", type(first_tuple))
print("Variable first_dictionary is a:", type(first_dictionary))

# Boolean
x = True
y = False

# print Boolean
print(x)
print(y)

print("x is a ", type(x))
print("y is a ", type(y))
