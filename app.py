import pandas as pd
import streamlit as st
import plotly.express as px

vehicles = pd.read_csv('vehicles_us.csv')
#filling in missing values 
vehicles_filled = vehicles.copy()
#creating a copy of the orginal dataframe

# Handling missing values
vehicles.dropna(inplace=True)  # Or use other methods like filling missing values

# Renaming columns for better readability
vehicles.rename(columns={'column_name': 'new_name'}, inplace=True)

# Converting data types if necessary
vehicles['price'] = vehicles['price'].astype(float)

# Display the cleaned data
vehicles.head()

# Filling missing values
# Fill missing 'model_year' values by the median year for each model
vehicles['model_year'] = vehicles.groupby('model')['model_year'].transform(lambda x: x.fillna(x.median()))

# Fill missing 'cylinders' values by the median cylinders for each model
vehicles['cylinders'] = vehicles.groupby('model')['cylinders'].transform(lambda x: x.fillna(x.median()))

# Fill missing 'odometer' values by the median odometer for each model year
vehicles['odometer'] = vehicles.groupby(['model_year', 'model'])['odometer'].transform(lambda x: x.fillna(x.mean()))

st.header('Vehicles Distribution')

show_data = st.checkbox("Show Data")
if show_data: 
    st.write(vehicles.head())


#histogram for price distribution
fig = px.histogram(vehicles, x='price', title='Distribution of Car Prices', labels={'x':'Price'})
st.plotly_chart(fig)


#scatterplot between price and odometer
fig = px.scatter(vehicles, x='odometer', y='price', title='Price vs Mileage', labels={'x':'Odometer Reading', 'y':'Price'})
st.plotly_chart(fig)
