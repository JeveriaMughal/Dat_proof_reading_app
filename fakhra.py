import streamlit as st
import pandas as pd
import datetime
import gspread
from gspread_dataframe import get_as_dataframe, set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials



def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
def sentence_form(lines_done):
    local_css("style.css")
    file1=open("master_data/MC_ENG_1.txt","r")
    english=file1.readlines()
    file2=open("master_data/MC_URDU_1.txt","r")
    urdu=file2.readlines()
    st.write("lines reviewed = ",lines_done)
    if lines_done >= len(urdu) or lines_done >= len(english):
        st.success("you have reviewed all the existing data allocated to you")
        data =pd.DataFrame()
    else:
        default=""
        col1,col2=st.columns(2)
        with col1:
            st.write("English")
            st.title(english[lines_done])
            correction_eng=st.text_area("Change sentence",value=default)
        with col2:
            st.write("اردو")
            # st.title(urdu[lines_done])
            st.markdown('<h1 class="urdu-font-big">'+urdu[lines_done]+'</h1>', unsafe_allow_html=True)
            correction_urdu=st.text_area("جملہ تبدیل کریں",value=default)
        comment=st.text_area("comment",value=default)
        date = str(datetime.date.today())
        if correction_eng != "" or correction_urdu != "":
            status="CORRECTED"
        else:
            status="APPROVED"
        if correction_urdu=="":
            translation=urdu[lines_done]
        else:
            translation=correction_urdu
        if correction_eng == "":
            english_line = english[lines_done]
        else:
            english_line = correction_eng
        data=(lines_done,english_line,translation,status,comment,date)
    return data
def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return (len(str_list)+1)
    
def app():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
		"https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    # Assign credentials ann path of style sheet
    creds = ServiceAccountCredentials.from_json_keyfile_name("blank-test-363706-5265bab97753.json", scope)
    client = gspread.authorize(creds)
    file1=open("master_data/MC_ENG_1.txt","r")
    english=file1.readlines()
    if 'num' not in st.session_state:
        st.session_state.num = 1
    local_css("style.css")
    column1,column2,column3=st.columns(3)
    with column1:
        st.metric(label="Team Member (Language)", value="Fakhra Munawar", delta="Phase I Reviwer", delta_color="normal", help=None)
    with column2:
        st.metric(label="Assigned Data Sets", value="1", delta="CORPUS", delta_color="normal", help=None)
    with column3:
        st.metric(label="Assigned Lines", value=len(english), delta=None, delta_color="normal", help=None)

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
                sheet = client.open("modified_data").get_worksheet(0)
                next_row=next_available_row(sheet)
                lines_done=next_row-2 # 1 header row and one for accounting zero-th value
                st.write(lines_done)
                data=sentence_form(lines_done)

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

