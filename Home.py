import pandas as pd

from PIL import Image

import streamlit as st


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#  show logo image
image = Image.open('logo.jpg')

st.image(
    image, 
    caption='Image', 
    width=400, 
    channels='RGB')

st.divider()

#clothing options
clothing_options = ['Shirts', 'Hats']
st.selectbox('Select Clothing', clothing_options)

