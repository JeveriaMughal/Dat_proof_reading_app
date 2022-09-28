import streamlit as st
import stapp1,stapp2,rauf_parekh
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
    "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
# Assign credentials ann path of style sheet
creds = ServiceAccountCredentials.from_json_keyfile_name("blank-test-363706-5265bab97753.json", scope)
client = gspread.authorize(creds)

PAGES = {"جویریہ مغل": stapp1,
        "دانیہ شفیق":stapp2,
        "پروفیسر ڈاکٹر رؤف پاریکھ":rauf_parekh}
st.sidebar.title("NLP-L \n Proof reading app")
selection = st.sidebar.selectbox("نام",list (PAGES.keys()))
if selection == "جویریہ مغل":
    st.sidebar.image("images/jeveria.jpeg")
    sheet = client.open("modified_data").get_worksheet(0)
    df = pd.DataFrame(sheet.get_all_records(),index=None)
    csv=df.to_csv().encode('utf-8')
    st.sidebar.download_button(
            "Press to Download",
            csv,
            "file.csv",
            "text/csv",
            key='download-csv-jeveria')
    data=df
    if len(df.index)>1:
        chart_data=pd.DataFrame(columns=['index','date'])
        df1 = data['date'].value_counts()
        st.sidebar.bar_chart(df1)

if selection == "دانیہ شفیق":
    st.sidebar.image("images/dania.JPG")   
    sheet = client.open("modified_data").get_worksheet(1)
    df = pd.DataFrame(sheet.get_all_records(),index=None)
    csv=df.to_csv().encode('utf-8')
    st.sidebar.download_button(
            "Press to Download",
            csv,
            "file.csv",
            "text/csv",
            key='download-csv-dania')
    data=df
    if len(df.index)>1:
        chart_data=pd.DataFrame(columns=['index','date'])
        df1 = data['date'].value_counts()
        st.sidebar.bar_chart(df1)

if selection == "پروفیسر ڈاکٹر رؤف پاریکھ":
    st.sidebar.image("images/DG Dr Rauf Parekh.png")
    sheet = client.open("modified_data").get_worksheet(2)
    df = pd.DataFrame(sheet.get_all_records(),index=None)
    csv=df.to_csv().encode('utf-8')
    st.sidebar.download_button(
            "Press to Download",
            csv,
            "file.csv",
            "text/csv",
            key='download-csv-parekh')
    data=df
    if len(df.index)>1:
        chart_data=pd.DataFrame(columns=['index','date'])
        df1 = data['date'].value_counts()
        st.sidebar.bar_chart(df1)


page= PAGES[selection]
page.app()
