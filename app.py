import streamlit as st
import stapp1,stapp2,rauf_parekh

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")
PAGES = {"جویریہ مغل": stapp1,
        "دانیہ شفیق":stapp2,
        "پروفیسر ڈاکٹر رؤف پاریکھ":rauf_parekh}
st.sidebar.title("NLP-L \n Proof reading app")
selection = st.sidebar.selectbox("نام",list (PAGES.keys()))
if selection == "جویریہ مغل":
    st.sidebar.image("images/jeveria.jpeg")
if selection == "دانیہ شفیق":
    st.sidebar.image("images/dania.JPG")
if selection == "پروفیسر ڈاکٹر رؤف پاریکھ":
    st.sidebar.image("images/DG Dr Rauf Parekh.png")


page= PAGES[selection]
page.app()