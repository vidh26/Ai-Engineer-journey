import pandas as pd 

data={
    'Name':['Alice','Bob','Charlie','David','Eva'],
    'Age':[24,27,22,32,29],
    'Department':['HR','IT','Finance','Marketing','Sales'],
    "Salary":[50000,60000,55000,"np.nan",65000]
}

print(data)
df=pd.DataFrame(data)
print(df)

# print(df.head(2))
# print(df.tail(2))

# print(df.iloc[1:3])
# print(df.loc[1:3,["Age","Department"]])

print(df["Age"])
print(df.drop("Age",axis=1,inplace=True))
print(df)
print(df.shape)
print(df.info())
print(df.describe())