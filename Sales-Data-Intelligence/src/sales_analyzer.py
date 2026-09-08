import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("data/sales_data.csv")
# print(df.head())
# print(df.info())
# print(df.describe())

print("\n Missing Values:")
print(df.isnull().sum())

print("\n duplicates")
print(df.duplicated().sum())

print("\n Data Types ")
print(df.dtypes)

df["Date"]=pd.to_datetime(df["Date"])
print(df.dtypes)

df["Revenue"]=df["Quantity"]*df["Unit_Price"]
print(df.head())
print("\n Revenue Statistics")
print(df["Revenue"].describe())

total_revenue=df["Revenue"].sum()
total_order=df["Order_ID"].nunique()
total_quantity=df["Quantity"].sum()
total_average_order_value=total_revenue/total_order

print("\n Total Revenue: ", total_revenue)
print("\n Total Orders: ", total_order)
print("\n Total Quantity Sold: ", total_quantity)
print("\n Average Order Value: ", total_average_order_value)

product_sales=df.groupby("Product")[["Revenue"]].sum()
print("\n Product Sales:")
print(product_sales)

best_product=product_sales.idxmax()
best_product_revenue=product_sales.max()

print("\n Best Product: ", best_product)
print("\n Best Product Revenue: ", best_product_revenue)

region_sales=df.groupby("Region")["Revenue"].sum()
print("\n Region Sales:")
print(region_sales)

best_region=region_sales.idxmax()
best_region_revenue=region_sales.max()

print("\n Best Region: ", best_region)
print("\n Best Region Revenue: ", best_region_revenue)

category_sales=df.groupby("Category")["Revenue"].sum()
print("\n Category Sales:", category_sales)

best_category=category_sales.idxmax()
best_category_revenue=category_sales.max()

print("\n Best Category: ", best_category)
print("\n Best Category Revenue: ", best_category_revenue)

monthly_sales=df.groupby(df["Date"].dt.to_period("M"))["Revenue"].sum()
print("\n Monthly Sales:")
print(monthly_sales)

best_month = monthly_sales.idxmax()
best_month_revenue = monthly_sales.max()

print("\nBest Sales Month:", best_month)
print("Best Month Revenue:", best_month_revenue)

revenue_array=np.array(df["Revenue"])

print("\n Revenue Array mean:",revenue_array.mean())
print("\n Revenue Array max:",revenue_array.max())
print("\n Revenue Array min:",revenue_array.min())

print("\n===== BUSINESS INSIGHTS =====")

print(f"🏆 Best Product: {best_product}")
print(f"💰 Product Revenue: ₹{best_product_revenue}")

print(f"🌍 Best Region: {best_region}")
print(f"💰 Region Revenue: ₹{best_region_revenue}")

print(f"📦 Best Category: {best_category}")
print(f"💰 Category Revenue: ₹{best_category_revenue}")

print(f"📈 Best Sales Month: {best_month}")
print(f"💰 Monthly Revenue: ₹{best_month_revenue}")