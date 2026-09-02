import pandas as pd

s=pd.Series([1, 2, 3, 4, 5])
print(s)

print(s.dtype)
print(s.values)
print(s.index)
s.name="calories"
print(s.name)
print(s)
print(s[0:2])
print(s.iloc[3])
index=["apple", "banana", "cherry", "date", "elderberry"]
s.index=index
print(s) 


fruit_protien={
    "avacado": 2.0,
    "guava":2.6,
    "orange":1.2,
    "blackberries":1.4
}

s2=pd.Series(fruit_protien)
print(s2)

print(s2[s2<1.5])
