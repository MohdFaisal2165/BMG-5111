import streamlit as st
import streamlit.components.v1 as components
import tensorflow as tf
import cv2
from PIL import Image, ImageOps
import numpy as np
import pandas as pd 
import pickle
import joblib
import time

st.set_page_config(page_title = 'Cancer Dashboard', layout ="wide")

st.title('Welcome to E-Health Cancer Dashboard')
st.subheader('Get the Canadian Cancer Statistics and use AI tool to diagnose Lung Cancer*')

htmlfile1=open("TableauDash1.html", 'r', encoding = 'utf-8')
source_code2 = htmlfile1.read()
print(source_code2)
components.html(source_code2, height = 725, width = 1000)

htmlfile2=open("TableauDash2.html", 'r', encoding = 'utf-8')
source_code2 = htmlfile2.read()
print(source_code2)
components.html(source_code2, height = 725, width = 1000)

st.header('Lung Cancer Diagnosis')
st.text('This AI tool......')

x2 = st.file_uploader("Please upload the Xray Image", type = ["jpg", "jpeg", "png"], key = 1)

#This part is hard-coded only for representation purposes as the actual ML model is very heavy that cannot be integrated 
#without heavy hosting capacities of the website
#ML Model pickled filed is provided which will then be called by passing the user input image for classification 
if x2 != None:
    time.sleep(7)
    st.write("THE UPLOADED IMAGE IS SUSPECTED AS: Squamous Cell Carcinoma")
