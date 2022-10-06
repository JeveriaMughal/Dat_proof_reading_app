import streamlit as st 

def app():
    file1=open("master_data/MC_ENG_all.txt","r")
    corpus=file1.readlines()
    file2=open("master_data/official-terms.ur","r")
    glossary=file2.readlines()
    column1,column2,column3,column4,cloumn5=st.columns([.5,2,1,2,1])
    with column2:
        st.metric(label="Director General, NLPD", value="Prof. Dr. Rauf Parekh", delta=None, delta_color="normal", help=None)
    with column3:
        st.metric(label="Assigned Data Sets", value="2", delta="GLOSSARY & CORPUS", delta_color="normal", help=None)
    with column4:
        st.metric(label="Assigned Lines", value="Glossary:"+ str(len(glossary))+"|"+"Corpus:"+str(len(corpus)), delta=None, delta_color="normal", help=None)
    with column1:
        st.image("images/DG Dr Rauf Parekh.png")
    
    file2=open("master_data/official-terms-1.ur","r")
    glossary=file2.readlines()
    column1,column2,column3,column4,cloumn5=st.columns([.5,2,1,2,1])
    with column1:
        st.image("images/dr_rashid_TN.png")
    with column2:
        st.metric(label="Deputy Secretary, NLPD", value="Dr. Rashid Hameed", delta=None, delta_color="normal", help=None)
    with column3:
        st.metric(label="Assigned Data Sets", value="1", delta="GLOSSARY", delta_color="normal", help=None)
    with column4:
        st.metric(label="Assigned Lines", value=str(len(glossary)), delta=None, delta_color="normal", help=None)
    
    file1=open("master_data/MC_ENG.txt","r")
    english=file1.readlines()
    column1,column2,column3,column4,cloumn5=st.columns([.5,2,1,2,1])
    with column1:
         st.image("images/m_bugti_TN.png") 
    with column2:
        st.metric(label="Principle Investigator, NLP-LAB", value="Mehboob Bugti", delta=None, delta_color="normal", help=None)
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
        st.metric(label="Team Member (Language), NLP-LAB", value="Fakhra Munawar", delta=None, delta_color="normal", help=None)
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
        st.metric(label="Assistant informatics Officer, NLPD", value="Tanveer Fatima", delta=None, delta_color="normal", help=None)
    with column3:
        st.metric(label="Assigned Data Sets", value="1", delta="CORPUS", delta_color="normal", help=None)
    with column4:
        st.metric(label="Assigned Lines", value=str(len(corpus)), delta=None, delta_color="normal", help=None)