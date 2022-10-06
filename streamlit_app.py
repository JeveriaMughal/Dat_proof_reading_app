import streamlit as st
import fakhra,bugti,RP,rashid_hameed_homepage,homepage,tanveer_fatima_homepage
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
st.set_page_config(layout="wide")
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
    "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
# Assign credentials ann path of style sheet
creds = ServiceAccountCredentials.from_json_keyfile_name("blank-test-363706-5265bab97753.json", scope)
client = gspread.authorize(creds)

PAGES = {"":homepage,
        "پروفیسر ڈاکٹر رؤف پاریکھ":RP,
        "ڈاکٹر راشد حمید":rashid_hameed_homepage,
        "محبوب بگٹی":bugti,
        "فاخرہ منور": fakhra,
        "تنویر فاطمہ":tanveer_fatima_homepage}
st.sidebar.title("NLP-LAB \n Proofreading Application")
selection = st.sidebar.selectbox("نام",list (PAGES.keys()))
if selection == "فاخرہ منور":
    st.sidebar.image("images/fakhra_TN.png")
    sheet = client.open("modified_data").get_worksheet(0)
    df = pd.DataFrame(sheet.get_all_records(),index=None)
    csv=df.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button(
            "Download reviewed data",
            csv,
            "file.csv",
            "text/csv",
            key='download-csv-fakhra')
    data=df
    if len(df.index)>1:
        chart_data=pd.DataFrame(columns=['index','date'])
        df1 = data['date'].value_counts()
        st.sidebar.bar_chart(df1)

if selection == "محبوب بگٹی":
    st.sidebar.image("images/m_bugti_TN.png")   
    sheet = client.open("modified_data").get_worksheet(1)
    df = pd.DataFrame(sheet.get_all_records(),index=None)
    csv=df.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button(
            "Download reviewed data",
            csv,
            "file.csv",
            "text/csv",
            key='download-csv-bugti')
    data=df
    if len(df.index)>1:
        chart_data=pd.DataFrame(columns=['index','date'])
        df1 = data['date'].value_counts()
        st.sidebar.bar_chart(df1)

if selection == "پروفیسر ڈاکٹر رؤف پاریکھ":
    st.sidebar.image("images/DG Dr Rauf Parekh.png")
    sheet = client.open("modified_data").get_worksheet(2)
    sheet2 = client.open("modified_data").get_worksheet(3)
    df = pd.DataFrame(sheet.get_all_records(),index=None)
    df2 = pd.DataFrame(sheet2.get_all_records(),index=None)
    df_all=pd.concat([df,df2],ignore_index = True, axis = 0)
    csv=df.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button(
            "Download Reviewed Corpus",
            csv,
            "reviwed_corpus.csv",
            "text/csv",
            key='download-csv-parekh')
    csv2=df2.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button(
            "Download Reviewed Glossary",
            csv2,
            "reviwed_glossary.csv",
            "text/csv",
            key='download-csv2-parekh')
    data=df_all
    if len(df_all.index)>1:
        chart_data=pd.DataFrame(columns=['index','date'])
        df1 = data['date'].value_counts()
        st.sidebar.bar_chart(df1)

if selection == "ڈاکٹر راشد حمید":
    st.sidebar.image("images/dr_rashid_TN.png")   
    sheet = client.open("modified_data").get_worksheet(4)
    df = pd.DataFrame(sheet.get_all_records(),index=None)
    csv=df.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button(
            "Download reviewed data",
            csv,
            "file.csv",
            "text/csv",
            key='download-csv-bugti')
    data=df
    if len(df.index)>1:
        chart_data=pd.DataFrame(columns=['index','date'])
        df1 = data['date'].value_counts()
        st.sidebar.bar_chart(df1)
if selection =="تنویر فاطمہ":
    st.sidebar.image("images/TF_TN.png")
    sheet = client.open("modified_data").get_worksheet(5)
    df = pd.DataFrame(sheet.get_all_records(),index=None)
    csv=df.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button(
            "Download reviewed data",
            csv,
            "file.csv",
            "text/csv",
            key='download-csv-TF')
    data=df
    if len(df.index)>1:
        chart_data=pd.DataFrame(columns=['index','date'])
        df1 = data['date'].value_counts()
        st.sidebar.bar_chart(df1)

page= PAGES[selection]
page.app()
