import streamlit as st 

def app():
    st.title(':open_book: En-Ur Parallel Corpus Proofreading Instructions')
    st.warning("If Urdu language text is available and English text is missing, add English text")
    st.info("If English language text is available and Urdu text is missing, add to Urdu text")
    st.warning("Correct grammar mistakes of English and Urdu language text e.g. adding space after punctuation marks etc")
    st.info("Correct text on both sides if found incorrect. ")
    st.warning("Remove Urdu text from English side and remove any English text from Urdu side (Translate English Terms into Urdu Terms)")
    st.info("When words are separated by / in both sides and meaning is given in both sides: do not make any modification e.g.")
    col1,col2=st.columns(2)
    with col1:
        st.write("English")
        st.title("Ministries/ Divisions")
    with col2:
        st.write("اردو")
        st.title("وزارتوں/ ڈویژنوں")
    st.success("this is correct :white_check_mark:")
    st.warning("When words are separated by / in one side of text and missing in other, keep only one word that best fits the sentence or is context dependent. e.g. ")
    col3,col4=st.columns(2)
    with col3:
        st.write("English")
        st.title("Reduction in penalty through appeal")
        st.success("")

    with col4:
        st.write("اردو")
        st.title("بذریعہ اپیل بری الذمہ ہونے پر بحالی/ سزا میں کمی")
        st.error("بذریعہ اپیل بری الذمہ ہونے پر سزا میں کمی")
    st.write("When words are separated by / in one side of text and missing in other, and we want to keep the word that is recurrent and does not depend on context, then replace only once and add comment to replace in the whole file in the final stage of evaluation. e.g.")
    col5,col6=st.columns(2) 
    with col5:
        st.write("English")
        st.title("file")
    with col6:
        st.write("اردو")
        st.title(" فائل/ مسل")
    st.success(":spiral_note_pad: Comment: replace all فائل = مسل")
    st.info("Oftentimes / is used with reference numbers or additional information. In that case keep the information as it is. e.g.")
    st.title("ڈائریکٹر (انتظامیہ)/ چیئرمین")
    st.title("یوانِ اُردو، پطرس بخاری روڈ، ایچ ۔۴/۸")
    st.success("This is correct :white_check_mark:")
    st.warning("If information on any side of text (English/Urdu) is missing indicated with "....." then please add the missing information and remove "....."")
    st.info("Please make sure that the information added is unique and completes the sense of a sentence e.g.")
    col7,col8=st.columns(2) 
    with col7:
        st.write("English")
        st.title("No. ------------------- Islamabad, Date: ---------")
        st.error("No. R/23/42-9 Islamabad, (Date) 20/10/2022")
    with col8:
        st.write("اردو")
        st.title("نمبر--------------------- اسلام آباد، (تاریخ)-------------")
        st.error("نمبر ۹-۲۳/۴۲/ار اسلام آباد، (تاریخ) ۲۰​/۱۰/۲۰۲۲")
    st.succes("Note: In case of any ambiguity regarding instructions or data, kindly contact MT team for further assistance.")
