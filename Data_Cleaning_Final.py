import pandas as pd
import re
from datetime import datetime, timedelta
from statistics import median

# load dataset
file_path = '/Users/moe/Desktop/Data Analytics/Soft_Eng_Sal_Analysis Project/Software Engineer Salaries.csv'
df = pd.read_csv(file_path)

# function to extract min and max salary
def extract_salary(salary_str):
    if isinstance(salary_str, str):
        salary_range = re.findall(r'\d+', salary_str)
        if len(salary_range) == 2:
            min_salary = int(salary_range[0])
            max_salary = int(salary_range[1])
            return min_salary, max_salary
        return None, None

# apply above function to the 'Salary' column and creat new column for Min and Max Salary
df[["Min Salary", "Max Salary"]] = df["Salary"].apply(lambda x: pd.Series(extract_salary(x)))

# fill missing values in 'Company' and 'Location'
df.fillna({"Company": "Unknown"}, inplace=True)
df.fillna({"Location": "Unknown"}, inplace=True)

# imputing missing 'Company Score' values with median score
df.fillna({"Company Score": df["Company Score"].median()}, inplace=True)

# drop rows with missing Min and Max Salary
df.dropna(subset=['Min Salary', 'Max Salary'], inplace=True)

# convert relative dates to actual date
current_date = datetime.now()
def convert_relative_date(date_str):
    date_str = date_str.replace('+', '')
    if 'd' in date_str:
        days_ago = int(date_str.replace('d', ''))
        return current_date - timedelta(days=days_ago)
    elif 'w' in date_str:
        weeks_ago = int(date_str.replace('w', ''))
        return current_date - timedelta(weeks=weeks_ago)
    return None

df['Date'] = df['Date'].apply(convert_relative_date)

# save cleaned dataset to a new CSV file
cleaned_file_path = 'Soft_Eng_Sal_Cleaned.csv'
df.to_csv(cleaned_file_path, index=False)
print(f"Cleaned dataset saved to {cleaned_file_path}")

