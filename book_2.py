# -*- coding: utf-8 -*-
"""book-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c7Z3fAsMxaZCLFqSJORRbchp4LSGmn76
"""





import streamlit as st 
import joblib 
import numpy as np

from PIL import Image




reload_model = joblib.load('book_model_1')

book_name_1=st.text_input('book_name')


result =""

if st.button("Predict"): 
    prediction=reload_model.predict([[book_name]])
    st.text('suggested book is ')
    st.text(prediction)

