import streamlit as st
import datetime
import pandas as pd
import gspread
from gspread_dataframe import get_as_dataframe, set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
def sentence_form(english,urdu,comment_in,max_len,lines_done):
    if lines_done >= max_len:
        st.success("you have reviewed all the data prepared by this member")
        data=pd.DataFrame()
    else:
        default=""
        col1,col2=st.columns(2)
        with col1:
            st.write("English")
            st.title(english)
            correction_eng=st.text_area("Change sentence",value=default)
            comment=st.text_input("comment",value=comment_in)
        with col2:
            st.write("اردو")
            st.markdown('<h1 class="urdu-font-big">'+urdu+'</h1>', unsafe_allow_html=True)
            correction_urdu=st.text_area("جملہ تبدیل کیجیے",value=default)
            st.write("________________________________________")
            status_other=st.selectbox("Other Options",["NONE","SKIP","PEND","DELETE"])
       
        date = datetime.date.today()
        if status_other == "NONE":
            if correction_eng != "" or correction_urdu != "":
                status="CORRECTED"
            else:
                status="APPROVED"
        else:
            status=status_other
        if correction_urdu=="":
            translation=urdu
        else:
            translation=correction_urdu
        if correction_eng == "":
            english_line = english
        else:
            english_line = correction_eng
        data=pd.DataFrame({'index':[lines_done],'ENG':[english_line],'URDU': [translation],'status':[status],'comment':[comment],'date':[date]})
    return data
    
def fakhra():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
		"https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    # Assign credentials ann path of style sheet
    creds = ServiceAccountCredentials.from_json_keyfile_name("blank-test-363706-5265bab97753.json", scope)
    client = gspread.authorize(creds)
    sheet_no=0
    sheet_in = client.open("modified_data").get_worksheet(sheet_no)
    df_in = pd.DataFrame(sheet_in.get_all_records(),index=None)
    if df_in.empty:
        english=[]
        urdu=[]
        st.write("Miss Fakhra Munawer has not submitted any data yet")
    else:
        english=df_in["ENG"].values.tolist()
        urdu=df_in["URDU"].values.tolist()
        comment_all=df_in["comment"].values.tolist()
        if 'num' not in st.session_state:
            st.session_state.num = 1
        local_css("style.css")
        st.write("CORPUS REVIEW")
        placeholder = st.empty()
        placeholder2 = st.empty()
        while True:    
            num = st.session_state.num

            if placeholder2.button('end', key=num):
                placeholder2.empty()
                break
            else:        
                with placeholder.form(key=str(num)):
                    sheet = client.open("Data_review_phase2").get_worksheet(sheet_no)
                    df = pd.DataFrame(sheet.get_all_records(),index=None)
                    lines_done=(len(df.index))
                    st.write("lines reviewed = ",lines_done) 
                    if lines_done >= len(df_in):
                        st.success("End of Phase I Data prepared by Ms. Munawer")
                        data=pd.DataFrame()
                    else:
                        data=sentence_form(english[lines_done],urdu[lines_done],comment_all[lines_done],len(df_in),lines_done)

                    if st.form_submit_button('OK'):    
                        df=pd.concat([df,data],ignore_index = True, axis = 0)
                        sheet.clear()
                        set_with_dataframe(worksheet=sheet, dataframe=df, include_index=False,include_column_header=True, resize=True)
                        st.session_state.num += 1
                        placeholder.empty()
                        placeholder2.empty()
                    else:
                        st.stop()
def m_bugti():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
		"https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    # Assign credentials ann path of style sheet
    creds = ServiceAccountCredentials.from_json_keyfile_name("blank-test-363706-5265bab97753.json", scope)
    client = gspread.authorize(creds)
    sheet_no=1
    sheet_in = client.open("modified_data").get_worksheet(sheet_no)
    df_in = pd.DataFrame(sheet_in.get_all_records(),index=None)
    if df_in.empty:
        english=[]
        urdu=[]
        st.write("Mr. Mehboob Bugti has not submitted any data yet")
    else:
        english=df_in["ENG"].values.tolist()
        urdu=df_in["URDU"].values.tolist()
        comment_all=df_in["comment"].values.tolist()
        if 'num' not in st.session_state:
            st.session_state.num = 1
        local_css("style.css")
        st.write("CORPUS REVIEW")
        placeholder = st.empty()
        placeholder2 = st.empty()
        while True:    
            num = st.session_state.num

            if placeholder2.button('end', key=num):
                placeholder2.empty()
                break
            else:        
                with placeholder.form(key=str(num)):
                    sheet = client.open("Data_review_phase2").get_worksheet(sheet_no)
                    df = pd.DataFrame(sheet.get_all_records(),index=None)
                    lines_done=(len(df.index))
                    st.write("lines reviewed = ",lines_done) 
                    if lines_done >= len(df_in):
                        st.success("End of Phase I Data prepared by Mr. Bugti")
                        data=pd.DataFrame()
                    else:
                        data=sentence_form(english[lines_done],urdu[lines_done],comment_all[lines_done],len(df_in),lines_done)

                    if st.form_submit_button('OK'):    
                        df=pd.concat([df,data],ignore_index = True, axis = 0)
                        sheet.clear()
                        set_with_dataframe(worksheet=sheet, dataframe=df, include_index=False,include_column_header=True, resize=True)
                        st.session_state.num += 1
                        placeholder.empty()
                        placeholder2.empty()
                    else:
                        st.stop()

