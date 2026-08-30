student={
    "Name":"",
    "age":0,
    "cgpa":0,
    "python":0,
    "math":0,
    "communication":0,
    "problem_solving":0,
    "interest":"",
    "work_preference":""

}

student["Name"] =input("enter your name")
student["age"] =int(input("enter your age"))
student["cgpa"] =float(input("enter your cgpa"))
student["python"] =int(input("enter your python skill fron 1-10"))
student["math"] =int(input("enter your math skill fron 1-10"))
student["communication"] =int(input("enter your communication skill fron 1-10"))
student["problem_solving"] =int(input("enter your problem_solving skill fron 1-10"))
student["interest"]=input("Enter  your interest in any of one   AI , Web Development , Data Science ,Cybersecurity")
student["work_preference"]=input("Enter  your job in any of one  Coding, Data Analysis, Problem Solving, Security")


print(student)

def Career_analysis(Interest,python_skill,math_skill,problemsolving_skill):
    if Interest== "AI" :
        if python_skill>=6 :
            if math_skill>=7 :
                print("You can become AI Enginner")
                return "AI Enginner"
            else:
                print("improve your math skill")
        else:
            print("improve your python skill")
    

    elif Interest== "Data Science" :
        if python_skill>=6 :
            if math_skill>=7 :
                print("You can become a data scientist")
                return "Data Analytics"
            else:
                print("improve your math skill")
        else:
            print("improve your python skill")


    elif Interest== "Web devlopment" :
        if python_skill>=5:
            print("You can be Web devolper")
            return "Web development"
        else:
            print("improve your python skill")

    
    elif Interest== "Cybersecurity":
            if problemsolving_skill>=5:
                print("You can be Web devolper")
                return "Cybersecurity"
            else:
                print("improve your problem solving skill")

    else:
        print("improve your skills")


def Carrer_score (python_skill,math_skill,problemsolving_skill,communication):

   return {
       "Ai Score":python_skill+math_skill,
       "Data Analysis Score":python_skill+math_skill,
       "Web development":python_skill+problemsolving_skill+communication,
       "cybersecurity":communication
   }


Analaysis= Career_analysis(student["interest"],student["python"],student["math"],student["problem_solving"])
score= Carrer_score(student["python"],student["math"],student["problem_solving"],student["communication"])

print("========================================")
print("AI CARRER ANALYZER")
print("========================================")
print("Name:", student["Name"])
print("Age:", student["age"])
print("CGPA:", student["cgpa"])

print("Python Skill:", student["python"])
print("Math Skill:", student["math"])
print("Problem Solving:", student["problem_solving"])
print("Communication:", student["communication"])


print("Insterest:", student["interest"])
print("Work Preference:", student["work_preference"])

print("========================================")
print("CARRER ANALYES")
print("========================================")

print("your score are:",score)
print("your recommendeted carrer are ",Analaysis)

print("====================end==================")