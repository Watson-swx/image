import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_excel("Cities2015.xlsx")
df = df.dropna()

st.map(df)