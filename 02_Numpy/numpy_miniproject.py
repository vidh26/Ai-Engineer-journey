import numpy as np

students=np.array([78,90,60,45,90,71,95,89])
print(students)

print("total student",students.size)
print("average",students.mean())
print("max",students.max())
print("min",students.min())
print("student above 80",students[students>80])
print("student less 40",students[students<40])
print(np.sort(students))
