import streamlit as st
import stapp1,stapp2,rauf_parekh
import pandas as pd
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")
PAGES = {"جویریہ مغل": stapp1,
        "دانیہ شفیق":stapp2,
        "پروفیسر ڈاکٹر رؤف پاریکھ":rauf_parekh}
st.sidebar.title("NLP-L \n Proof reading app")
selection = st.sidebar.selectbox("نام",list (PAGES.keys()))
if selection == "جویریہ مغل":
    st.sidebar.image("images/jeveria.jpeg")
    with open("modified_data/Jeveria.csv", "r") as file:
        st.sidebar.download_button(
        label="Download data prepared",
        data=file,
        file_name='jeveria.csv',
        mime='text/csv',)
    data=pd.read_csv("modified_data/Jeveria.csv",header=0)
    chart_data=pd.DataFrame(columns=['index','date'])
    df1 = data['date'].value_counts()
    st.sidebar.bar_chart(df1)

if selection == "دانیہ شفیق":
    st.sidebar.image("images/dania.JPG")    
    with open("modified_data/dania.csv", "r") as file:
        st.sidebar.download_button(
        label="Download data prepared",
        data=file,
        file_name='dania.csv',
        mime='text/csv',)
    data=pd.read_csv("modified_data/dania.csv",header=0)
    chart_data=pd.DataFrame(columns=['index','date'])
    df1 = data['date'].value_counts()
    st.sidebar.bar_chart(df1)

if selection == "پروفیسر ڈاکٹر رؤف پاریکھ":
    st.sidebar.image("images/DG Dr Rauf Parekh.png")
    with open("modified_data/dr_parekh.csv", "r") as file:
        st.sidebar.download_button(
        label="Download data prepared",
        data=file,
        file_name='dr_parekh.csv',
        mime='text/csv',)
    data=pd.read_csv("modified_data/dr_parekh.csv",header=0)
    chart_data=pd.DataFrame(columns=['index','date'])
    df1 = data['date'].value_counts()
    st.sidebar.bar_chart(df1)


page= PAGES[selection]
page.app()
