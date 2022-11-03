import pandas as pd
import plotly.graph_objects as go
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
def colour():
  import random
  r=random.randint(0,255)
  g=random.randint(0,255)
  b=random.randint(0,255)
  a=0.5
  c="rgba("+str(r)+","+str(g)+","+str(b)+","+str(a)+")"
  # print(c)
  return c
def app():
    column1,column2=st.columns([1,1])
    with column1:
      # st.header('Data Preparation')
      st.title("Initial Data ----> Final Data")
    #Read Initial data files
    Corpus_Data=len(open("master_data/daftari-zuban-ka-taruf.en","r").readlines())
    #print(Corpus_Data)
    Glossary_1=len(open("master_data/official-terms.en","r").readlines())
    Glossary_2=len(open("master_data/official-terms-1.en","r").readlines())
    Glossary=Glossary_1+Glossary_2
    assigned_Bughti=len(open("master_data/MC_ENG.txt","r").readlines())
    assigned_Fakhra=len(open("master_data/MC_ENG_1.txt","r").readlines())
    assigned_TF=len(open("master_data/MC_ENG_TF.txt","r").readlines())
    assigned_NMK=len(open("master_data/MC_ENG_NMK.txt","r").readlines())
    assigned_RP=len(open("master_data/MC_ENG_all.txt","r").readlines())
    #Google sheet credentials
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
        "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("proofreading-app-stats.json", scope)
    client = gspread.authorize(creds)
    #phase1 sheets 
    sheet=client.open("modified_data").get_worksheet(0)
    df_Fakhra=len(pd.DataFrame(sheet.get_all_records(),index=None))
    sheet1=client.open("modified_data").get_worksheet(1)
    df_Bughti=len(pd.DataFrame(sheet1.get_all_records(),index=None))
    sheet2=client.open("modified_data").get_worksheet(2)
    df_NMK=len(pd.DataFrame(sheet2.get_all_records(),index=None))
    #print(df_NMK)
    sheet3=client.open("modified_data").get_worksheet(5)
    df_TF=len(pd.DataFrame(sheet3.get_all_records(),index=None))
    #Phase2 sheets
    sheet4=client.open("Data_review_phase2").get_worksheet(0)
    df1_P2_Fakhra=len(pd.DataFrame(sheet4.get_all_records(),index=None))
    sheet5=client.open("Data_review_phase2").get_worksheet(1)
    df1_P2_Bughti=len(pd.DataFrame(sheet5.get_all_records(),index=None))
    sheet6=client.open("Data_review_phase2").get_worksheet(2)
    df1_P2_NMK=len(pd.DataFrame(sheet6.get_all_records(),index=None))
    sheet7=client.open("Data_review_phase2").get_worksheet(5)
    df1_P2_TF=len(pd.DataFrame(sheet7.get_all_records(),index=None))

    sheet8=client.open("Data_review_phase2").get_worksheet(3)
    df_RPG=len(pd.DataFrame(sheet8.get_all_records(),index=None))
    sheet9=client.open("Data_review_phase2").get_worksheet(4)
    df_DRG=len(pd.DataFrame(sheet9.get_all_records(),index=None))
    #corpus Dr Rashid=corpus_TF+corpus NMK
    df_DRC=df1_P2_NMK+df1_P2_TF

    sheet10=client.open("Data_review_phase2").get_worksheet(6)
    #CORPUS DG=phase2 corpus+corpus Fakhra+corpus sir bughti
    df_RPC=len(pd.DataFrame(sheet10.get_all_records(),index=None))+df1_P2_Fakhra+df1_P2_Bughti

    fig = go.Figure(data=[go.Sankey(
        node = dict(
          pad = 20,
          thickness =40,
          line = dict(color = "black", width = 0.2),
          label = ["Corpus", "Glossary", "Fakhra", "Sir Bughti", "Tanveer Fatima", "Sir Nisar","Dr Rauf Parekh","Dr Rashid","Dr Rauf Parek_CD","Dr Rauf Parek_GD","Dr Rashid_CD","Dr Rashid_GD"],
          color = ["darkgoldenrod","darkgoldenrod","cadetblue","cadetblue","cadetblue","cadetblue","chocolate","chocolate","maroon","maroon","maroon","maroon"]
        ),
        link = dict(
          source = [0,0,0,0,0,1,1,2,3,4,5,6,6,7,7], # indices correspond to labels, eg A1, A2, A1, B1, ...
          target = [2,3,4,5,6,6,7,6,6,7,7,8,9,10,11],
          value = [assigned_Fakhra, assigned_Bughti,assigned_TF,assigned_NMK,assigned_RP,Glossary_1,Glossary_2,df_Fakhra,df_Bughti,df_TF,df_NMK,df_RPC,df_RPG,df_DRC,df_DRG],
          # color = ["silver","silver","silver","silver","royalblue","royalblue","darkmagenta","royalblue","royalblue","darkmagenta","darkmagenta","orange","orange","purple","purple",]
          color=[colour(),colour(),colour(),colour(),colour(),
                colour(),colour(),colour(),colour(),colour(),
                 colour(),colour(),colour(),colour(),colour()]
      ))])

    fig.update_layout(title_text="Data Preparation Flow Diagram", font_size=16,font_color="black", width=1200,height=700)
    col1,col2=st.columns([3,1])
    with col1:
      st.plotly_chart(fig)