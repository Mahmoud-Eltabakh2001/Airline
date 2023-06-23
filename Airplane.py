
import joblib
import lightgbm as ltb
import streamlit as st
import numpy as np
import pandas as pd
st.set_option('deprecation.showPyplotGlobalUse', False)

model=joblib.load("Airplane.pkl")

def predict_Airplane_price(Airline, Source, Destination, Total_Stops, month,day,day_name,duration_min):
    prediction =model1.predict( pd.DataFrame({"Airline":[Airline],
                                      "Source":[Source],
                                      "Destination":[Destination],
                                      "Total_Stops":[Total_Stops],
                                      "month":[month],
                                      "day":[day],
                                      "day_name":[day_name],
                                      "duration_min":[duration_min]} ,index=[1] ) )
    return round(prediction[0])

def main():
    
    st.set_page_config(layout="wide")


      
       html_temp = """
                        <div style="background-color:tomato;padding:10px">
                        <h2 style="color:white;text-align:center;">Find out price of Airline</h2>
                        </div>
                   """
       st.markdown(html_temp,unsafe_allow_html=True)
       st.title("")

       Airline=st.selectbox("choose airline.",['IndiGo', 'Air India', 'Jet Airways', 'SpiceJet','Multiple carriers', 'GoAir', 'Vistara', 'Air Asia','Vistara Premium economy', 'Jet Airways Business',
                                              'Multiple carriers Premium economy', 'Trujet'])

       Source=st.selectbox("Select your Source.",['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai'])

       Destination=st.selectbox("Select your destination.",['Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Hyderabad'])

       Total_Stops=st.selectbox("Choose number of stops",[0, 1,2, 3, 4])

       month=st.selectbox("month of Airline",[ 3,  1,  9, 12,  6,  5,  4])  

       day=st.selectbox("Day of Airline",[24,  5,  6,  3, 27, 18, 15, 21,  4]) 

       day_name=st.selectbox("Value added",['Sunday', 'Saturday', 'Friday', 'Thursday', 'Monday', 'Tuesday', 'Wednesday']) 

       duration_min=st.slider("enter duration of airline in minute ",min_value=0,max_value=3000,step=5) 


       result=""
       if st.button("Predict"):
          result=predict_Airplane_price(Airline,Source,Destination,Total_Stops,month,day,day_name,duration_min)
          st.success("Expected trip price : {} $".format(result)) 
