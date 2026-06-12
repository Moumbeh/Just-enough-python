"""
This script will implement our knowledge on conditions and data types
"""
print("This IT Organisation has various skill sets")
print("Find out your match")

print("Enter capitalised values: ")

DevOps = ["Jenkins", "Ansible", "Bash", "Python", "Terraform", "Docker", "Kubernetes"]
Development = ("Nodejs", "Angularjs", "Java", ".Net", "Python")
cntr_emp1 = {"Name":"Valery", "Skill":"Blockchain", "code":1024}
cntr_emp2 = {"Name":"Yakub", "Skill":"AI", "code":1030}

usr_skill = input("Enter your desired skill: ")
#print(usr_skill)

# check in the database if we have this skill
if usr_skill in DevOps:
    print(f"We have {usr_skill} in DevOps team.")
elif (usr_skill in Development):
    print(f"We have {usr_skill} in Development Team")
elif (usr_skill in cntr_emp1.values()) or (usr_skill in cntr_emp2.values()):
    print(f"We have contract employees with {usr_skill} skill")
else:
    print("Skill not found")
    print("Please check if you have entered values in capitalised or check spelling")

