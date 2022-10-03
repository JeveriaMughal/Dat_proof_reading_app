import streamlit as st
import rauf_parekh,rauf_parekh_glossary
def app():
    file1=open("master_data/MC_ENG_all.txt","r")
    corpus=file1.readlines()
    file2=open("master_data/official-terms.ur","r")
    glossary=file2.readlines()
    column1,column2,column3=st.columns(3)
    with column1:
        st.metric(label="Director General", value="Prof. Dr. Rauf Parekh", delta=None, delta_color="normal", help=None)
    with column2:
        st.metric(label="Assigned Data Sets", value="2", delta="GLOSSARY & CORPUS", delta_color="normal", help=None)
    with column3:
        st.metric(label="Assigned Lines", value="Glossary:"+ str(len(glossary))+"|"+"Corpus:"+str(len(corpus)), delta=None, delta_color="normal", help=None)

    col1,col2,col3=st.columns([2,2,1])
    with col3:
        selection=st.radio("DATA SET",["GLOSSARY","CORPUS"])
    
    if selection == "CORPUS":
        rauf_parekh.app()
    if selection == "GLOSSARY":
        rauf_parekh_glossary.app()
