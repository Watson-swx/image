import streamlit as st
#from HK import synthesis
#from CPOE import evolution
import math

st.title('观点演化模型信息系统')

num = st.number_input('输入一个数字')
st.write('the square equals ',math.sqrt(num))

'''
st.sidebar.text('HK model parameter:')
epsilon1 = st.sidebar.slider('epsilon1', min_value=0.0,max_value=1.0)

st.sidebar.text('CPOE model parameter:')
epsilon2 = st.sidebar.slider('epsilon2', min_value=0.0,max_value=1.0)
lambd = st.sidebar.slider('lambda', min_value=0.0,max_value=1.0)
theta = st.sidebar.slider('theta', min_value=0.0,max_value=1.0)

if st.button('Run opinion evolution model'):
    col1,col2 = st.columns(2)

    # HK model
    with col1:
        filepath = synthesis(epsilon1)
        st.image(filepath,caption='HK model')

    # CPOE model
    with col2:
        filepath = evolution(epsilon2,lambd,theta)
        st.image(filepath,caption='CPOE model')
'''