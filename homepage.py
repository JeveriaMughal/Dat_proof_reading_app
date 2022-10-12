import streamlit as st
import rules,team,score_board,data_flow
def app():
    st.image("images/left-1 - Copy.jpg")
    col1,col2,col3=st.columns([2,2,1])
    with col3:
        selection=st.radio("",["Team Members","Instructions","Team Progress", "Data Progress"])
    
    if selection == "Instructions":
        rules.app()
    if selection == "Team Members":
        team.app()
    if selection == "Team Progress":
        score_board.app()
    if selection == "Data Progress":
        data_flow.app()
