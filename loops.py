# For loop
Planet = "Earth"
for i in Planet:
    print("Value of i is now ", i)
print("Rest of the code")

vaccines = ("Moderna","Pfizer", "Sputnik v", "Covaxin", "AstraZeneca")
for vac in vaccines:
    print(f"{vac} vaccine provides immunisation against covid19", "####")

vaccines = ["Moderna","Pfizer", "Sputnik v", "Covaxin", "AstraZeneca"]
for vac in vaccines:
    print(f"{vac} vaccine provides immunisation against covid19")

# while loop
x = 0
while x <= 10:
    print("Value of X is:", x)
    print("looping")
    x+=1
print("Rest of the Code")