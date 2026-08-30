name="Vidhi Bhanushali"
age=21
city="Bhuj"
CGPA=7.0
Skills=["Python", "Java", "C++", "HTML", "CSS", "JavaScript"]

print("==================Student Information==================")

print("----------Basic Information----------")
print("Name:",name)
print("Age:",age)
print("City:",city)
print("CGPA:",CGPA)
print("Skills:",Skills)

print("-----------------Data Types--------------------")
print("Name:",type(name))
print("Age:",type(age))
print("City:",type(city))
print("CGPA:",type(CGPA))
print("Skills:",type(Skills))

print("-------------------if-else CGPA--------------------")
if CGPA>=9.0:
    print("OUTSTANDING")
elif CGPA>=8.0:
    print("EXCELLENT")
elif CGPA>=7.0:
    print("GOOD")
else:
    print("NEEDS IMPROVEMENT")

print("-----------------SKIILL CHECKING-----------------")
print("Know Python","Python" in Skills)
print("know SQL","SQL" in Skills)
print("Know React","React" in Skills)
print("know Java","Java" in Skills)

print("-------------------if-else INTERNSHIP ELIGIBILITY --------------------")
if age>=18 and CGPA>=6.0:
    print("ELIGIBLE")
else:
    print("NOT ELIGIBLE")

print("-------------------My SKILLS --------------------") 

for skill in Skills:
    print("my Skills:",skill)

print("----------------Number--------------------------")
for i in range (1,11):
    print (i)

print("----------------CGPA-------------------------")
count=(float(input("Enter your CGPA")))
while count<=0 or count>=10:
    print("INVAILD CGPA")
    count=(float(input("Enter your CGPA")))
print("Your CGPA IS",count)

