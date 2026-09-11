
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('/content/sample_data_cleaning_project - Sample_data_cleaning_project.csv')
print(data.head())
print(data.isnull().sum())
data['Age'] = data['Age'].fillna(data['Age'].median())
data['Salary'] = data['Salary'].fillna(data['Salary'].mean())
data = data.dropna(subset=['Join_Date'])

# Convert object columns to strip whitespace and then convert to lowercase
for col in data.select_dtypes(include='object').columns:
    data[col] = data[col].str.strip()
    data[col] = data[col].str.lower()
data = data.drop_duplicates(subset=['name', 'age', 'join_date'])

q1 = data['salary'].quantile(0.25)
q3 = data['salary'].quantile(0.75)
iqr = q3 - q1
data = data[(data['salary'] >= q1 - 1.5 * iqr) & (data['salary'] <= q3 + 1.5 * iqr)]

data['join_date'] = pd.to_datetime(data['join_date'])

data = pd.get_dummies(data, columns=['department'])

data.to_csv('cleaned_data.csv', index=False)

data[['department_hr', 'department_it']].sum().plot(kind='bar')
plt.title('Department Distribution')
plt.show()
data['salary'].hist()
plt.title('Salary Distribution')
plt.show()
