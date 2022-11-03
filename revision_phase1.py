import streamlit as st
import pandas as pd
import datetime
import gspread
from gspread_dataframe import get_as_dataframe, set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def sentence_form(line_number,row):
    local_css("style.css")
    english=        row[1]
    urdu=           row[2]
    status_prev=    row[3]
    comment_prev=   row[4]
    date_prev=      row[5]

    st.write("index number = ",line_number-2)
    if line_number < 0 :
        st.success("you have revised all the existing data allocated to you")
        data =pd.DataFrame()
    else:
        default=""
        col1,col2=st.columns(2)
        with col1:
            st.write("English")
            st.title(english)
            correction_eng=st.text_area("Change sentence",value=default)
        with col2:
            st.write("اردو")
            st.markdown('<h1 class="urdu-font-big">'+urdu+'</h1>', unsafe_allow_html=True)
            correction_urdu=st.text_area("جملہ تبدیل کریں",value=default)
        comment_new=st.text_area("comment",value=comment_prev)
        if comment_new ==comment_prev:
            comment=comment_prev
        else:
            comment=comment_new

        date_new = str(datetime.date.today())
        if correction_eng != "" or correction_urdu != "":
            status="REVISED"
            date=date_new
        else:
            status=status_prev
            date=date_prev
        if correction_urdu=="":
            translation=urdu
        else:
            translation=correction_urdu
        if correction_eng == "":
            english_line = english
        else:
            english_line = correction_eng
        data=(line_number-2,english_line,translation,status,comment,date)
    return data

def last_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return (len(str_list))

def app_fakhra():
    if 'num' not in st.session_state:
        st.session_state.num = 1
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
		"https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    # Assign credentials ann path of style sheet
    creds = ServiceAccountCredentials.from_json_keyfile_name("proofreading-app-fakhra.json", scope)
    client = gspread.authorize(creds)

    local_css("style.css")

    sheet = client.open("modified_data").get_worksheet(0)
    lines_done=last_available_row(sheet)
    col1,col2,col3=st.columns([0.25,3,1])
    with col3:
            show_data=st.checkbox("Show Data")
    with col2:
        if show_data:
            if lines_done>1:
                df=pd.DataFrame(sheet.get_all_records())
                df.set_index('index', inplace=True)
                st.dataframe(df)
            else:
                st.error("NO DATA TO SHOW")
    if lines_done<=1:
        st.error("Please review some data first, then come back to the revision page")
    else:
        col_left,col_right=st.columns([5,1])
        with col_right:
            line_number=(st.number_input("choose index number",min_value=0,max_value=lines_done-2,format="%i",value=lines_done-2)+2)  

        placeholder = st.empty()
        placeholder2 = st.empty()
        while True:    
            num = st.session_state.num

            if placeholder2.button('end', key=num):
                placeholder2.empty()
                break
            else:        
                with placeholder.form(key=str(num)):
                    row=sheet.row_values(line_number)
                    data=sentence_form(line_number,row)
                    

                    if st.form_submit_button('ok'):  
                        sheet.update_acell("A{}".format(line_number), data[0])
                        sheet.update_acell("B{}".format(line_number), data[1])
                        sheet.update_acell("C{}".format(line_number), data[2])
                        sheet.update_acell("D{}".format(line_number), data[3])
                        sheet.update_acell("E{}".format(line_number), data[4])
                        sheet.update_acell("F{}".format(line_number), data[5])
                        st.session_state.num += 1
                        placeholder.empty()
                        placeholder2.empty()

                    
                    else:
                        st.stop()

def app_bugti():
    if 'num' not in st.session_state:
        st.session_state.num = 1
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
		"https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    # Assign credentials ann path of style sheet
    creds = ServiceAccountCredentials.from_json_keyfile_name("proofreading-app-m-bugti.json", scope)
    client = gspread.authorize(creds)

    local_css("style.css")

    sheet = client.open("modified_data").get_worksheet(1)
    lines_done=last_available_row(sheet)
    col1,col2,col3=st.columns([0.25,3,1])
    with col3:
            show_data=st.checkbox("Show Data")
    with col2:
        if show_data:
            if lines_done>1:
                df=pd.DataFrame(sheet.get_all_records())
                df.set_index('index', inplace=True)
                st.dataframe(df)
            else:
                st.error("NO DATA TO SHOW")
    if lines_done<=1:
        st.error("Please review some data first, then come back to the revision page")
    else:
        col_left,col_right=st.columns([5,1])
        with col_right:
            line_number=(st.number_input("choose index number",min_value=0,max_value=lines_done-2,format="%i",value=lines_done-2)+2)
        placeholder = st.empty()
        placeholder2 = st.empty()
        while True:    
            num = st.session_state.num

            if placeholder2.button('end', key=num):
                placeholder2.empty()
                break
            else:        
                with placeholder.form(key=str(num)):
                    row=sheet.row_values(line_number)
                    data=sentence_form(line_number,row)
                    

                    if st.form_submit_button('ok'):  
                        sheet.update_acell("A{}".format(line_number), data[0])
                        sheet.update_acell("B{}".format(line_number), data[1])
                        sheet.update_acell("C{}".format(line_number), data[2])
                        sheet.update_acell("D{}".format(line_number), data[3])
                        sheet.update_acell("E{}".format(line_number), data[4])
                        sheet.update_acell("F{}".format(line_number), data[5])
                        st.session_state.num += 1
                        placeholder.empty()
                        placeholder2.empty()

                    
                    else:
                        st.stop()

