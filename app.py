import streamlit as st

from app_industry import run_industry

def main():
    st.sidebar.header('데이터 애널리스트 모집공고 분석')
    column_list = ['연봉별','산업/섹터별','평가별','설립연도별','종합분석']
    
    choice = st.sidebar.radio(label= '분석 내용 선택',options = column_list)

           
    if choice == column_list[0]:
        pass
    elif choice == column_list[1]:
        run_industry()
    elif choice == column_list[2]:
        pass
    elif choice == column_list[3]:
        pass
    elif choice == column_list[4]:
        pass

    # st.sidebar.snow()

    name = st.sidebar.text_input('Job Title 키워드 검색',max_chars = 35)

    name = st.sidebar.text_input('회사명 검색',max_chars = 35)


    name = st.sidebar.text_input('산업명 영문 기입',max_chars = 35)

    name = st.sidebar.text_input('섹터명 영문 기입',max_chars = 35)


if __name__ == '__main__':
    main()