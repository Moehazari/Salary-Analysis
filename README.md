# Salary-Analysis
Software Engineer Salaries Data Analysis
Project Overview
This project aims to explore and analyze a dataset containing salary information for Software Engineering roles in the United States. The data analysis covers a range of aspects, including salary distributions, company ratings, location-based salary variations, and more. The project provides valuable insights into factors that influence software engineering salaries and trends within the industry.

Table of Contents
Project Overview
Data Cleaning
Exploratory Data Analysis (EDA)
Hypothesis 1
Hypothesis 2
Hypothesis 3
Hypothesis 4
Hypothesis 5
Hypothesis 6
Hypothesis 7
Conclusion
Technologies Used
Project Setup
Data Cleaning
The dataset was cleaned to remove inconsistencies and prepare it for analysis. Key cleaning steps included:

Parsing the Salary Ranges: The Salary column, originally containing text ranges, was split into Min Salary and Max Salary.
Handling Missing Values: Missing Company, Location, and Company Score values were filled with appropriate placeholders or imputed values.
Standardizing Date Formats: The Date column, initially in relative terms (e.g., "2d" for two days ago), was converted into absolute dates.
Filtering United States: Entries marked as "United States" were either replaced with more specific cities or standardized to indicate remote roles.
Exploratory Data Analysis (EDA)
The EDA explored various relationships within the dataset, providing insights into factors that affect salary ranges. Seven hypotheses were tested:

Hypothesis 1: Higher Company Scores Correlate with Tighter Salary Ranges
Description: Companies with higher scores may offer more consistent salaries due to well-defined pay bands.
Analysis: A box plot of Salary Range by Company Score was used to observe the distribution.
Findings: Companies with higher scores tend to show [consistent/inconsistent] salary ranges.
Hypothesis 2: Remote Positions Offer More Competitive Salaries
Description: Remote roles may offer higher salaries to attract a wider pool of talent.
Analysis: A box plot of Max Salary by Location Type (Remote vs. On-Site) was used for comparison.
Findings: Remote positions were found to have [higher/lower/similar] salaries compared to on-site roles.
Hypothesis 3: Senior-Level Roles Show a Wider Range in Salary
Description: Senior positions might exhibit greater salary variation due to diverse responsibilities and skill levels.
Analysis: A violin plot of Salary Range by Role Level (Senior, Mid, Junior) was used to analyze distribution.
Findings: Senior roles displayed a [wider/narrower/similar] range in salary.
Hypothesis 4: Jobs in Tech Hubs Offer Higher Salaries
Description: Highly-populated tech hubs like San Francisco, Seattle, and New York likely offer higher salaries due to competition.
Analysis: A box plot of Max Salary by Location (Tech Hub vs. Non-Tech Hub) was created.
Findings: Tech hub locations had [higher/lower/similar] salaries on average.
Hypothesis 5: Companies with Higher Scores Are More Likely to Offer Remote Positions
Description: Highly-rated companies might provide remote options to attract top talent.
Analysis: A stacked bar plot was created to show the proportion of Remote vs. On-Site positions by Company Score.
Findings: Companies with higher scores had a [higher/lower/similar] proportion of remote roles.
Hypothesis 6: Higher Salaries Are More Common in Recent Job Postings
Description: Recent job postings may reflect current market trends, including higher salaries due to increased demand for software engineers.
Analysis: A line plot showing average Max Salary over time.
Findings: Recent job postings showed a [higher/lower/constant] salary trend.
Hypothesis 7: Certain Job Titles Command Premium Salaries Across Locations
Description: Titles like "Senior Software Engineer" or "Data Scientist" may consistently offer high salaries regardless of location.
Analysis: A box plot of Max Salary for selected job titles across various locations.
Findings: Specific job titles commanded [premium/similar] salaries across locations.
Conclusion
This analysis provided insights into the factors that influence software engineering salaries in the United States. The results show patterns based on company score, location, role level, and remote options, highlighting trends within the software engineering job market. These findings can be beneficial for job seekers, recruiters, and companies to understand salary dynamics.

Technologies Used
Python: Data analysis and visualization (pandas, matplotlib, seaborn)
SQL: Querying the dataset in PostgreSQL 

