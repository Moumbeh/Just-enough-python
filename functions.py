# defining functions
from random import choice


def add(arg1, arg2):
    total = arg1 + arg2
    return total
out = add(2, 3)
print(out)

print(add(4, 6))

###############################
def summ(arg):
    x = 0
    for i in arg:
        x = x + i
    return x

out = sum([10, 20, 30])
print(out)

print(summ([5, 10, 15]))
#################################
def greetings(MSG):
    print(f'Good {MSG}')
    print("Welcome to the function")

print(greetings("Afternoon"))

# Add default message which can be override and return
def greetings(MSG="Morning"):
    print(f'Good {MSG}')
    print("Welcome to the function")

print(greetings())
print(greetings("Night"))

###################
# Keywords argument
print("####################################################")
def vac_feedback(vac, efficacy):
    print(f"{vac} vaccine is having {efficacy} % efficacy")
    if (efficacy > 50) and (efficacy <= 75):
        print("Seems not so effective, Needs more trial")
    elif (efficacy > 75) and (efficacy < 90):
        print("can consider this vaccine")
    elif efficacy >= 90:
        print("Sure, will take the shot")
    else:
        print("Needs many more trials")

vac_feedback("Pfizer", 95)
vac_feedback("Unknown", 45)
vac_feedback(efficacy=65, vac="Moderna")

# Variable Length Arguments **kwargs (keyword Arguments)
print("########## Key Pair Argument ################")

import random
def time_activity(*args, **kwargs):
    """
    Input: Multiple values for minutes, key=value pair activity
    Output: Return sum of minutes + random minute spect on a random activity
    """
    min = sum(args) + random.randint(0, 60)
    print(min)
    choice = random.choice(list(kwargs.keys()))
    print(choice)
    print(f"You have to spend {min} Minutes for {kwargs[choice]}")

time_activity( hobby="Dance", sport="Boxing", fun="Driving", work="DevOps")
time_activity(10, 20, 10, hobby="Dance", sport="Boxing", fun="Driving", work="DevOps")