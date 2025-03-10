import pickle
import streamlit as st
from streamlit_option_menu import option_menu
model=pickle.load(open('diabetes.pkl','rb'))
heart_model=pickle.load(open('heart.pkl','rb'))

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Attack Prediction'],
                          icons=['activity','heart'],
                          default_index=0)
if (selected == 'Diabetes Prediction'):   

   st.title('Diabetes Prediction')
   Pregnancies = st.text_input('Number of Pregnancies')
   Glucose = st.text_input('Glucose Level')
   BloodPressure = st.text_input('Blood Pressure value')
   SkinThickness = st.text_input('Skin Thickness value')
   Insulin = st.text_input('Insulin Level')
   BMI = st.text_input('BMI value')
   DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
   Age = st.text_input('Age of the Person')
   if st.button('Predict'):
     makeprediction=model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
     print(makeprediction)
     
     if (makeprediction[0]==0):
      st.success('The person is not diabetic')
     else:
      st.warning('The person is diabetic')
      
      
if (selected == 'Heart Attack Prediction'):
    st.title('Heart Attack Prediction')
    age = st.text_input('Age')
    sex = st.text_input('Sex')
    cp = st.text_input('Chest Pain')
    trestbps = st.text_input('Resting blood pressure')
    chol = st.text_input('Serum Cholestoral in mg/dl')
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    restecg = st.text_input('Resting Electrocardiographic results')
    thalach = st.text_input('Maximum Heart Rate achieved')
    exang = st.text_input('Exercise Induced Angina')
    oldpeak = st.text_input('ST depression induced by exercise')
    slope = st.text_input('Slope of the peak exercise ST segment')
    ca = st.text_input('Major vessels colored by flourosopy')
    thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    heart_diagnosis = ''
    if st.button('Heart Attack Test Result'):
        heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if (heart_prediction[0] == 0):
          heart_diagnosis = 'Heart is Healthy'
          st.success(heart_diagnosis)
        else:
          heart_diagnosis = 'You may suffer from heart attack'
          st.warning(heart_diagnosis)
   
   
   
   