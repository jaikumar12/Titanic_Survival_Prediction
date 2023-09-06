import pandas as pd
import numpy as np
import streamlit as st
import pickle 


## Loading the Savel model

survival_model = pickle.load(open('model.pkl','rb'))

## Create empty tuple to store the inputs Data
input_data = ()

## Streamlit app

st.title("Survival Prediction")
st.header('User input')

## Input for Pclass
Pclass_input = st.text_input("Enter data for Pclass:")
if Pclass_input:
    try:
        Pclass_input = int(Pclass_input)  # Convert to int
        input_data += (Pclass_input,)
    except ValueError:
        st.warning("Pclass_input must be an integer.")
                   
## Input for Sex

Sex_input = st.text_input("Enter data for Sex :")
if Sex_input:
    try:
        Sex_input = int(Sex_input)   ## Convert to int
        input_data += (Sex_input,)
    except ValueError:
        st.warning('Sex_input must be an integer.')  
                   
## Input For Age 

Age_input = st.text_input("Enter data for Age :")
if Age_input:
    try:
        Age_input = int(Age_input)   ## Convert to int
        input_data += (Age_input,)
    except ValueError:
        st.warning('Age_input must be an integer.')
                   
## Input For SibSp(sibling and Spouse)                  

SibSp_input = st.text_input("Enter data for SibSp :")
if SibSp_input:
    try:
        SibSp_input = int(SibSp_input)   ## Convert to int
        input_data += (SibSp_input,)
    except ValueError:
        st.warning('SibSp_input must be an integer.')  
        
## Input for Parch(parents)                    
                   
Parch_input = st.text_input("Enter data for Parch :")
if Parch_input:
    try:
        Parch_input = int(Parch_input)   ## Convert to int
        input_data += (Parch_input,)
    except ValueError:
        st.warning('Parch_input must be an integer.')                   
                   
## Input for Fare

Fare_input = st.text_input("Enter data for Fare:")
if Fare_input:
    try:
        Fare_value = float(Fare_input)  # Convert to float
        input_data += (Fare_value,)
    except ValueError:
        st.warning("Fare input must be a float.")
                   
## Input for Embarked                   

Embarked_input = st.text_input("Enter data for Embarked :")
if Embarked_input:
    try:
        Embarked_input = int(Embarked_input)   ## Convert to int
        input_data += (Embarked_input,)
    except ValueError:
        st.warning('Embarked_input must be an integer.')
                   
                   
# Submit Button
if st.button("Predict"):
    if len(input_data) == 7:
        
        # Convert the input_data to a NumPy array and reshape it
        input_data_as_numpy_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

        # Make the prediction using your final_logit_model (replace this with your model)
        prediction = survival_model.predict(input_data_reshaped)
        # Uncomment the line above and replace it with your model prediction code.

        # Mocking a prediction (replace this with your actual prediction result)
          # Replace with the actual prediction value

        # Display the prediction result
        if prediction[0] == 0:
            st.markdown('<p style="font-size:24px; font-weight:bold; color:red;">The Person is not Survived</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p style="font-size:24px; font-weight:bold; color:red;">The Person Survived</p>', unsafe_allow_html=True)
    else:
        st.warning("Please fill in all Seven columns before predicting.")     
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   