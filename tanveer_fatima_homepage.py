import streamlit as st
import tanveer_fatima_page1
def app():
    file1=open("master_data/MC_ENG_TF.txt","r")
    corpus=file1.readlines()
    # file2=open("master_data/official-terms.ur","r")
    # glossary=file2.readlines()
    column1,column2,column3=st.columns(3)
    with column1:
        st.metric(label="Assistant informatics Officer, NLPD", value="Tanveer Fatima", delta=None, delta_color="normal", help=None)
    with column2:
        st.metric(label="Assigned Data Sets", value="1", delta="CORPUS", delta_color="normal", help=None)
    with column3:
        st.metric(label="Assigned Lines", value=str(len(corpus)), delta=None, delta_color="normal", help=None)

    # col1,col2,col3=st.columns([2,2,1])
    # with col3:
    #     selection=st.radio("DATA SET",["GLOSSARY","CORPUS"])
    
    # if selection == "CORPUS":
    #     rauf_parekh.app()
    # if selection == "GLOSSARY":
    #     rauf_parekh_glossary.app()


    tanveer_fatima_page1.app()
