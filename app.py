import pandas as pd
import streamlit as st
import plotly.express as px

vehicles = pd.read_csv('vehicles_us.csv')
#filling in missing values 
vehicles_filled = vehicles.copy()
#creating a copy of the orginal dataframe

#fill model year with median
vehicles_filled['model_year'].fillna(vehicles_filled['model_year'].median(), inplace=True)

#fill cylinders with mode 
vehicles_filled['cylinders'].fillna(vehicles_filled['cylinders'].mode()[0], inplace=True)

#fill odometer with median
vehicles_filled['odometer'].fillna(vehicles_filled['odometer'].median(), inplace=True)

#fill is_4wd with mode
vehicles_filled['is_4wd'].fillna(vehicles_filled['is_4wd'].mode()[0], inplace=True)

#check to make sure there are no more missing values in columns (vehicles_filled[['model_year', 'cylinders', 'odometer', 'is_4wd']].isna().sum())

st.header('Vehicles Distribution')

show_data = st.checkbox("Show Data")
if show_data: 
    st.write(vehicles.head())

#histogram for price distribution
fig = px.histogram(vehicles, x='price', title='Vehicle Price Distribution')
st.plotly_chart(fig)

#scatterplot between price and odometer
fig = px.scatter(vehicles, x='odometer', y='price', color='condition',
                 title='Price vs Odometer by Vehicle Condition')
st.plotly_chart(fig)

