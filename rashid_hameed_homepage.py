import streamlit as st
import rashid_hameed_page1
def app():
    file2=open("master_data/official-terms-1.ur","r")
    glossary=file2.readlines()
    column1,column2,column3=st.columns(3)
    with column1:
        st.metric(label="Deputy Secretary", value="Dr. Rashid Hameed", delta=None, delta_color="normal", help=None)
    with column2:
        st.metric(label="Assigned Data Sets", value="1", delta="GLOSSARY", delta_color="normal", help=None)
    with column3:
        st.metric(label="Assigned Lines", value=str(len(glossary)), delta=None, delta_color="normal", help=None)

    # col1,col2,col3=st.columns([2,2,1])
    # with col3:
    #     selection=st.radio("DATA SET",["GLOSSARY","CORPUS"])
    
    # if selection == "CORPUS":
    #     rauf_parekh.app()
    # if selection == "GLOSSARY":
    #     rauf_parekh_glossary.app()
    rashid_hameed_page1.app()