import pandas as pd

df=pd.read_excel("Dataset for data analytics.xlsx")
print(df.head())

print(df.info())
print(df.shape)
print(df.columns)


print(df.describe())

print("Quantity Count:",df["Quantity"].count())
print("Quantity mean:",df["Quantity"].mean())
print("Quantity median:",df["Quantity"].median())
print("Total Quantity:",df["Quantity"].count())
print("Total Quantity:",df["Quantity"].mean())
print("Total Quantity:",df["Quantity"].median())      



print(df["Product"].value_counts())
print(df["OrderStatus"].value_counts())

Q1 = df["TotalPrice"].quantile(0.25)
Q3=df["TotalPrice"].quantile(0.75)
IQR=Q3-Q1

lower_limit=Q1-1.5*IQR
upper_limit=Q3+1.5*IQR

outliers=df[(df["TotalPrice"]<lower_limit) | (df["TotalPrice"]>upper_limit)]
print("Number of outliers:",len(outliers))

print("Minimum TotalPrice:",df["TotalPrice"].min())
print("Maximum TotalPrice:",df["TotalPrice"].max())

df["Year"]=df["Date"].dt.year
yearly_sales=df.groupby("Year")["TotalPrice"].sum()
print("yearly_sales:",yearly_sales)

product_orders=df["Product"].value_counts()
print("product_orders:",product_orders)
