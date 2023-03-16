#Import the necessary libraries and load the data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# show all columns at once
pd.set_option('display.max_columns', None)
#Load the data
fifa = pd.read_csv(r'C:\Users\DELL\Desktop\dataset\archive\fifa21 raw data v2.csv')
df = fifa.copy()
# view first few rows
df.head(10)

# Check column information
print(df.info())
#Check the shape of the data
print(df.shape)

#Check the number of duplicates in the data
duplicates = df.duplicated().sum()
display('{} duplicate(s) found in this dataset'.format(duplicates))

# Missing values
total_missing = len(df) - len(df[df['Loan Date End'].notna()])
print('There are {} missing values in the Loan Date End column'.format(total_missing))
#Since this is a date column, replace missing values with pandas's NAT
df['Loan Date End'] = pd.to_datetime(df['Loan Date End'])
df['Loan Date End'] = df['Loan Date End'].replace('', pd.NaT)
#Confirm the dtypes
df['Loan Date End'].dtypes

# HANDLING INCORRECT VALUES AAND DATATYPES
def make_int(x):
    if x.endswith('M'):
        return int(float(x[:-1]) * 1000000)
    elif x.endswith('K'):
        return int(float(x[:-1]) * 1000)
    else:
        return int(x)
    
def clean_hit(s):
    # check if s ends with k
    s = str(s)
    if s[-1] == "K":
        # remove k and multiply by 1000
        return float(s[:-1]) * 1000
    else:
        # return s as int
        return float(s)
#Using loop, remove unwanted characters and change the datatype 
cols_to_clean =['Weight','W/F', 'SM','IR']
vals_to_clean =['★','€','kg','cm','K','M','lbs',]
int_col =['Weight','W/F', 'SM','IR']
for col in cols_to_clean:
    for val in vals_to_clean:
            df[col] = df[col].str.replace(val,'')
for col in int_col:
    df[col] = df[col].astype('int')
for col in cols_to_clean:
    if col not in int_col:
        df[col] = df[col].astype('float')
#Clean the Value Column
df['Value'] = df['Value'].str.strip('€')
df['Value'] = df['Value'].apply(make_int)
#clean the Release Clause Column
df['Release Clause'] = df['Release Clause'].str.strip('€')
df['Release Clause'] = df['Release Clause'].apply(make_int)         
df['Weight'] = np.where(df['Weight']>=130,round(df['Weight']*0.454), df['Weight'])
df['Weight'] = df['Weight'].astype('int')
#Cleaning The Height Column: Remove unwanted characters and convert the values recorded in feet to cm and
#Change the Data type to integer as majority of the data were recorded in integer
df['Height'] = df['Height'].str.replace("cm",'')
df['Height'] = df['Height'].str.replace(r"'",'.', regex=True)
df['Height'] = df['Height'].str.replace(r'"','', regex=True)
df['Height'] = df['Height'].astype('float')
df['Height'] = np.where(df['Height']<10, round(df['Height'] * 30.48), df['Height'])
df['Height'] = df['Height'].astype('int')
#Chean the wage column
df['Wage'] = df.Wage.str.strip('€')
df['Wage'] = df.Wage.str.replace('K','000')
df['Wage'] = df['Wage'].astype('int')
#clean Hits column
df['Hits'] = df['Hits'].apply(clean_hit)
df['Hits'] = df['Hits'].fillna(0).astype(pd.Int64Dtype())
#Check the datatypes
df.loc[:,['Weight','Height','Value','Wage','Release Clause', 'W/F', 'SM','IR','Hits']].dtypes

#Remove white space from the columns
for col in df.columns:
    if df[col].dtypes == 'object':
        df[col] = df[col].str.strip()
#Changing the datatype of joined column
df['Joined'] = pd.to_datetime(df['Joined'])
#Cleaning the Contract column
cb = df['Joined'].dt.year
ce = df['Contract'].str.split('~', expand=True).iloc[:,1]
ind = df[df['Loan Date End'].notna() == True].index
str_lde = df['Loan Date End'].astype('string')
lde_val = str_lde.str.split('-', expand = True).iloc[:,0]
for i in ind:
    ce[i] = lde_val[i]
df.insert(11, 'Contract Begins', cb)
df.insert(12, 'Contract Ends', ce)

no_club_ind = df[df['Club']=='No Club'].index
for i in no_club_ind:
    df['Contract Begins'][i] = np.nan
df['Contract Begins'] = df['Contract Begins'].astype(pd.Int64Dtype())
df['Contract Ends'] = df['Contract Ends'].str.strip()
df['Contract Ends'] = df['Contract Ends'].astype(pd.Int64Dtype())
df[['Contract Begins','Contract Ends']].info()

# Changing Column Names
new_column_names = {'LongName':'Player Name','↓OVA':'Overall Rating', 'BOV':'Best Overall rating','POT':'Potential','DRI':'Dribble','PAC':'Pace','PAS':'Passing',
                   'SHO':'Shooting','DEF':'Defend','PHY':'Physical','SM':'Skill Moves', 'IR':'International Reputation',
                   'W/F':'Weak Foot', 'A/W': 'Away win', 'D/W':'Draw', 'Height': 'Height (cm)', 'Weight': 'Weight (kg)',
                   'Value': 'Value (€)', 'Release Clause': 'Release Clausee (€)', 'Wage':'Wage (€)'}
df = df.rename(columns=new_column_names)

# Checking calculations
#Check For Base Stats
calc_base_stat= df.iloc[:,67:73].sum(axis=1)
df_base_stat=df['Base Stats']
compare = pd.DataFrame({'calculated Base stat':calc_base_stat,'df Base Stat':df_base_stat})
compare['isnt_thesame'] = compare['calculated Base stat'] != compare['df Base Stat']
#Check for Total Stats
calc_total_stat=df.iloc[:,20:61].sum(axis=1)
df_tot_stat=df['Total Stats']
compare = pd.DataFrame({'calculated Total stat':calc_total_stat,'df Total Stat':df_tot_stat})
compare['isnt_thesame'] = compare['calculated Total stat'] != compare['df Total Stat']
#Since they do not equal, correct it
df['Total Stats'] = compare['calculated Total stat']
display(df.iloc[:5,60:])
df.shape

# Droping irrelevant columns
df.drop(['Name','photoUrl','playerUrl','Contract'],axis=1, inplace=True)
print(df.columns)
print('\nThe total columns after cleaning is {}'.format(len(df.columns)))
df.columns
