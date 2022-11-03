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
        data=()
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
       
        date = str(datetime.date.today())
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
        data=(lines_done,english_line,translation,status,comment,date)
    return data

def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return (len(str_list)+1)
    
def fakhra():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
		"https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    # Assign credentials ann path of style sheet
    creds = ServiceAccountCredentials.from_json_keyfile_name("proofreading-app-dr-rp.json", scope)
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
                    next_row=next_available_row(sheet)
                    lines_done=next_row-2 # 1 header row and one for accounting zero-th value
                
                    st.write("lines reviewed = ",lines_done) 
                    if lines_done >= len(df_in):
                        st.success("End of Phase I Data prepared by Ms. Munawer")
                        data=()
                    else:
                        data=sentence_form(english[lines_done],urdu[lines_done],comment_all[lines_done],len(df_in),lines_done)

                    if st.form_submit_button('OK'):     
                        sheet.update_acell("A{}".format(next_row), data[0])
                        sheet.update_acell("B{}".format(next_row), data[1])
                        sheet.update_acell("C{}".format(next_row), data[2])
                        sheet.update_acell("D{}".format(next_row), data[3])
                        sheet.update_acell("E{}".format(next_row), data[4])
                        sheet.update_acell("F{}".format(next_row), data[5])
                        st.session_state.num += 1
                        placeholder.empty()
                        placeholder2.empty()
                    else:
                        st.stop()
def m_bugti():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
		"https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    # Assign credentials ann path of style sheet
    creds = ServiceAccountCredentials.from_json_keyfile_name("proofreading-app-dr-rp.json", scope)
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
                    next_row=next_available_row(sheet)
                    lines_done=next_row-2 # 1 header row and one for accounting zero-th value
                
                    st.write("lines reviewed = ",lines_done) 
                    if lines_done >= len(df_in):
                        st.success("End of Phase I Data prepared by Ms. Munawer")
                        data=()
                    else:
                        data=sentence_form(english[lines_done],urdu[lines_done],comment_all[lines_done],len(df_in),lines_done)

                    if st.form_submit_button('OK'):     
                        sheet.update_acell("A{}".format(next_row), data[0])
                        sheet.update_acell("B{}".format(next_row), data[1])
                        sheet.update_acell("C{}".format(next_row), data[2])
                        sheet.update_acell("D{}".format(next_row), data[3])
                        sheet.update_acell("E{}".format(next_row), data[4])
                        sheet.update_acell("F{}".format(next_row), data[5])
                        st.session_state.num += 1
                        placeholder.empty()
                        placeholder2.empty()
                    else:
                        st.stop()

def t_fatima():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
		"https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    # Assign credentials ann path of style sheet
    creds = ServiceAccountCredentials.from_json_keyfile_name("proofreading-app-dr-rh.json", scope)
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
                    next_row=next_available_row(sheet)
                    lines_done=next_row-2 # 1 header row and one for accounting zero-th value
                
                    st.write("lines reviewed = ",lines_done) 
                    if lines_done >= len(df_in):
                        st.success("End of Phase I Data prepared by Ms. Munawer")
                        data=()
                    else:
                        data=sentence_form(english[lines_done],urdu[lines_done],comment_all[lines_done],len(df_in),lines_done)

                    if st.form_submit_button('OK'):     
                        sheet.update_acell("A{}".format(next_row), data[0])
                        sheet.update_acell("B{}".format(next_row), data[1])
                        sheet.update_acell("C{}".format(next_row), data[2])
                        sheet.update_acell("D{}".format(next_row), data[3])
                        sheet.update_acell("E{}".format(next_row), data[4])
                        sheet.update_acell("F{}".format(next_row), data[5])
                        st.session_state.num += 1
                        placeholder.empty()
                        placeholder2.empty()
                    else:
                        st.stop()

def nisar_MK():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
		"https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    # Assign credentials ann path of style sheet
    creds = ServiceAccountCredentials.from_json_keyfile_name("proofreading-app-dr-rh.json", scope)
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
                    next_row=next_available_row(sheet)
                    lines_done=next_row-2 # 1 header row and one for accounting zero-th value
                
                    st.write("lines reviewed = ",lines_done) 
                    if lines_done >= len(df_in):
                        st.success("End of Phase I Data prepared by Ms. Munawer")
                        data=()
                    else:
                        data=sentence_form(english[lines_done],urdu[lines_done],comment_all[lines_done],len(df_in),lines_done)

                    if st.form_submit_button('OK'):     
                        sheet.update_acell("A{}".format(next_row), data[0])
                        sheet.update_acell("B{}".format(next_row), data[1])
                        sheet.update_acell("C{}".format(next_row), data[2])
                        sheet.update_acell("D{}".format(next_row), data[3])
                        sheet.update_acell("E{}".format(next_row), data[4])
                        sheet.update_acell("F{}".format(next_row), data[5])
                        st.session_state.num += 1
                        placeholder.empty()
                        placeholder2.empty()
                    else:
                        st.stop()
