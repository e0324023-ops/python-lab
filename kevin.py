1.dataset
Column Name,Description,Data Type
sepal_length,Length of the sepal in cm,Numerical
sepal_width,Width of the sepal in cm,Numerical
petal_length,Length of the petal in cm,Numerical
petal_width,Width of the petal in cm,Numerical
species,"The type of Iris flower (setosa, versicolor, virginica)",Categorical (Target)


2. Code 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset('iris')
print("First 5 rows of the dataset:")
print(df.head())
print("\nSpecies counts:")
print(df['species'].value_counts())

3.bar chart
plt.figure(figsize=(7, 5))
sns.barplot(x='species', y='sepal_length', data=df, errorbar=None)
plt.title('Average Sepal Length for Each Iris Species')
plt.xlabel('Species')
plt.ylabel('Average Sepal Length (cm)')
plt.show()

4.pie chart
# Pie Chart: Distribution of Species
species_counts = df['species'].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(species_counts, 
        labels=species_counts.index, 
        autopct='%1.1f%%', 
        startangle=90, 
        colors=sns.color_palette('viridis'))
plt.title('Distribution of Iris Species')
plt.show()

5.histogram
plt.figure(figsize=(8, 6))
sns.histplot(df['petal_length'], bins=15, kde=True)
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.show()

6.line plot
plt.figure(figsize=(10, 6))
sns.lineplot(x=df_sorted.index, y='petal_length', hue='species', data=df_sorted)
plt.title('Petal Length Trend across Sorted Samples (by Species)')
plt.xlabel('Sample Index (Sorted by Petal Length)')
plt.ylabel('Petal Length (cm)')
plt.show()

7.scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='petal_length', y='petal_width', hue='species', data=df, s=80)
plt.title('Petal Length vs. Petal Width (by Species)')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.legend(title='Species')
plt.show()








