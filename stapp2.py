import streamlit as st
import pandas as pd

if 'num' not in st.session_state:
    st.session_state.num = 1

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
def sentence_form(lines_done):
    file1=open("master_data/MC_ENG.txt","r")
    english=file1.readlines()
    file2=open("master_data/MC_URDU.txt","r")
    urdu=file2.readlines()
    st.write("lines reviewed = ",lines_done)
    default=""
    col1,col2=st.columns(2)
    with col1:
        st.write("English")
        st.title(english[lines_done])
        correction_eng=st.text_input("Change sentence",value=default)
    with col2:
        st.write("اردو")
        st.title(urdu[lines_done])
        correction_urdu=st.text_input("جملہ تبدیل کریں",value=default)
    comment=st.text_input("comment",value=default)
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
    data=pd.DataFrame({'ENG':[english_line],'URDU': [translation],'status':[status],'comment':[comment],'index':[lines_done]})
    return data
    
def app():
    local_css("style.css")
    st.write("welcome Dania")
    placeholder = st.empty()
    placeholder2 = st.empty()
    while True:    
        num = st.session_state.num

        if placeholder2.button('end', key=num):
            placeholder2.empty()
            break
        else:        
            with placeholder.form(key=str(num)):
                df=pd.DataFrame(columns=['index','ENG', 'URDU','status','comment'])
                data=pd.read_csv("modified_data/dania.csv")
                df=pd.concat([df,data],ignore_index = True, axis = 0)
                lines_done=(len(df.index))
                data=sentence_form(lines_done)

                if st.form_submit_button('OK'):    
                    df=pd.concat([df,data],ignore_index = True, axis = 0)
                    df.to_csv("modified_data/dania.csv",index=False)
                    st.session_state.num += 1
                    placeholder.empty()
                    placeholder2.empty()
                else:
                    st.stop()



