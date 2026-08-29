# # personal information

# name = "Bhanushali Vidhi"
# age = 21
# city ="Bhuj"

# # education

# degree ="B.C.A"
# college="S.M.I.T"
# CGPA=7.0

# #Technical skills
# skills= ["Python", "Java", "C++", "HTML", "CSS", "JavaScript"]
# ai_skills = ["Machine Learning", "Deep Learning", "Natural Language Processing", "Computer Vision"]

# # career information

# python_knowledge="true"
# interested_in_ai="true"

# print ("-----------------------------Ai Enginner Candidate Information -----------------------------")

# print ("Personal Information:")
# print ("Name:", name)
# print ("Age:",age)
# print ("City:",city)


# print("Education:")

# print("Degree:",degree)
# print("College:",college)
# print("CGPA:",CGPA)

# print("technical Skills:")

# print("programming Languages:",skills)
# print("AI Skills:",ai_skills)

# print("Career Information:")

# print("Python Knowledge:",python_knowledge)
# print("Interested in AI:",interested_in_ai)

# print("-----------------------------Data Types------------------------------")

# print("Name:", type(name))
# print("Age:",type(age))
# print("CGPA:",type(CGPA))
# print("Python Knowledge:",type(python_knowledge))
# print("Programming Languages:",type(skills))

# print("------------------------------End------------------------------")

# print("--------mini problems ---------")

# print("percentage:", CGPA*9.5)
# print("even :", age%2==0)


# print(len(skills))

# print("Eligibility:", age>=18 and CGPA>=6.0)
# print(age**2)

# print("know python:", "Python" in skills)
# print("know Ruby:","Ruby" in skills)

# print("----------------if else ---------------")

# if age >=18:
#     print ("you are eligible to vote")
# else:
#     print ("you are still a minor")

# if CGPA>=9.0:
#     print ("Excellent")
# elif CGPA>=7.5:
#     print("Very Good")
# elif CGPA>=6.0:
#     print("good")
# else:
#     print("you need to work hard")

# if age>=18 and CGPA>=6.0:
#     print ("you are eligible for internship")
# else:
#     print("not eligible for internship")

# if len(skills)>=6:
#     print("you have good technical skills")
# elif len(skills)>=3:
#     print("you have average technical skills")
# else:
#     print("you need to improve your technical skills")


# print("-----------------loops--------------------")
# print(list(range(5)))
# print(list(range(1,10)))
# print(list(range(1,10,2)))


# for i in range(5):
#     print(i)


# skills= ["Python", "Java", "C++", "HTML", "CSS", "JavaScript"]

# for skill in skills:
#     print(skill)



# my_skills=["communication", "problem solving", "teamwork", "leadership", "adaptability"]


# for kill in my_skills:
#     print(kill)


# for i in range(1,101):
#     print(i)

# count = int(input("Enter a number:"))
# while count<=0:
#     print("try again ")
#     count = int(input("Enter a number:"))
# print("You entered:", count)
students={
    "name":"vidhi",
    "age":"21",
    "city":"bhuj",
    "cgpa":"7.0"
}

print(students["name"])
print(students["cgpa"])

students["cgpa"]=7.5
print(students["cgpa"])

for key, value in students.items():
    print(key,":",value) 


def greet(name):
    print ("hello",name)

greet("vidhi")
greet("jiya")

def add(a,b):
    print(a+b)

add(1,2)  


def eligibility(age,cgpa):
    if age >= 18 and cgpa >= 6.0:
        return"Eligibile"
    else:
        return"wait"

status=eligibility(21,9.0)
print(status)