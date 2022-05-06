"""By landry: jlandryf@gmail.com"""
import streamlit as st

import awesome_streamlit as ast
from PIL import Image

# pylint: disable=line-too-long


def write():
    st.balloons()
    image = Image.open("./src/img/tek_up_logo.jpg")
    st.image(image, use_column_width=True)
    """Used to write the page in the app.py file"""
    st.markdown('<h2><b><font color=‘#5bc0de’><i><u>BI Project : </u></i> DSEN-1-A !</font></b></h2>', unsafe_allow_html=True)
    with st.spinner("Loading About ..."):
        # ast.shared.components.title_awesome(" - About")
        st.markdown('''
            <h3 style="font-family: cursive; color: rgb(255, 127, 39)"><b>About</b></h3>
            <p style="margin-top: 10px"> 
                In this project, we are using a dataset from the <b> UNICEFT </b> website to analyse the infant death rate in the world from 2011 to 2020
            </p>
            <p>
                This project was developed using several libraries
            </p>
            Some are :
            <ul>
                <li>python ; </li>
                <li>Streamlit ; </li>
                <li>PIL ; </li>
                <li>awesome_streamlit ; </li>
                <li>pandas ; </li>
                <li>numpy; </li>
                <li>plotly; </li>
                <li>statsmodels; </li>
                <li>altair; </li>
                <li>sklearn; </li>
                <li>and more. </li>
            </ul>
            <hr style="border:1px solid black">
            <h3 style="font-family: cursive; color: rgb(255, 127, 39)"><b>Why this dataset ?</b></h3>
            <p>
                I think it's important to the how the demogaphy is growing in the world. Some NGOs need this kind of studies to better direct their aid and actions in order to touch the right target (People who really need assitance)
            </p>
            <p style="margin-bottom: 30px">
                We can therefore get the rates
            </p><hr style="border:1px solid black">
            <h3 style="font-family: cursive; color: rgb(255, 127, 39)"><b>What Next ?</b></h3>
            <div>
                <p>The next stage is to study the causes of infant death specially in the countries where this rate has grown through years. Identifying the causes may help to reduce the rate.</p>
                <p></p>
            </div>
            ''', 
            unsafe_allow_html=True
        )