def app_nisar():
    if 'num' not in st.session_state:
        st.session_state.num = 1
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
		"https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    # Assign credentials ann path of style sheet
    creds = ServiceAccountCredentials.from_json_keyfile_name("proofreading-app-n-mk.json", scope)
    client = gspread.authorize(creds)

    local_css("style.css")

    sheet = client.open("modified_data").get_worksheet(2)
    lines_done=last_available_row(sheet)
    col1,col2,col3=st.columns([0.25,3,1])
    with col3:
            show_data=st.checkbox("Show Data")
    with col2:
        if show_data:
            if lines_done>1:
                df=pd.DataFrame(sheet.get_all_records())
                df.set_index('index', inplace=True)
                st.dataframe(df)
            else:
                st.error("NO DATA TO SHOW")
    if lines_done<=1:
        st.error("Please review some data first, then come back to the revision page")
    else:
        col_left,col_right=st.columns([5,1])
        with col_right:
            line_number=(st.number_input("choose index number",min_value=0,max_value=lines_done-2,format="%i",value=lines_done-2)+2)
   
        placeholder = st.empty()
        placeholder2 = st.empty()
        while True:    
            num = st.session_state.num

            if placeholder2.button('end', key=num):
                placeholder2.empty()
                break
            else:        
                with placeholder.form(key=str(num)):
                    row=sheet.row_values(line_number)
                    data=sentence_form(line_number,row)
                    

                    if st.form_submit_button('ok'):  
                        sheet.update_acell("A{}".format(line_number), data[0])
                        sheet.update_acell("B{}".format(line_number), data[1])
                        sheet.update_acell("C{}".format(line_number), data[2])
                        sheet.update_acell("D{}".format(line_number), data[3])
                        sheet.update_acell("E{}".format(line_number), data[4])
                        sheet.update_acell("F{}".format(line_number), data[5])
                        st.session_state.num += 1
                        placeholder.empty()
                        placeholder2.empty()

                    
                    else:
                        st.stop()

def app_tf():
    if 'num' not in st.session_state:
        st.session_state.num = 1
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
		"https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    # Assign credentials ann path of style sheet
    creds = ServiceAccountCredentials.from_json_keyfile_name("proofreading-app-tf.json", scope)
    client = gspread.authorize(creds)

    local_css("style.css")

    sheet = client.open("modified_data").get_worksheet(5)
    lines_done=last_available_row(sheet)
    col1,col2,col3=st.columns([0.25,3,1])
    with col3:
            show_data=st.checkbox("Show Data")
    with col2:
        if show_data:
            if lines_done>1:
                df=pd.DataFrame(sheet.get_all_records())
                df.set_index('index', inplace=True)
                st.dataframe(df)
            else:
                st.error("NO DATA TO SHOW")
    if lines_done<=1:
        st.error("Please review some data first, then come back to the revision page")
    else:
        col_left,col_right=st.columns([5,1])
        with col_right:
            line_number=(st.number_input("choose index number",min_value=0,max_value=lines_done-2,format="%i",value=lines_done-2)+2)
   
        placeholder = st.empty()
        placeholder2 = st.empty()
        while True:    
            num = st.session_state.num

            if placeholder2.button('end', key=num):
                placeholder2.empty()
                break
            else:        
                with placeholder.form(key=str(num)):
                    row=sheet.row_values(line_number)
                    data=sentence_form(line_number,row)
                    

                    if st.form_submit_button('ok'):  
                        sheet.update_acell("A{}".format(line_number), data[0])
                        sheet.update_acell("B{}".format(line_number), data[1])
                        sheet.update_acell("C{}".format(line_number), data[2])
                        sheet.update_acell("D{}".format(line_number), data[3])
                        sheet.update_acell("E{}".format(line_number), data[4])
                        sheet.update_acell("F{}".format(line_number), data[5])
                        st.session_state.num += 1
                        placeholder.empty()
                        placeholder2.empty()

                    
                    else:
                        st.stop()