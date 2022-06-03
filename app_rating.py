import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import matplotlib.pyplot as plt
import plotly.graph_objects as go


df = pd.read_csv('data/df_data_anaylist2.csv', index_col=0)
df = df.astype({'Founded':'int'})

df['Rating'] = round(df['Rating'],1)
# pd.options.display.float_format ='{:1f}'.format

df = df[['Rating','Job Title', 'Job Description','Company Name','Location','Headquarters','Founded','Type of ownership','Industry','Sector','Revenue','Competitors', 'Easy Apply', 'Salary_Estimate_From_(K)','Salary_Estimate_To_(K)','Size_From(employees)','Size_To(employees)']]


def run_rating():
    
    col1,col2 = st.columns([1,3])

    rating = st.slider('별점 선택', 1.0,5.0,1.0,0.1 )

    df_rating = df.loc[df['Rating'] == rating, 
        ['Rating','Job Title','Company Name','Industry',
        'Sector','Revenue','Salary_Estimate_From_(K)','Salary_Estimate_To_(K)',
        'Size_From(employees)','Size_To(employees)']]
    st.dataframe(df_rating)
    
    st.write(' ')
    st.write('해당 별점 범위에 해당하는 연봉 범위 산점그래프')
    fig = px.scatter(df_rating, 'Salary_Estimate_From_(K)', 
        'Salary_Estimate_To_(K)')
    plt.xlabel('Sa')

    st.plotly_chart(fig)

# checkbox를 이용해서, groupby에 누굴 포함할지 여부 결정.