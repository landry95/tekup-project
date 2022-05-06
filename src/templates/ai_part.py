"""This page is for searching and viewing the list of awesome resources"""
"""By landry: jlandryf@gmail.com"""
import logging

import streamlit as st
import pandas as pd

import awesome_streamlit as ast
from awesome_streamlit.core.services import resources
import matplotlib.pyplot as plt
import re
from random import random
from PIL import Image
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import streamlit as st
import plotly.figure_factory as ff
import numpy as np
import plotly.express as px
from statsmodels.tsa.exponential_smoothing.ets import ETSModel
import altair as alt
from sklearn.metrics import accuracy_score

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)



def sentiment_analysis(text):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(text)
    if sentiment_dict['compound'] >= 0.05 :
        return 1
    elif sentiment_dict['compound'] <= - 0.05 :
        return -1
    else :
        return 0
    





def get_df(file):
    # get extension and read file
    extension = file.name.split('.')[1]
    if extension.upper() == 'CSV':
        df = pd.read_csv(file)
    elif extension.upper() == 'XLSX':
        df = pd.read_excel(file, engine='openpyxl')
    elif extension.upper() == 'PICKLE':
        df = pd.read_pickle(file)
    return df





def write():

    st.markdown('<h2 style="text-align: center; font-family: cursive; color: rgb(41, 43, 44)"><b>FORECASTING</b></h3>', unsafe_allow_html=True)
    st.sidebar.markdown('<h2 style="margin-top: 20px; font-family: cursive; color: rgb(255, 127, 39)"><b>********</b></h3>', unsafe_allow_html=True)

    st.info(
            """Your will select a dataset, and let the **algorithm Analyse them and display the result!**"""
        )
    st.markdown('''<p style="color: #d9534f">
                            This data is linked to this code: <b>data</b> folder  <b></b> 
                            </p>
                            <p><b>Please Select the data and take a cup of coffee.</b></p>
                        ''', unsafe_allow_html=True)
    
    
    file = st.file_uploader("Upload file", type=['csv', 'xlsx'])
    if not file:
        st.write("Upload a .csv or .xlsx file to get started")
        return
    
    
    
    dataset = get_df(file)
    #st.write(dataset)
    data = dataset[["Geographic area", "Indicator", "TIME_PERIOD", "OBS_VALUE"]]
    
    col1, col2 = st.columns(2)
    option = col1.selectbox(
     'Select the country',
     set(dataset["Geographic area"]))
    
    indicator = col2.selectbox(
     'Select an indicator',
     set(dataset["Indicator"]))
    
    data = data.loc[dataset['Geographic area'] == option]
    data = data.astype({"TIME_PERIOD": str}, errors='raise')
    infant = data[data['Indicator'] == indicator]
    """child = data[data['Indicator'] == "Child deaths (aged 1-4 years)"]
    neo_natal = data[data['Indicator'] == "Neonatal deaths"]
    aged = data[data['Indicator'] == "Deaths aged 15 to 24"]"""
    
    st.write(infant)
    plt.rcParams["figure.figsize"] = (12, 8)
    
    infant_serie = pd.Series(list(infant["OBS_VALUE"]), index=pd.date_range("2011", "2020", freq="AS"))
    st.line_chart(infant_serie)
    st.write(infant_serie)
    


########################"Holt’ method
    st.write("")
    st.markdown('<h4 style="text-align: center; font-family: cursive; color: rgb(41, 43, 44)"><b>Holt’ Model</b></h4>', unsafe_allow_html=True)

    holt_model = ETSModel(
        infant_serie,
        error="add",
        trend="add",
        damped_trend=True,
        seasonal_periods=4,
    )
    fit_holt_model = holt_model.fit()
    st.line_chart(fit_holt_model.fittedvalues)
    st.write(fit_holt_model.summary())
    st.write(fit_holt_model.fittedvalues)
    
    pred = fit_holt_model.get_prediction(start="2021-01-01T00:00:00", end="2025-01-01T00:00:00")
    st.write(pred.summary_frame())
    

