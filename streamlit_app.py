import streamlit as st
import fakhra_homepage,m_bugti_homepage,RP,rashid_hameed_homepage,homepage,tanveer_fatima_homepage,nisar_MK_homepage,jawad_homepage
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
        "محبوب بگٹی":m_bugti_homepage,
        "فاخرہ منور": fakhra_homepage,
        "تنویر فاطمہ":tanveer_fatima_homepage,
        "نثار ماماخیل":nisar_MK_homepage,
        "جواد الحق":jawad_homepage}
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
    sheet = client.open("Data_review_phase2").get_worksheet(0)
    sheet2 = client.open("Data_review_phase2").get_worksheet(1)
    sheet3 = client.open("Data_review_phase2").get_worksheet(3)
    sheet4 = client.open("Data_review_phase2").get_worksheet(6)

    df = pd.DataFrame(sheet.get_all_records(),index=None)
    df2 = pd.DataFrame(sheet2.get_all_records(),index=None)
    df3 = pd.DataFrame(sheet3.get_all_records(),index=None)
    df4 = pd.DataFrame(sheet4.get_all_records(),index=None)
    df_all=pd.concat([df,df2,df3,df4],ignore_index = True, axis = 0)
    data=df_all
    if len(df_all.index)>1:
        chart_data=pd.DataFrame(columns=['index','date'])
        df1 = data['date'].value_counts()
        st.sidebar.bar_chart(df1)
    csv=df.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button(
            "Download Reviewed Corpus_BUGTI",
            csv,
            "reviwed_corpus.csv",
            "text/csv",
            key='download-csv-parekh0')
    csv2=df2.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button(
            "Download Reviewed Corpus_MUNAWAR",
            csv2,
            "reviwed_corpus.csv",
            "text/csv",
            key='download-csv-parekh1')
    csv4=df4.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button(
            "Download Reviewed Corpus_Parekh",
            csv4,
            "reviwed_glossary.csv",
            "text/csv",
            key='download-csv2-parekh2')
    csv3=df3.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button(
            "Download Reviewed Glossary",
            csv3,
            "reviwed_glossary.csv",
            "text/csv",
            key='download-csv2-parekh3')


if selection == "ڈاکٹر راشد حمید":
    st.sidebar.image("images/dr_rashid_TN.png")   
    sheet = client.open("Data_review_phase2").get_worksheet(4)
    sheet2 = client.open("Data_review_phase2").get_worksheet(5)
    sheet3 = client.open("Data_review_phase2").get_worksheet(2)

    df = pd.DataFrame(sheet.get_all_records(),index=None)
    df2 = pd.DataFrame(sheet2.get_all_records(),index=None)
    df3 = pd.DataFrame(sheet3.get_all_records(),index=None)
    df_all=pd.concat([df,df2,df3],ignore_index = True, axis = 0)
    data=df_all
    if len(df_all.index)>1:
        chart_data=pd.DataFrame(columns=['index','date'])
        df1 = data['date'].value_counts()
        st.sidebar.bar_chart(df1)
    csv=df.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button(
            "Download Reviewed GLOSSARY",
            csv,
            "reviwed_GLOSSARY.csv",
            "text/csv",
            key='download-csv-hameed0')
    csv2=df2.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button(
            "Download Reviewed Corpus_FATIMA",
            csv2,
            "reviwed_corpus_FATIMA.csv",
            "text/csv",
            key='download-csv-hameed1')
    csv3=df3.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button(
            "Download Reviewed corpus_NISAR",
            csv3,
            "reviwed_corpus_NISAR.csv",
            "text/csv",
            key='download-csv2-hameed3')
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

if selection == "نثار ماماخیل":
    st.sidebar.image("images/NMK.png")
    sheet = client.open("modified_data").get_worksheet(2)
    df = pd.DataFrame(sheet.get_all_records(),index=None)
    csv=df.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button(
            "Download reviewed data",
            csv,
            "file.csv",
            "text/csv",
            key='download-csv-NMK')
    data=df
    if len(df.index)>1:
        chart_data=pd.DataFrame(columns=['index','date'])
        df1 = data['date'].value_counts()
        st.sidebar.bar_chart(df1)

if selection == "جواد الحق":
#     st.sidebar.image("images/fakhra_TN.png")
    sheet = client.open("modified_data").get_worksheet(7)
    df = pd.DataFrame(sheet.get_all_records(),index=None)
    csv=df.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button(
            "Download reviewed data",
            csv,
            "file.csv",
            "text/csv",
            key='download-csv-jawad')
    data=df
    if len(df.index)>1:
        chart_data=pd.DataFrame(columns=['index','date'])
        df1 = data['date'].value_counts()
        st.sidebar.bar_chart(df1)

page= PAGES[selection]
page.app()