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
