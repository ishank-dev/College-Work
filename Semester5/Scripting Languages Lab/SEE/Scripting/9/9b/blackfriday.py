import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

black_df = pd.read_csv("BlackFriday.csv")

print("======Data Headers=======")
black_df.head() #first 5 rows

print("=====Data Decription=====")
black_df.info() # object, attributes with their datatypes 
black_df.describe() # gives all data statistics 

black_df = black_df.drop(['User_ID', 'Product_ID', 'Stay_In_Current_City_Years'], axis=1)
black_df.head()

black_df["City_Category"] = black_df["City_Category"].fillna("B")
print(black_df["City_Category"])

black_df["City_Category"] = black_df['City_Category'].map({
    "A": "Metro Cities",
    "B": "Small Towns",
    "C": "Villages"
})

print(black_df.head(10))

# black_df["Marital_Status"] = black_df['Marital_Status'].map({
#     1: "Married",
#     0: "Un-married"
# })

# print(black_df.head(10))

# black_df.rename(columns={"Product_Category_1":"Baseball Caps","Product_Category_2":"Wine tumblers","Product_Category_3":"Pet Raincoats"},inplace=True)

# print(black_df.head(10))

# black_df["Wine tumblers"] = black_df["Wine tumblers"].fillna("5")
# black_df["Pet Raincoats"] = black_df["Pet Raincoats"].fillna("10")

# print(black_df.head(10))

# ax = sns.countplot(x="Baseball Caps", hue="Gender", palette="Set1", data=black_df)
# ax.set(title="Product Category 1", xlabel="Categories", ylabel="Total")
# plt.show()

# ax = sns.countplot(x="Wine tumblers", hue="Gender", palette="Set1", data=black_df)
# ax.set(title="Product Category 2", xlabel="Categories", ylabel="Total")
# plt.show()

ax = sns.countplot(x="City_Category", hue="Gender", palette="Set1", data=black_df)
ax.set(title="City Category", xlabel="Categories", ylabel="Total")
plt.show()
