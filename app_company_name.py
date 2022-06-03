import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('data/df_data_anaylist2.csv', index_col=0)

def search_company(name):
    result = df.loc[df['Company Name'].str.lower().str.contains(name.lower()), ]
    st.dataframe(result)
    st.text('검색된 데이터는 {}개입니다.'.format(result.shape[0]))

def run_company_type ():
    
    col1,col2 = st.columns([2,3])

    ownership = df['Type of ownership'].value_counts()
    ownership = ownership.to_frame()
    ownership.columns = ['counts']
 
    with st.expander('회사 유형 테이블'):
        st.dataframe(ownership)
    
    chart_type = col1.radio('회사 유형 차트 확인',['원형 그래프','막대 그래프','버블 그래프'])
    if chart_type == '원형 그래프':
        fig1 = px.pie(ownership,names = ownership.index, values='counts')
        st.plotly_chart(fig1)

    elif chart_type == '막대 그래프':
        fig2 = px.bar(ownership)
        st.plotly_chart(fig2)

    elif chart_type == '버블 그래프':
        fig3 = px.scatter(ownership)
        fig3.show()


