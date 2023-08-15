import streamlit as st
import rashid_hameed_page1,phase1_review,revision_RH
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
def app():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
    "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
# Assign credentials ann path of style sheet
    creds = ServiceAccountCredentials.from_json_keyfile_name("blank-test-363706-5265bab97753.json", scope)
    client = gspread.authorize(creds)
    sheet1 = client.open("modified_data").get_worksheet(2)
    df1 = pd.DataFrame(sheet1.get_all_records(),index=None)
    sheet2 = client.open("modified_data").get_worksheet(5)
    df2 = pd.DataFrame(sheet2.get_all_records(),index=None)
    file2=open("master_data/official-terms-1.ur","r")
    glossary=file2.readlines()
    column1,column2,column3=st.columns(3)
    with column1:
        st.metric(label="Executive Director", value="Dr. Rashid Hameed", delta="Phase II Reviewer", delta_color="normal", help=None)
    with column2:
        st.metric(label="Assigned Data Sets", value="3", delta="Glossary & Phase I Corpus", delta_color="normal", help=None)
    with column3:
        st.metric(label="Assigned Lines", value="Glossary:"+ str(len(glossary))+"|"+"Corpus:"+str(len(df1)+len(df2)), delta=None, delta_color="normal", help=None)

    col1,col2,col3=st.columns([2,2,1])
    with col3:
        selection=st.radio("DATA SET",["GLOSSARY","TANVEER FATIMA","NISAR MAMAKHEL"])
        revise=st.checkbox("Revise your work")
    if revise:
        if selection == "GLOSSARY":
            revision_RH.app_glossary()
        if selection == "TANVEER FATIMA":
            revision_RH.app_corpus_T()
        if selection =="NISAR MAMAKHEL":
            revision_RH.app_corpus_N()
    else:
        if selection == "GLOSSARY":
            rashid_hameed_page1.app()
        if selection =="TANVEER FATIMA":
            phase1_review.t_fatima()
        if selection =="NISAR MAMAKHEL":
            phase1_review.nisar_MK()
        