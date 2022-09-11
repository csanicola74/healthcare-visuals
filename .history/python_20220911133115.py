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
