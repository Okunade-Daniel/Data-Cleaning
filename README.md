# Data-Cleaning
> Preparing the Fifa players' Data for analysis
# INTRODUCTION
Data Cleaning is a vital skill for Data Analysts as it prepares and validates data for analysis. Data Cleaning is the process of tidying the data within a dataset. It involves fixing or removing incomplete, corrupted, inconsistent, wrongly formatted or duplicated data. This is important because it ensures the accuracy and reliability of data analysis.

Sometimes, data may become messy or dirty when combining them from different sources, therefore, making it necessary to clean before use. If data is incorrect, insights generated and models trained cannot be relied upon even if they look correct. Data cleaning improves the quality of the data by reducing errors, removing irrelevant information, making the data consistent and preparing data for transformation. Having clean data can help improve decision-making, customer satisfaction, business performance, and analytics.

# PROJECT OBJECTIVES
The objective of this project is to clean the data made available in the #DataCleaningChallenge and make it ready for use for analysis.
PROBLEMS TO LOOK OUT FOR IN THE DATA
•	Duplicates
•	Missing values
•	Incorrect values and Datatypes
•	Handle Column Names
•	Irrelevant Data
•	Calculations

# PROJECT APPROACH
1.	LOOKING AT THE DATA AVAILABLE: Here, I look at the first few rows of the data to get an idea of how the data looks. I looked at the columns information as well as the shape of the data. Looking at the shape of the data, there were 18979 rows each representing a player and 77 columns representing each player features. The data shows a lot of incorrectness. Like the star symbols in columns like the IR column, non-meaningful column names like OVA, incorrect datatypes like Weight inconsistent values like Hits and so on. After going through the individual columns I noted down the things I will like to correct in the columns.
2.	CHECKING FOR DUPLICATES: Duplicates occur when data is entered more than once. I checked for the duplicates in the data and there was none. So, I moved to the next phase.
3.	HANDLING MISSING VALUES: From the column information obtained, Loan Date End and Hits columns were the only columns containing missing values. To treat the Loan Date End Column missing values. I first checked the number of values missing in the column. I also took my time to understand why there are missing values in the columns. I understood that not all players are on loan so it makes sense that the columns contains null. I Changed the data type from object to datetime  and filled the empty cells with pandas’ NaT. For the Hits column, there are also other inconsistency in the column, so I left it to be resolved in the next step.
4.	HANDLING INCONSISTENT VALUES AND DATATYPES: I divided this step into 2. To treat the Numeric/Columns that should be numeric and columns that should be strings.
a.	Numeric Columns: Here I cleaned the Hits, Value, Release Clause, Wage, Height, Weight, W/R, SM, IR columns. Using loops, I was able to remove the special characters in columns like W/R, SM, IR. By defining a function, I was able to standardize the values in columns like Hits, Value, Release Clause, Wage, Height and Weight. I also changed the datatypes to integers. For the Hits Column containing missing values. I filled the missing values with zero (0) after understanding that it is possible that the link to some players profiles may not have been clicked before especially if they are not popular.
b.	 String Columns: Using Loop, I removed all extra space in the string columns. I also split the Contract column on the (~) delimiter into Contract Begin and Contract Ends for all players including those on loans. Some of the values were also set to null for players who currently have no clubs.
5.	COLUMN NAMES: In this step, I renamed  the columns to make them more readable and understandable
6.	CHECKING CALCULATIONS: I confirmed the calculations made in the Base Stats column by adding the pace, shooting, defend, dribble, passing and physical columns. I also did the same for the Totals Stats. The values did not match so I corrected the values in the Total Stats column.
7.	IRRELEVANT DATA: In this Final step, I removed the columns that gives no additional meaning to the data.  

# CONCLUSION
I started the data cleaning process 18979 rows and 77 columns of data and after the cleaning, I was left with 18979 rows and 75 columns.

