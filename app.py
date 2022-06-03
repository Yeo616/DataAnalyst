import streamlit as st
import pandas as pd
from app_founded import run_founded

from app_industry import run_industry
from app_rating import run_rating
from app_salary import run_salary
from app_search import search_sector
from app_company_name import run_company_type, search_company
from app_serach_job import search_jobtitle
from app_search_industry import search_industry

def main():
    # 가로로 길게 보이도록 어케함?


    # st.set_page_config(layout="wide")
    st.sidebar.header('데이터 애널리스트 모집공고 분석')
    column_list = ['회사/회사유형별','급여별','산업/섹터별','평가별','설립연도별','종합분석','검색']
    
    choice = st.sidebar.radio(label= '분석 내용 선택',options = column_list)
    

           
    if choice == column_list[0]:
        name2 = st.text_input('회사명 검색',max_chars = 35)
        if len(name2)>0:
            search_company(name2)
        run_company_type()
        
    elif choice == column_list[1]:
        run_salary()
   
    elif choice == column_list[2]:
        run_industry()

    elif choice == column_list[3]:
        run_rating()

    elif choice == column_list[4]:
        run_founded()

    elif choice == column_list[5]:
        pass
    elif choice == column_list[6]:
        name = st.text_input('Job Title 키워드 검색',max_chars = 35)
        if len(name)>0:
            search_jobtitle(name)

        name2 = st.text_input('회사명 검색',max_chars = 35)
        if len(name2)>0:
            search_company(name2)

        name3 = st.text_input('산업명 영문 기입',max_chars = 35)
        if len(name3)>0:
            search_industry(name3)

        name4 = st.text_input('섹터명 영문 기입',max_chars = 35)
        if len(name4)>0:
            search_sector(name4)

    # st.sidebar.snow()


if __name__ == '__main__':
    main()