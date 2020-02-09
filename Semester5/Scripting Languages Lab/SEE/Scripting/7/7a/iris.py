import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
iris_df=pd.read_csv('iris.csv')
print('---DataFrame---')
print(iris_df)
print('---info---')
iris_df.info()
print('---Functions---')
print(iris_df[['Species','Petal.Width']].groupby(['Species'],as_index=True).mean())

ax=sns.countplot(x="Sepal.Width", hue="Species",data=iris_df, palette="Set1")
ax.set(title="Categorization of flowers based on sepal width", xlabel="Categories",ylabel="Total")
plt.show()

# interval=(0,1,2,3)
# categories=['<0','1-2','>2']
# iris_df['flowers_cats']=pd.cut(iris_df['Petal.Width'],interval,labels=categories)
# ax = sns.countplot(x = 'flowers_cats',  data = iris_df, hue = 'Species', palette = 'Set2')
# ax.set(xlabel='Flowers Categorical', ylabel='Total',title="Writing Marks Categorical Distribution")
# plt.show()

# ax = sns.countplot(x = 'Sepal.Width', hue = 'Species', palette = 'Set3',data = iris_df)
# ax.set(title="Flowers Categorical",xlabel="Species", ylabel="total")
# plt.show()
