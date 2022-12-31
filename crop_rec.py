# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 18:41:22 2022

@author: ADMIN
"""

import pandas as pd
import streamlit as st
import joblib
import warnings

warnings.filterwarnings('ignore')

def main():
    html_temp="""
    <div style = "background-color:lightblue;padding:11px">
    <h2 style = "color:black;text-align:center;">Crop Recommendation System</h2>
    </div>
    """
    model = joblib.load('crop_prediction')
    
    st.markdown(html_temp,unsafe_allow_html=True)
    p1 = st.number_input("Amount of Nitrogen in %",)
    p2 = st.number_input("Amount of Phosphorous in %")
    p3 = st.number_input("Amount of Pottasium in %")
    p4 = st.number_input("Enter the Temperature of farming area in °C",step=1)
    p5 = st.number_input("Enter the Humidity in %")
    p6 = st.number_input("Enter the PH of soil")
    p7 = st.number_input("Rainfall in mm")
    
    data_new = pd.DataFrame({
    'Nitrogen':p1,
    'Phosphorous':p2,
    'Pottasium':p3,
    'Temperature':p4,
    'Humidity':p5,
    'PH':p6,
    'Rainfall':p7,
    },index=[0])
    
    if st.button('Predict'):
        pred = model.predict(data_new)
        if pred == 'apple':
            st.balloons()
            st.success("Apple(સફરજન)")
        elif pred=='banana':
            st.balloons()
            st.success("Banana(કેળું)")
        elif pred=='blackgram':
            st.balloons()
            st.success("Blackgram(અડદની દાળ)")
        elif pred=='chickpea':
            st.balloons()
            st.success("Chickpea(ચણા)")
        elif pred=='coconut':
            st.balloons()
            st.success("Coconut(નાળિયેર)")
        elif pred=='coffee':
            st.balloons()
            st.success("Coffee(કોફી)")
        elif pred=='cotton':
            st.balloons()
            st.success("Cotton(કપાસ)")
        elif pred=='grapes':
            st.balloons()
            st.success("Grapes(દ્રાક્ષ)")
        elif pred=='jute':
            st.balloons()
            st.success("Jute(શણ)")
        elif pred=='kidneybeans':
            st.balloons()
            st.success("Kidneybeans(રાજમા)")
        elif pred=='lentil':
            st.balloons()
            st.success("Lentil(મસૂર)")
        elif pred=='maize':
            st.balloons()
            st.success("Maize(મકાઈ)")
        elif pred=='mango':
            st.balloons()
            st.success("Mango(કેરી)")
        elif pred=='mothbeans':
            st.balloons()
            st.success("Mothbeans(શલભ કઠોળ)")
        elif pred=='mungbean':
            st.balloons()
            st.success("Mungbean(મગ)")
        elif pred=='muskmelon':
            st.balloons()
            st.success("Muskmelon(શકરટેટી)")
        elif pred=='orange':
            st.balloons()
            st.success("Orange(નારંગી)")
        elif pred=='papaya':
            st.balloons()
            st.success("Papaya(પપૈયા)")
        elif pred=='pigeonpeas':
            st.balloons()
            st.success("Pigeonpeas(તુવેર)")
        elif pred=='pomegranate':
            st.balloons()
            st.success("Pomegranate(દાડમ)")
        elif pred=='rice':
            st.balloons()
            st.success("Rice(ચોખા)")
        else:
            st.balloons()
            st.success("Watermelon(તરબૂચ)")
    
    
    
    
if __name__ == '__main__':
    main()