########################"Simple ETS’  method
    st.write("")
    st.markdown('<h4 style="text-align: center; font-family: cursive; color: rgb(41, 43, 44)"><b>Simple ETS</b></h4>', unsafe_allow_html=True)
    
    
    model_simple = ETSModel(infant_serie)
    fit_simple = model_simple.fit()
    st.line_chart(fit_simple.fittedvalues)
    st.write(fit_simple.summary())
    
    pred_simple = fit_simple.get_prediction(start="2021-01-01T00:00:00", end="2025-01-01T00:00:00")
    st.write(pred_simple.summary_frame())
    
    
    
########################"heuristic’  method
    st.write("")
    st.markdown('<h4 style="text-align: center; font-family: cursive; color: rgb(41, 43, 44)"><b>Heuristic Model</b></h4>', unsafe_allow_html=True)

    model_heuristic = ETSModel(infant_serie, initialization_method="heuristic")
    fit_heuristic = model_heuristic.fit()
    st.line_chart(fit_heuristic.fittedvalues)
    st.write(fit_heuristic.summary())
    
    pred_heuristic = fit_heuristic.get_prediction(start="2021-01-01T00:00:00", end="2025-01-01T00:00:00")
    st.write(pred_heuristic.summary_frame())
    
    
########################"Holt-Winters’ seasonal method
    st.write("")
    st.markdown('<h4 style="text-align: center; font-family: cursive; color: rgb(41, 43, 44)"><b>Winters’ Model</b></h4>', unsafe_allow_html=True)

    model_winter = ETSModel(
        infant_serie,
        error="add",
        trend="add",
        seasonal="add",
        damped_trend=True,
        seasonal_periods=4,
    )
    fit_model_winter = model_winter.fit()
    st.line_chart(fit_model_winter.fittedvalues)
    st.write(fit_model_winter.summary())
    
    pred_winter = fit_model_winter.get_prediction(start="2021-01-01T00:00:00", end="2025-01-01T00:00:00")
    st.write(pred_winter.summary_frame())
    
    

    return



    df_i = get_df(file)
    text = df_i['text']
    result = list()
    i=0
    
    
    for t in text:
        i = i+1
        result.append(sentiment_analysis(t))
        

    
    data = {i:result.count(i) for i in result}
    nb = len(result)
    st.write("")
    st.write("")
    st.write("")
    st.write("NUMBER OF RECORDS")
    st.write(nb)
    st.write("")
    st.write("")
    st.write("")
    st.write("STATISTICS")
    data1 = {'Sentiment': ['Neutral', 'Negative', 'Positive'], 'Reccurence': [data[0], data[-1], data[1]], 'Rate': [str(100*data[0]/nb) + "%", str(100*data[-1]/nb)+"%", str(100*data[1]/nb)+"%"]}  
    df = pd.DataFrame(data1)
    st.write(df)
    
    
    st.write("## Some Positive content")
    count = 0
    #st.write("# ", df_i.head())
    pos = {'tweet_id': [], 'airline':[],'text':[], 'tweet_created':[], 'tweet_location':[], 'airline_sentiment': [], 'negativereason': [], 'negativereason_confidence': [], 'airline':[]}
    positive = list()
    i = 0
    for j in result:
        if j == 1:
            positive.append(text[i])
            count = count+1
        i=i+1
        if count==10: break
    
    
    # Calling DataFrame constructor on list  
    #positive = pd.DataFrame(pos)  
    st.write(positive)  
    
    
    st.write("")
    st.write("=============================================================================================")
    st.write("## Some Negative content")
    count = 0
    i = 0
    negative = list()
    for j in result:
        if j == -1:
            negative.append(text[i])
            count = count+1
        i = i+1
        if count==10: break
    st.write(negative)
    
    
    st.write("")
    st.write("=============================================================================================")
    st.write("## Some Neutral content")
    count = 0
    i = 0
    neutral = list()
    for j in result:
        if j == 0:
            neutral.append(text[i])
            count = count+1
        i = i+1
        if count==10: break
    st.write(neutral)





if __name__ == "__main__":
    write()