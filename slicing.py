from xml.dom.minidom import ProcessingInstruction

planet1 = "closest to the sun"
print(planet1)

# slice planet variable using the index number of the string
print(planet1[0])
print(planet1[1])
print(planet1[2])
print(planet1[3])

# Reverse slicing
print(planet1[-1])
print(planet1[-2])
print(planet1[-3])

# substring slicing
print(planet1[1:4])
print(planet1[1:4])
print(planet1[15:])

# slicing a tuple
devops = ("linux", "bash", "powershell", "azure", "github actions", "python")
print(devops[0])
print(devops[2])
print(devops[-1])
print(devops[2:5])
print(devops[2:5][0])
print(devops[2:5][0][:5])
print(devops[2:5][0][:5][-1])

# slicing a list
devops = ["linux", "bash", "powershell", "azure", "github actions", "python"]
print(devops[0])
print(devops[2])
print(devops[-1])
print(devops[2:5])
print(devops[2:5][0])
print(devops[2:5][0][:5])
print(devops[2:5][0][:5][-1])

# slicing dictionary
skills = {"DevOps":("azure", "powershell", "terraform", "git"), "Development": ["python", "java", "NodeJS", ".NET","php"]}
print(skills)
print(skills["DevOps"])
print(skills["Development"])
print(skills["DevOps"][-1])
print(skills["DevOps"][1:4])
