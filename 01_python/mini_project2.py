students={
    "name":"Vidhi Bhanushali",
    "age":21,
    "city":"Bhuj",
    "CGPA":7.0,
    "Skills":["Python", "Java", "C++", "HTML", "CSS", "JavaScript"]
}


def get_grade(CGPA):
    if CGPA>=9.0:
        return("OUTSTANDING")
    elif CGPA>=8.0:
        return("EXCELLENT")
    elif CGPA>=7.0:
        return("GOOD")
    else:
        return("NEEDS IMPROVEMENT")


def check_eligibilty(age,cgpa):
    if age >= 18 and cgpa >= 6.0:
        return"Eligibile"
    else:
        return"wait"

def has_skill(skills,skill_name):
    return skill_name in skills

grade = get_grade(students["CGPA"])
eligibility = check_eligibilty(students["age"], students["CGPA"])

print("========================================")
print("STUDENT REPORT")
print("========================================")
print("Name:", students["name"])
print("Age:", students["age"])
print("City:", students["city"])
print("CGPA:", students["CGPA"])
print("Grade:", grade)
print("Eligibility:", eligibility)
print("Knows Python:", has_skill(students["Skills"], "Python"))
print("Knows SQL:", has_skill(students["Skills"], "SQL"))

print("Skills:")
for skill in students["Skills"]:
    print("-", skill)
print("========================================")