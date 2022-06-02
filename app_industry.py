import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

def run_industry():
    st.subheader("데이터 애널리스트 모집 산업 Top")
    st.text('')

    df = pd.read_csv('data/df_data_anaylist2.csv', index_col=0)
 #   st.dataframe(df)

    col1, col2 = st.columns([1, 3])
     
    top_list = ['Top10','Top30','Top50']
    top = col1.radio('Top 보기',top_list)

    industry = df['Industry'].value_counts()
    industry = industry.to_frame()
    industry.columns = ['counts']

    if top == top_list[0]:
        top = 10 
    elif top == top_list[1]:
        top = 20
    elif top == top_list[2]:
        top = 30  

    col2.text('\n\n')

    with col2.expander('데이터 애널리스트 모집 공고 산업별 Top{}'.format(top)):
        st.dataframe(industry.head(top))
    # col2.text('데이터 애널리스트 모집 공고 산업별 Top{}'.format(top))
    # col2.dataframe(industry.head(top))





    # with col2.expander('Top50'):
    #     st.dataframe(industry)

