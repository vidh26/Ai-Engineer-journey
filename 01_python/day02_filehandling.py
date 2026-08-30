# file=open("student.txt","w")

# file.write(
#     '''
# Name:Vidhi
# Age:21
# Goal:Ai enginner
# '''
# )
# file=open("student.txt","r")
# content=file.read()

# print (content)

# file=open("student.txt","a")
# file.write(
#     '''
# Learning:Python
# wants:Ai Enginner'''

# )
with open("student.txt","r") as file:
    content=file.read()
    print (content)