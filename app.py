# -*- coding:utf-8 -*-

import streamlit as st
import numpy as np
from eda_app import run_eda_app
from ml_app import run_ml_app

def main():

    st.markdown("# Deploy Strealit")
    st.markdown("## using iris data")
    menu = ['Home', 'EDA', 'ML', 'About']
    choice = st.sidebar.selectbox("menu", menu)
    if choice == "Home":
        st.subheader("Home")
    elif choice == "EDA":
        # st.subheader("EDA")
        run_eda_app()
    elif choice == "ML":
        run_ml_app()
    elif choice == "About":
        st.subheader("About")
    else: 
        pass

if __name__ == "__main__":
    main()