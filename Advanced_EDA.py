import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import title

# load the cleaned dataset
file_path = '/Users/moe/Desktop/Data Analytics/Soft_Eng_Sal_Analysis Project/Soft_Eng_Sal_Cleaned.csv'
df = pd.read_csv(file_path)

# salary distribution by company score: checking if higher rated companies offer higher salaries

plt.figure(figsize=(12,8))
sns.scatterplot(x='Company Score', y='Max Salary', data=df, hue='Company Score', palette='coolwarm', legend=False)
plt.title('Max Salary vs. Company Score')
plt.xlabel('Company Score')
plt.ylabel('Max Salary (in thousands)')
plt.show()

# salary distribution across locations: Using boxplot to see salary variations by location
plt.figure(figsize=(18,12))
top_locations = df['Location'].value_counts().head(10).index
sns.boxplot(x='Location', y='Max Salary', data=df[df['Location'].isin(top_locations)])
plt.xticks(rotation=45)
plt.title('Salary Distribution Across Top Locations')
plt.xlabel('Location')
plt.ylabel('Max Salary (in thousands)')
plt.show()


# Salary by job title: which job titles have the highest salary ranges

plt.figure(figsize=(19,12))
top_titles = df['Job Title'].value_counts().head(10).index
sns.barplot(y='Job Title', x='Max Salary', data=df[df['Job Title'].isin(top_titles)], estimator=max)
plt.title('Max Salary by Job Title')
plt.xlabel('Max Salary (in thousands)')
plt.ylabel('Job Title')
plt.show()

# pairwise correlation analysis
plt.figure(figsize=(14,10))
sns.heatmap(df[['Company Score', 'Min Salary', 'Max Salary']].corr(), annot=True, cmap='coolwarm', vmin=0, vmax=1)
plt,title('Correlation Matrix')
plt.show()

# box plot of salaries by company score range
df['Company Score Range']= pd.cut(df['Company Score'], bins=[1, 2, 3, 4, 5], labels=['1-2', '2-3', '3-4', '4-5'])

plt.figure(figsize=(10,6))
sns.boxplot(x='Company Score Range', y='Max Salary', data=df)
plt.title('Max Salary by Company Score Range')
plt.xlabel('Company Score Range')
plt.ylabel('Max Salary (in thousands)')
plt.show()

# location-based analysis: compare salary distribution across different regions to see how they differ
top_location = df['Location'].value_counts().head(10).index
avg_salary_by_location = df[df['Location'].isin(top_location)].groupby('Location')['Max Salary'].mean().sort_values()

plt.figure(figsize=(14,10))
avg_salary_by_location.plot(kind='barh')
plt.title('Average Max Salary by Top Location')
plt.xlabel('Average Max Salary (in thousands)')
plt.ylabel('Location')
plt.show()


# plotting the distribution of Min Salary and Max Salary
plt.figure(figsize=(12, 6))
plt.hist(df['Min Salary'], bins=30, alpha=0.5, label='Min Salary')  # Accessing the data from df
plt.hist(df['Max Salary'], bins=30, alpha=0.5, label='Max Salary')  # Accessing the data from df
plt.title('Distribution of Min and Max Salary')
plt.xlabel('Salary (in thousands)')
plt.ylabel('Frequency')
plt.legend()
plt.show()
