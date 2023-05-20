import datetime as dt
import re
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from aip import AipNlp
import time
import altair as alt

df=pd.DataFrame(np.random.randn(500,2)/[50,50]+[37.76,-122.4],
columns=['lat','lon'])
st.map(df)

st.graphviz_chart('''
digraph{
Big_shark->Tuna
Tuna->Mackerel
Mackerel->Small_fishes
Small_fishes->Shrimp
}
''')

df=pd.DataFrame(
np.random.randn(500,3),
columns=['x','y','z'])

c=alt.Chart(df).mark_circle().encode(x='x',y='y',size='z',color='z',tooltip=['x','y','z'])
st.altair_chart(c,use_container_width=True)


#显示文本
st.write("Hello,let's learn how to build a streamlit app together")

st.title("this is the app title")
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x = 2021")
st.latex(r'''a+ar^1+ar^2+ar^3''')

st.image("ren.jpg")
st.audio("MAN.mp3")
st.video("video.mp4")

# 你的 APPID AK SK

APP_ID = '32577728'
API_KEY = '9EZWTYmZ1wiOh3BlpDh3wFri '
SECRET_KEY = 'j0At28YMvceTIUrtTdwx6VsOCgBnk7tj'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

# Set page title
st.title('Twitter Sentiment Analysis')

### SINGLE TWEET CLASSIFICATION ###
st.subheader('Single tweet classification')

# Get sentence input, preprocess it, and convert to flair.data.Sentence format
tweet_input = st.text_input('Tweet:')

if tweet_input != '':
    dic = client.sentimentClassify(tweet_input)
    s = dic['items'][0]['positive_prob']
    print(s)

    st.write('Prediction:')
    st.write('the probability of positive is ', 100*s,'%')
else:
    st.warning('you have no any enter.')


x = st.slider('Select a value')
st.write(x, 'squared is', x * x)


st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter','Mars','neptune'])
st.select_slider('Pick a mark',['Bad','Good','Excellent'])
st.slider('Pick a number',0,50)


st.number_input('Pick a number',0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

st.balloons()
st.progress(10)
with st.spinner('Wait for it...'):
    time.sleep(3)

st.success("You did it!")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("Runtime Error exception"))

st.sidebar('hello')
