import pandas as pd
import streamlit as st

df = pd.read_csv('data/df_data_anaylist2.csv', index_col=0)

def search_jobtitle(name):
    result = df.loc[df['Job Title'].str.lower().str.contains(name.lower()), ]
    result.sort_values('Rating')
    st.dataframe(result)
    st.text('검색된 데이터는 {}개입니다.'.format(result.shape[0]))

def search_company(name):
    result = df.loc[df['Company Name'].str.lower().str.contains(name.lower()), ]
    st.dataframe(result)
    st.text('검색된 데이터는 {}개입니다.'.format(result.shape[0]))

def search_industry(name):
    result = df.loc[df['Industry'].str.lower().str.contains(name.lower()), ]
    st.dataframe(result)
    st.text('검색된 데이터는 {}개입니다.'.format(result.shape[0]))

def search_sector(name):
    result = df.loc[df['Sector'].str.lower().str.contains(name.lower()), ]
    st.dataframe(result)
    st.text('검색된 데이터는 {}개입니다.'.format(result.shape[0]))