def t_fatima():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
		"https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    # Assign credentials ann path of style sheet
    creds = ServiceAccountCredentials.from_json_keyfile_name("blank-test-363706-5265bab97753.json", scope)
    client = gspread.authorize(creds)
    sheet_no=5
    sheet_in = client.open("modified_data").get_worksheet(sheet_no)
    df_in = pd.DataFrame(sheet_in.get_all_records(),index=None)
    if df_in.empty:
        english=[]
        urdu=[]
        st.write("Miss Tanveer Fatima has not submitted any data yet")
    else:
        english=df_in["ENG"].values.tolist()
        urdu=df_in["URDU"].values.tolist()
        comment_all=df_in["comment"].values.tolist()
        if 'num' not in st.session_state:
            st.session_state.num = 1
        local_css("style.css")
        st.write("CORPUS REVIEW")
        placeholder = st.empty()
        placeholder2 = st.empty()
        while True:    
            num = st.session_state.num

            if placeholder2.button('end', key=num):
                placeholder2.empty()
                break
            else:        
                with placeholder.form(key=str(num)):
                    sheet = client.open("Data_review_phase2").get_worksheet(sheet_no)
                    df = pd.DataFrame(sheet.get_all_records(),index=None)
                    lines_done=(len(df.index))
                    st.write("lines reviewed = ",lines_done) 
                    if lines_done >= len(df_in):
                        st.success("End of Phase I Data prepared by Ms. Fatima")
                        data=pd.DataFrame()
                    else:
                        data=sentence_form(english[lines_done],urdu[lines_done],comment_all[lines_done],len(df_in),lines_done)

                    if st.form_submit_button('OK'):    
                        df=pd.concat([df,data],ignore_index = True, axis = 0)
                        sheet.clear()
                        set_with_dataframe(worksheet=sheet, dataframe=df, include_index=False,include_column_header=True, resize=True)
                        st.session_state.num += 1
                        placeholder.empty()
                        placeholder2.empty()
                    else:
                        st.stop()
def nisar_MK():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
		"https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    # Assign credentials ann path of style sheet
    creds = ServiceAccountCredentials.from_json_keyfile_name("blank-test-363706-5265bab97753.json", scope)
    client = gspread.authorize(creds)
    sheet_no=2
    sheet_in = client.open("modified_data").get_worksheet(sheet_no)
    df_in = pd.DataFrame(sheet_in.get_all_records(),index=None)
    if df_in.empty:
        english=[]
        urdu=[]
        st.write("This member has not submitted any data yet")
    else:
        english=df_in["ENG"].values.tolist()
        urdu=df_in["URDU"].values.tolist()
        comment_all=df_in["comment"].values.tolist()
        if 'num' not in st.session_state:
            st.session_state.num = 1
        local_css("style.css")
        st.write("CORPUS REVIEW")
        placeholder = st.empty()
        placeholder2 = st.empty()
        while True:    
            num = st.session_state.num

            if placeholder2.button('end', key=num):
                placeholder2.empty()
                break
            else:        
                with placeholder.form(key=str(num)):
                    sheet = client.open("Data_review_phase2").get_worksheet(sheet_no)
                    df = pd.DataFrame(sheet.get_all_records(),index=None)
                    lines_done=(len(df.index))
                    st.write("lines reviewed = ",lines_done) 
                    if lines_done >= len(df_in):
                        st.success("End of Phase I Data prepared by Mr. Mamakhel")
                        data=pd.DataFrame()
                    else:
                        data=sentence_form(english[lines_done],urdu[lines_done],comment_all[lines_done],len(df_in),lines_done)

                    if st.form_submit_button('OK'):    
                        df=pd.concat([df,data],ignore_index = True, axis = 0)
                        sheet.clear()
                        set_with_dataframe(worksheet=sheet, dataframe=df, include_index=False,include_column_header=True, resize=True)
                        st.session_state.num += 1
                        placeholder.empty()
                        placeholder2.empty()
                    else:
                        st.stop()