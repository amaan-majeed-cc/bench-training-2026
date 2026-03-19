# Exercise: Answer 10 Questions with Code
# 01. How many passengers survived vs. didn't? Show as counts and percentages.
# 02. What was the survival rate by passenger class (1st, 2nd, 3rd)?
# 03. Average age of survivors vs. non-survivors.
# 04. Which embarkation port had the highest survival rate?
# 05. How many passengers have missing age values? Fill missing ages with the median age
# for that passenger class.
# 06. Who was the oldest surviving passenger? Print their name, age, class.
# 07. What % of women survived vs. what % of men?
# 08. Create a new column 'AgeGroup': Child (<18), Adult (18-60), Senior (60+). Show survival
# rate per group.
# 09. Among 3rd class passengers, what was the survival rate for men vs. women?
# 10. Drop all rows with missing Cabin data. How many rows remain? What % of original data did you keep?


import pandas as pd

# Load the dataset
df = pd.read_csv('titanic.csv')

# 01. How many passengers survived vs. didn't? Show as counts and percentages.
print(f'--------------------------------\n 01. How many passengers survived vs. didn\'t? Show as counts and percentages.\n--------------------------------')
print(f'Survivors: {df["Survived"].value_counts()[1]} - {df["Survived"].value_counts(normalize=True)[1] * 100:.2f}%')
print(f'Could not survive: {df["Survived"].value_counts()[0]} - {df["Survived"].value_counts(normalize=True)[0] * 100:.2f}%')

# 02. What was the survival rate by passenger class (1st, 2nd, 3rd)?
print(f'\n\n--------------------------------\n 02. What was the survival rate by passenger class (1st, 2nd, 3rd)?\n--------------------------------')
rate = df.groupby('Pclass')['Survived'].mean() * 100

for pclass, val in rate.items():
    print(f"Passenger Class {pclass} survival rate: {val:.2f}%")

# 03. Average age of survivors vs. non-survivors.
print(f'\n\n--------------------------------\n 03. Average age of survivors vs. non-survivors.\n--------------------------------')
print(f'Average age of survivors: {df[df["Survived"] == 1]["Age"].mean():.2f}')
print(f'Average age of non-survivors: {df[df["Survived"] == 0]["Age"].mean():.2f}')

# 04. Which embarkation port had the highest survival rate?
print(f'\n\n--------------------------------\n 04. Which embarkation port had the highest survival rate?\n--------------------------------')
embarkation_survival_rate = df.groupby('Embarked')['Survived'].mean() * 100
highest_survival_port = embarkation_survival_rate.idxmax()
print(f'Embarkation port with the highest survival rate: {highest_survival_port} - {embarkation_survival_rate[highest_survival_port]:.2f}%')

# 05. How many passengers have missing age values? Fill missing ages with the median age for that passenger class.
print(f'\n\n--------------------------------\n 05. How many passengers have missing age values? Fill missing ages with the median age for that passenger class.\n--------------------------------')

missing_age_count = df['Age'].isnull().sum()
print(f'Number of passengers with missing age values: {missing_age_count}')
average_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(average_age)

print(f'Filled missing ages with the average age: {average_age:.2f}')

# 06. Who was the oldest surviving passenger? Print their name, age, class.
print(f'\n\n--------------------------------\n 06. Who was the oldest surviving passenger? Print their name, age, class.\n--------------------------------')
oldest_survivor = df[df['Survived'] == 1].sort_values(by='Age', ascending=False).iloc[0]
print(f'Name: {oldest_survivor["Name"]}, Age: {oldest_survivor["Age"]}, Class: {oldest_survivor["Pclass"]}')

# 07. What % of women survived vs. what % of men?

embarkation_survival_rate = df.groupby('Sex')['Survived'].mean() * 100
print(f'\n\n--------------------------------\n 07. What % of women survived vs. what % of men?\n--------------------------------')
for gender, val in embarkation_survival_rate.items():
    print(f"{gender} survival rate: {val:.2f}%")

# 08. Create a new column 'AgeGroup': Child (<18), Adult (18-60), Senior (60+). Show survival rate per group.
print(f'\n\n--------------------------------\n 08. Create a new column \'AgeGroup\': Child (<18), Adult (18-60), Senior (60+). Show survival rate per group.\n--------------------------------')
bins = [0, 18, 60, 100]
labels = ['Child', 'Adult', 'Senior']

df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
rate = df.groupby('AgeGroup', observed=True)['Survived'].mean() * 100
for age_group, val in rate.items():
    print(f"{age_group} survival rate: {val:.2f}%")

# 09. Among 3rd class passengers, what was the survival rate for men vs. women?
print(f'\n\n--------------------------------\n 09. Among 3rd class passengers, what was the survival rate for men vs. women?\n--------------------------------')

third_class = df[df['Pclass'] == 3]
survival_rate = third_class.groupby('Sex')['Survived'].mean() * 100
for gender, val in survival_rate.items():
    print(f"{gender} survival rate in 3rd class: {val:.2f}%")

# 10. Drop all rows with missing Cabin data. How many rows remain? What % of original data did you keep?
print(f'\n\n--------------------------------\n 10. Drop all rows with missing Cabin data. How many rows remain? What % of original data did you keep?\n--------------------------------')

original_count = len(df)
df_dropped = df.dropna(subset=['Cabin'])
remaining_count = len(df_dropped)
percentage_kept = (remaining_count / original_count) * 100
print(f'Number of rows remaining after dropping missing Cabin data: {remaining_count}')
print(f'Percentage of original data kept: {percentage_kept:.2f}%')
