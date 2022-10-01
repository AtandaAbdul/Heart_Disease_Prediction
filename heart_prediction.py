import streamlit as st
import pandas as pd
import numpy as np
import pickle  #to load a saved model
import base64  #to open .gif files in streamlit app


@st.cache(suppress_st_warning=True)
def get_fvalue(val):
    feature_dict = {"No":1,"Yes":2}
    for key,value in feature_dict.items():
        if val == key:
            return value

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value

app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction']) #two pages

if app_mode=='Home':
    st.title('HEART DISEASE PREDICTION :')  
    #st.image('loan_image.jpg')
    st.markdown('Dataset :')
    data=pd.read_csv('heart.csv')
    st.write(data.head())
    st.markdown('Age  and Heart Disease ')
    st.bar_chart(data[['Age','HeartDisease']].head(20))
    #st.bar_chart(data[['ApplicantIncome']].head(20))

elif app_mode == 'Prediction':
    #st.image('slider-short-3.jpg')

    st.subheader('Sir/Mr , YOU need to fill all necessary to check the Heart Disease Prediction')
    st.sidebar.header("Informations about the Patient :")
    gender_dict = {"Male":1,"Female":0}
    feature_dict = {"No":0,"Yes":1}
    ChestPain ={'Atypical Angina':1,'NonAnginal Pain':2,'Asymptomatic':0,'Typical Angina':4}
    ST_Slop={'Flat':1,'Up':2,'Down':3}

    Age=st.sidebar.slider('Age',18,100,0,)
    Sex=st.sidebar.radio('Gender',tuple(gender_dict.keys()))
    ChestPainType=st.sidebar.radio('Chest Pain Type',tuple(ChestPain.keys()))
    RestingBP =st.sidebar.slider('Resting BP',18,250,0,)
    Cholesterol = st.sidebar.slider('Cholesterol',18,500,0,)
    FastingBS = st.sidebar.radio('Fasting BLood Sugar(> or < 120mg/dL)',tuple(feature_dict.keys()))
    MaxHR = st.sidebar.slider('Max HR',18,200,0,)
    ExerciseAngina = st.sidebar.radio('Excercised Induced Angina',tuple(feature_dict.keys()))
    Oldpeak=st.sidebar.slider('Old Peak',0,2,0,)
    ST_Slope=st.sidebar.radio('ST Slope',tuple(ST_Slop.keys()))
    
    

    data1={
    'Age' : Age,
    'Sex':Sex,
    'ChestPainType':ChestPainType,
    'RestingBP':RestingBP,
    'Cholesterol':Cholesterol,
    'FastingBS':FastingBS,
    'MaxHR':MaxHR,
    'ExerciseAngina':ExerciseAngina,
    'Oldpeak':Oldpeak,
    'ST_Slope':ST_Slope,
    
    }

    feature_list=[Age,get_value(Sex,gender_dict),get_value(ChestPainType,ChestPain),RestingBP,Cholesterol,get_fvalue(FastingBS),MaxHR,get_fvalue(ExerciseAngina),Oldpeak,get_value(ST_Slope,ST_Slop)]


    single_sample = np.array(feature_list).reshape(1,-1)



if st.button("Predict"):
        #file_ = open("6m-rain.gif", "rb")
        #contents = file_.read()
        #data_url = base64.b64encode(contents).decode("utf-8")
        #file_.close()

        # file = open("green-cola-no.gif", "rb")
        # contents = file.read()
        # data_url_no = base64.b64encode(contents).decode("utf-8")
        # file.close()


        loaded_model = pickle.load(open('Random_Forest.sav', 'rb'))
        prediction = loaded_model.predict(single_sample)
        if prediction[0] == 0 :
            st.success(
    'According to our Calculations, the patient is not likely to have a Heart Disease'
    )
           # st.markdown(
    #f'<img src="data:image/gif;base64,{data_url_no}" alt="cat gif">',
    #unsafe_allow_html=True,)
        elif prediction[0] == 1 :
            st.error(
    'According to our Calculations, the patient is likely to have a Heart Disease'
    )
      #      st.markdown(
    #f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    #unsafe_allow_html=True,
    #)


