#loaded the dataset and checked for missing values and duplicates. Cleaned the dataset by dropping rows with missing values and saved the cleaned dataset to a new Excel file.
import pandas as pd
df=pd.read_excel("Dataset for Data Analytics.xlsx")
print(df.shape)
print(df.head())
print(df.columns)

# check for missing values
print(df.isnull().sum())
print(df[df.isnull().any(axis=1)])

# handle missing values by dropping rows with missing values
df=df.dropna()
print(df.isnull().sum())
print(df.shape)

#check for duplicates
print(df["OrderID"].duplicated().sum())

#verified the data types of the columns and converted the "Date" column to datetime format
print(df["Date"].dtype)

df["Date"]=pd.to_datetime(df["Date"])
print(df["Date"].dtype)

# verified the data types of the columns again after conversion
print(df[["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]].dtypes)
print(df[["Product", "ShippingAddress", "PaymentMethod", "OrderStatus"]].dtypes)

#verified duplicate orderids
print("Duplicate OrderIDs are:",df["OrderID"].duplicated().sum())

#verified missing dates
print("Missing Dates are:",df["Date"].isna().sum())
print("Total Missing Values are:",df.isnull().sum().sum())

#saved the cleaned dataset to a new Excel file
df.to_excel("Cleaned_Dataset.xlsx",index=False)


#Final verification of the cleaned dataset
print("=======FINAl VERIFICATION=======")
print("Total Missing Values are:",df.isnull().sum().sum())
print("Duplicate OrderIDs are:",df["OrderID"].duplicated().sum())
print("Missing Dates are:",df["Date"].isna().sum())
print("Total Rows and Columns are:",df.shape)
print("Data Types of Columns are:",df.dtypes)
print("\n Text Data Types of Columns are:\n",df[["Product", "ShippingAddress", "PaymentMethod", "OrderStatus"]].dtypes)