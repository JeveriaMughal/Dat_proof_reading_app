import streamlit as st 
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def app():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
    "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    # Assign credentials ann path of style sheet
    creds = ServiceAccountCredentials.from_json_keyfile_name("proofreading-app-stats.json", scope)
    client = gspread.authorize(creds)
    sheet1 = client.open("modified_data").get_worksheet(0)
    df1 = pd.DataFrame(sheet1.get_all_records(),index=None)
    sheet2 = client.open("modified_data").get_worksheet(1)
    df2 = pd.DataFrame(sheet2.get_all_records(),index=None)
    # file1=open("master_data/MC_ENG_all.txt","r")
    # corpus=file1.readlines()
    file2=open("master_data/official-terms.ur","r")
    glossary=file2.readlines()
    column1,column2,column3,column4,cloumn5=st.columns([.5,2,1,2,1])
    with column2:
        st.metric(label="Former Director General NLPD", value="Prof. Dr. Rauf Parekh", delta="Phase II Reviewer", delta_color="inverse", help=None)
    with column3:
        st.metric(label="Assigned Data Sets", value="2", delta="GLOSSARY & CORPUS", delta_color="normal", help=None)
    with column4:
        st.metric(label="Assigned Lines", value="Glossary:"+ str(len(glossary))+"|"+"Corpus:"+str(len(df1)+len(df2)), delta=None, delta_color="normal", help=None)
    with column1:
        st.image("images/DG Dr Rauf Parekh.png")
    
    sheet3 = client.open("modified_data").get_worksheet(2)
    df3 = pd.DataFrame(sheet3.get_all_records(),index=None)
    sheet4 = client.open("modified_data").get_worksheet(5)
    df4 = pd.DataFrame(sheet4.get_all_records(),index=None)
    file2=open("master_data/official-terms-1.ur","r")
    glossary=file2.readlines()
    column1,column2,column3,column4,cloumn5=st.columns([.5,2,1,2,1])
    with column1:
        st.image("images/dr_rashid_TN.png")
    with column2:
        st.metric(label="Director General, NLPD", value="Dr. Rashid Hameed", delta="Phase II Reviewer", delta_color="inverse", help=None)
    with column3:
        st.metric(label="Assigned Data Sets", value="1", delta="GLOSSARY & CORPUS", delta_color="normal", help=None)
    with column4:
        st.metric(label="Assigned Lines",value="Glossary:"+ str(len(glossary))+"|"+"Corpus:"+str(len(df3)+len(df4)), delta=None, delta_color="normal", help=None)
    
    file1=open("master_data/MC_ENG.txt","r")
    english=file1.readlines()
    column1,column2,column3,column4,cloumn5=st.columns([.5,2,1,2,1])
    with column1:
         st.image("images/m_bugti_TN.png") 
    with column2:
        st.metric(label="Principle Investigator, NLP-LAB", value="Mehboob Bugti", delta="Phase I Reviewer", delta_color="off", help=None)
    with column3:
        st.metric(label="Assigned Data Sets", value="1", delta="CORPUS", delta_color="normal", help=None)
    with column4:
        st.metric(label="Assigned Lines", value=len(english), delta=None, delta_color="normal", help=None)

    file1=open("master_data/MC_ENG_1.txt","r")
    english=file1.readlines()
    column1,column2,column3,column4,cloumn5=st.columns([.5,2,1,2,1])
    with column1:
         st.image("images/fakhra_TN.png") 
    with column2:
        st.metric(label="Team Member (Language), NLP-LAB", value="Fakhra Munawar", delta="Phase I Reviewer", delta_color="off", help=None)
    with column3:
        st.metric(label="Assigned Data Sets", value="1", delta="CORPUS", delta_color="normal", help=None)
    with column4:
        st.metric(label="Assigned Lines", value=len(english), delta=None, delta_color="normal", help=None)
    
    file1=open("master_data/MC_ENG_TF.txt","r")
    corpus=file1.readlines()
    # file2=open("master_data/official-terms.ur","r")
    # glossary=file2.readlines()
    column1,column2,column3,column4,cloumn5=st.columns([.5,2,1,2,1])
    with column1:
        st.image("images/TF_TN.png") 
    with column2:
        st.metric(label="Assistant informatics Officer, NLPD", value="Tanveer Fatima", delta="Phase I Reviewer", delta_color="off", help=None)
    with column3:
        st.metric(label="Assigned Data Sets", value="1", delta="CORPUS", delta_color="normal", help=None)
    with column4:
        st.metric(label="Assigned Lines", value=str(len(corpus)), delta=None, delta_color="normal", help=None)

    file1=open("master_data/MC_ENG_NMK.txt","r")
    corpus=file1.readlines()
    
    column1,column2,column3,column4,cloumn5=st.columns([.5,2,1,2,1])
    with column1:
        st.image("images/NMK.png") 
    with column2:
        st.metric(label="Programmer, NLPD", value="Nisar Mamakhel", delta="Phase I Reviewer", delta_color="off", help=None)
    with column3:
        st.metric(label="Assigned Data Sets", value="1", delta="CORPUS", delta_color="normal", help=None)
    with column4:
        st.metric(label="Assigned Lines", value=str(len(corpus)), delta=None, delta_color="normal", help=None)

    file1=open("master_data/jawad.en","r")
    corpus=file1.readlines()
    
    column1,column2,column3,column4,cloumn5=st.columns([.5,2,1,2,1])
    with column1:
        st.image("images/umer_farooq_TN.png") 
    with column2:
        st.metric(label="DEO, NLPD", value="Umer Farooq", delta="Phase I Reviewer", delta_color="off", help=None)
    with column3:
        st.metric(label="Assigned Data Sets", value="1", delta="CORPUS", delta_color="normal", help=None)
    with column4:
        st.metric(label="Assigned Lines", value=str(len(corpus)), delta=None, delta_color="normal", help=None)
