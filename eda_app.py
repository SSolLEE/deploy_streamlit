# -*- coding:utf-8 -*-

import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

def run_eda_app():

    st.subheader("EDA Page")
    st.subheader("EDA-ing")

    # 메뉴 지정
    submenu = st.sidebar.selectbox("submenu", ['통계', '시각화', '분석'])

    iris_df = pd.read_csv("data\iris.csv")
    st.dataframe(iris_df)

    if submenu == "submenu":
        st.subheader("submenu")
    elif submenu == "통계":
        st.subheader("통계")
    elif submenu == "시각화":
        st.subheader("시각화")
        fig1= px.scatter(iris_df,
                         x = 'sepal_width',
                         y = 'sepal_length',
                         color = 'species',
                         size = 'petal_width',
                         hover_data= ['petal_length'],
                         title= "Scatter Plot")
        st.plotly_chart(fig1)
    elif submenu == "분석":
        st.subheader("분석")
    else: 
        pass


