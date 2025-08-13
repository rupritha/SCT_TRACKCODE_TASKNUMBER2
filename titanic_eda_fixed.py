import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the data
df = pd.read_csv('c:/Users/rupri/Downloads/titanic (2)/train.csv')

# 2. Basic Info
print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nInfo:")
print(df.info())
print("\nMissing values:\n", df.isnull().sum())

# 3. Data Cleaning
# Handling missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df = df.drop('Cabin', axis=1)  # Too many missing values

# Verify no missing values
print("\nAfter cleaning:\n", df.isnull().sum())

# 4. Exploratory Data Analysis (EDA)
# Survival rate
print("\nSurvival rate:\n", df['Survived'].value_counts(normalize=True))
sns.countplot(x='Survived', data=df)
plt.title('Survival Count')
plt.show()

# Gender and survival
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title('Survival Count by Gender')
plt.show()

# Passenger Class and survival
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title('Survival Count by Class')
plt.show()

# Age distribution
sns.histplot(df['Age'], kde=True)
plt.title('Age Distribution')
plt.show()

# Age vs Survival
sns.boxplot(x='Survived', y='Age', data=df)
plt.title('Age by Survival')
plt.show()

# Correlation heatmap - select only numeric columns
numeric_df = df.select_dtypes(include=[np.number])
plt.figure(figsize=(10,6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Explore relationship between Fare and Survival
sns.boxplot(x='Survived', y='Fare', data=df)
plt.title('Fare by Survival')
plt.show()

# Pattern: Family size and survival
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
sns.countplot(x='FamilySize', hue='Survived', data=df)
plt.title('Survival by Family Size')
plt.show()

print("\nDone with EDA!")
