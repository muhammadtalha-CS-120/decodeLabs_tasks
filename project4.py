import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel("Dataset for data analytics.xlsx")
print(data)
data.plot(x='Product', y='TotalPrice', kind='bar')
plt.title("Total Price by Product")
plt.xlabel("Product")
plt.ylabel("Total Price")
plt.tight_layout()
plt.show()
