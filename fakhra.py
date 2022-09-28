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
            correction_eng=st.text_input("Change sentence",value=default)
        with col2:
            st.write("اردو")
            # st.title(urdu[lines_done])
            st.markdown('<h1 class="urdu-font-big">'+urdu[lines_done]+'</h1>', unsafe_allow_html=True)
            correction_urdu=st.text_input("جملہ تبدیل کریں",value=default)
        comment=st.text_input("comment",value=default)
        date = datetime.date.today()
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
        data=pd.DataFrame({'ENG':[english_line],'URDU': [translation],'status':[status],'comment':[comment],'index':[lines_done],'date':[date]})
    return data
    
def app():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
		"https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    # Assign credentials ann path of style sheet
    creds = ServiceAccountCredentials.from_json_keyfile_name("blank-test-363706-5265bab97753.json", scope)
    client = gspread.authorize(creds)

    if 'num' not in st.session_state:
        st.session_state.num = 1
    local_css("style.css")
    st.write("Username: Fakhra Munwar")

    placeholder = st.empty()
    placeholder2 = st.empty()
    while True:    
        num = st.session_state.num

        if placeholder2.button('end', key=num):
            placeholder2.empty()
            break
        else:        
            with placeholder.form(key=str(num)):
                # df=pd.DataFrame(columns=['index','ENG', 'URDU','status','comment','date'])
                # data=pd.read_csv("modified_data/Jeveria.csv")
                # df=pd.concat([df,data],ignore_index = True, axis = 0)
                sheet = client.open("modified_data").get_worksheet(0)
                df = pd.DataFrame(sheet.get_all_records(),index=None)
                lines_done=(len(df.index))
                data=sentence_form(lines_done)

                if st.form_submit_button('OK'):    
                    df=pd.concat([df,data],ignore_index = True, axis = 0)
                    # df.to_csv("modified_data/Jeveria.csv",index=False)
                    sheet.clear()
                    set_with_dataframe(worksheet=sheet, dataframe=df, include_index=False,include_column_header=True, resize=True)
                    st.session_state.num += 1
                    placeholder.empty()
                    placeholder2.empty()
                else:
                    st.stop()

