import streamlit as st
import joblib

PCI=joblib.load("Canada_PCI.pkl")
housing=joblib.load("HousePricePredict.pkl")
st.sidebar.title("Pages")
#page=st.sidebar.selectbox("Select Model",['PCI','HousingPrice']) # to select multiple values
page=st.sidebar.radio("Select Model",options=['PCI','HousingPrice']) # to select one value
if page=="PCI":
    st.title('Per Capita Income of Canada')
    st.write('This is a simple web app to predict the per capita income of Canada')
    year=st.number_input('Enter the year')
    prediction=PCI.predict([[year]])
    if st.button('Predict'):
        st.write(prediction[0])
else:
    st.title('House Price Prediction')
    st.write('This is a simple web app to predict the house price')
    SQFT=st.number_input('Enter the Squarefeet',min_value=100)
    room=st.number_input('Enter the number of bedrooms')
    age=st.slider('Enter the age of the house',0)
    
    prediction=housing.predict([[SQFT,room,age]])
    if st.button('Predict'):
        st.write(prediction[0])