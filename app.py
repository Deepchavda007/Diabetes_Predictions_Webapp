import pickle
import streamlit as st


diabetas_model = pickle.load(open(
    'diabetas_model.sav', 'rb'))

st.title('Diabetes Prediction')

col1, col2, col3 = st.columns(3)

with col1:
    Age = st.number_input('Age', max_value=60)

with col2:
    Glucose = st.number_input('Glucose', max_value=200)

with col3:
    BloodPressure = st.number_input('BloodPressure', max_value=200)

with col1:
    SkinThickness = st.number_input('SkinThickness', max_value=80)

with col2:
    Insulin = st.number_input('Insulin', max_value=1000)

with col3:
    BMI = st.number_input('BMI', max_value=50.0)

with col1:
    DiabetesPedigreeFunction = st.number_input(
        'DiabetesPedigreeFunction', max_value=5.0)

with col2:
    Pregnancies = st.number_input('Pregnancies', max_value=20)

# code for Prediction
diabetes = ''

if st.button('Diabetes Test Result'):
    diabetas_prediction = diabetas_model.predict(
        [[Age, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Pregnancies]])

    if (diabetas_prediction[0] == 1):
        diabetes = 'The Person has Diabetas'
        st.error(diabetes)
    else:
        diabetes = 'The Person does not have a Diabetas'
        st.success(diabetes)
