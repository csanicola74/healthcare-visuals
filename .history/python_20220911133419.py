# *visualization-covid19-georgia*

# the below packages are related to loading and performing basic
# transformations of the data

import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

print('cell successfully ran')

# now we are going to load in some visualization packages to help with create
# visuals of the data


sns.set_theme(style="whitegrid")
print('cell successfully ran')

## Loading in Data
dataframe = pd.read_csv(
    'https://raw.githubusercontent.com/hantswilliams/AHI_Microcourse_Visualization/main/Data/Georgia_COVID/Georgia_COVID-19_Case_Data.csv')
dataframe

len(dataframe)

dataframe.shape

# Describing the variables
dataframe.info()

list(dataframe)

dataframe['COUNTY'].value_counts()

dataframe_counties = dataframe['COUNTY'].value_counts()
dataframe_counties.head(5)

# Transforming Columns
dataframe['DATESTAMP']

# creating a copy of the existing column, so we keep the original version
# we could also override the column if we wanted to, but because we are unsure
# where we are going to take the analysis - lets just keep it

dataframe['DATESTAMP_MOD'] = dataframe['DATESTAMP']
print(dataframe['DATESTAMP_MOD'].head(10))
print(dataframe['DATESTAMP_MOD'].dtypes)

dataframe['DATESTAMP_MOD'] = pd.to_datetime(dataframe['DATESTAMP_MOD'])
dataframe['DATESTAMP_MOD'].dtypes

dataframe[['DATESTAMP', 'DATESTAMP_MOD']]

dataframe['DATESTAMP_MOD_DAY'] = dataframe['DATESTAMP_MOD'].dt.date
dataframe['DATESTAMP_MOD_DAY']

dataframe['DATESTAMP_MOD_YEAR'] = dataframe['DATESTAMP_MOD'].dt.year
dataframe['DATESTAMP_MOD_MONTH'] = dataframe['DATESTAMP_MOD'].dt.month

dataframe['DATESTAMP_MOD_YEAR']

dataframe['DATESTAMP_MOD_MONTH']
dataframe

dataframe['DATESTAMP_MOD_MONTH_YEAR'] = dataframe['DATESTAMP_MOD'].dt.to_period(
    'M')
dataframe['DATESTAMP_MOD_MONTH_YEAR'].sort_values()
dataframe

dataframe['DATESTAMP_MOD_WEEK'] = dataframe['DATESTAMP_MOD'].dt.week
dataframe['DATESTAMP_MOD_WEEK']

dataframe['DATESTAMP_MOD_QUARTER'] = dataframe['DATESTAMP_MOD'].dt.to_period(
    'Q')
dataframe['DATESTAMP_MOD_QUARTER']

dataframe['DATESTAMP_MOD_QUARTER'].sort_values()

dataframe['DATESTAMP_MOD_DAY_STRING'] = dataframe['DATESTAMP_MOD_DAY'].astype(
    str)
dataframe['DATESTAMP_MOD_WEEK_STRING'] = dataframe['DATESTAMP_MOD_WEEK'].astype(
    str)
dataframe['DATETIME_STRING'] = dataframe['DATESTAMP_MOD_MONTH_YEAR'].astype(
    str)
dataframe

# Getting the counties required for our analysis
# We know that the counties we want to analysis our:
#   * Cobb
#   * DeKalb
#   * Fulton
#   * Gwinnett
#   * Hall

dataframe['COUNTY']

countList = ['COBB', 'DEKALB', 'FULTON', 'GWINNETT', 'HALL']
countList

selectCounties = dataframe[dataframe['COUNTY'].isin(countList)]
len(selectCounties)

# Getting just the specific date/time frame we want
# dataframe = length ~90,000
# selectCounties = length 2,830
# selectCountyTime = ???/TBD
