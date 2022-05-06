# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 22:12:03 2022

@author: PC-2022
"""

import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import numpy as np

import awesome_streamlit as ast

#st.title('Sentiment Analysis Application')

#-----------------------------------
import src.templates.about
import src.templates.home
import src.templates.gallery
from PIL import Image
import src.templates.use_dataset
import src.templates.ai_part

ast.core.services.other.set_logging_format()


#------------------------------------------

st.set_option('deprecation.showPyplotGlobalUse', False)


PAGES = {
    "Home": src.templates.home,
    "BI Part": src.templates.use_dataset,
    "AI Part": src.templates.ai_part,
    #"gallery": src.templates.gallery,
    "About": src.templates.about,
}

st.sidebar.markdown('<h4 style="text-align: center; font-family: cursive; color: rgb(255, 127, 39)"><b>PROJET BI, 2021-2022</b></h4>', unsafe_allow_html=True)
image = Image.open("./src/img/tek_up_logo.jpg")
st.sidebar.image(image, use_column_width=True)
st.sidebar.info(
    """
	        Infant Death Analysis Application
	"""
)


selection = st.sidebar.radio("Navigate to", list(PAGES.keys()))

page = PAGES[selection]

with st.spinner(f"Loading {selection} ..."):
    ast.shared.components.write_page(page)
    
   
