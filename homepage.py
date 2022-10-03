import streamlit as st
import rules,team
def app():
    st.image("images/left-1 - Copy.jpg")
    col1,col2,col3=st.columns([2,2,1])
    with col3:
        selection=st.radio("",["Team","Instructions"])
    
    if selection == "Instructions":
        rules.app()
    if selection == "Team":
        team.app()