# string built-in function
message = "corona vaccine is ready to use, most of them are more than 90% effective."
print(message)
print(message.capitalize())
print(message) # messages are immutable so you have to store the capitalise version as a var
Message = message.capitalize()
print(Message)

# Look for possible functions
print(dir(""))
print(dir([]))
print(dir({}))
print(dir(()))

print(message.upper())
print(message.islower())
print(message.isupper())

print(message.find("ready")) # use the index add number of character of the word to get and return the word
print(message[18:24]) # in this case 18 the index plus five the word and one extra because you need the letter y in the word
print(message.find("not")) # you get -1 because the word does not exist in the string

seq1= ("192","168","40","90") # practice join
print(".".join(seq1))
print("/".join(seq1))
print("-".join(seq1))

mountains = ["Everest", "Himalaya", "Sahyadri", "Alps", "K2", "Mt Hood"]
print(mountains)

mountains.append("oregon mount")
print(mountains)

mountains.extend(["mt Rainer", "Satpuda"])
print(mountains)

mountains.insert(2, "Mt Abu")
print(mountains)

mountains.pop() # deletes the last word
print(mountains)
mountains.pop()
mountains.pop()
print(mountains)

cntr_emp1 = {"Name":"Santa", "Skill":"Blockchain", "Code":1024}
print(cntr_emp1.keys())
print(cntr_emp1.values())
print(cntr_emp1.clear())