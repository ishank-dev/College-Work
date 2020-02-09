import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

student_df = pd.read_csv("StudentsPerformance.csv")

print("======Data Headers=======")
student_df.head()

print("=====Data Decription=====")
student_df.info()
student_df.describe()

student_df1 = student_df.drop(['lunch', 'test preparation course'], axis=1)
student_df1.head()

student_df1["parental level of education"] = student_df1["parental level of education"].fillna("high school")
print(student_df1["parental level of education"])

# student_df1["race/ethnicity"] = student_df1['race/ethnicity'].map({
#     "group A": "Asian Students",
#     "group B": "African Students",
#     "group C": "Afro-Asian Students",
#     "group D": "American Students",
#     "group E": "European Students"
# })

print(student_df1.head(10))

ax = sns.countplot(x="test preparation course", hue="gender", palette="Set1", data=student_df)
ax.set(title="Test Preparation", xlabel="Course", ylabel="Total")
plt.show()

# ax = sns.countplot(x="race/ethnicity", hue="gender", palette="Set1", data=student_df1)
# ax.set(title="Students according to each group", xlabel="Ethnicity", ylabel="Total")
# plt.show()

# marks_intervals = [0, 40, 50, 60, 75]
# categories = ['failed', 'second class', 'first class', 'distinction']
# student_df1['Marks_Categories_math'] = pd.cut(student_df1.mathscore, marks_intervals, labels=categories)
# ax = sns.countplot(x="Marks_Categories_math", hue="gender", palette="Set1", data=student_df1)
# ax.set(title="Math Marks Grouping", xlabel="Marks Groups", ylabel="Total")
# plt.show()

# student_df1['Marks_Categories_reading'] = pd.cut(student_df1.readingscore, marks_intervals, labels=categories)
# ax = sns.countplot(x="Marks_Categories_reading", hue="gender", palette="Set1", data=student_df1)
# ax.set(title="Reading Marks Grouping", xlabel="Marks Groups", ylabel="Total")
# plt.show()

# student_df1['Marks_Categories_writing'] = pd.cut(student_df1.writingscore, marks_intervals, labels=categories)
# ax = sns.countplot(x="Marks_Categories_writing", hue="gender", palette="Set1", data=student_df1)
# ax.set(title="Writing Marks Grouping", xlabel="Marks Groups", ylabel="Total")
# plt.show()
