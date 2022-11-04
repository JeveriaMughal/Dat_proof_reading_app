import matplotlib.pyplot as plt
import plotly.express as px
from plotly import colors
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
from PIL import Image
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random

def app():
    #image=Image.open('/home/dania/Documents/NLPL/Applications/MT/frontpage.jpeg')
    #st.image(image, width=1000, use_column_width=500, clamp=False, channels="RGB", output_format="auto")
   # st.title('National Language Processing Laboratory')
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
    "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    col1,col2=st.columns([1,5])
    with col1:
   	 st.header('Phase I Stats')	 
    col3,col4=st.columns([2,2])
    creds = ServiceAccountCredentials.from_json_keyfile_name("proofreading-app-stats.json", scope)
    client = gspread.authorize(creds)
    # uploaded_file = st.file_uploader("Choose a file")
    colors=['aliceblue','purple','aliceblue','aqua','aquamarine','darkturquoise','purple']
	
    #if uploaded_file is not None:
    sheet=client.open("modified_data").get_worksheet(0)
    df = pd.DataFrame(sheet.get_all_records(),index=None)
    # print(df)
    sheet1=client.open("modified_data").get_worksheet(1)
    df1=pd.DataFrame(sheet1.get_all_records(),index=None)
    sheet5=client.open("modified_data").get_worksheet(5)
    df5=pd.DataFrame(sheet5.get_all_records(),index=None)
    sheet6=client.open("modified_data").get_worksheet(2)
    df6=pd.DataFrame(sheet6.get_all_records(),index=None)
    sheet11=client.open("modified_data").get_worksheet(7)
    df11=pd.DataFrame(sheet11.get_all_records(),index=None)
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    colour='rgb('+str(r)+','+str(g)+','+str(b)+')'
    # print(colour)
    colour1='rgb(110,43,147)'
    colour2='rgb(222,159,26)'
    # print (colour)
    Total_lines=len(df)
    Total_lines1=len(df1)
    Total_lines5=len(df5)
    Total_lines6=len(df6)
    Total_lines11=len(df11)
    fig = go.Figure(go.Bar(x=["Fakhra","Mehboob Bughti",
                              # "Dr Rauf Parekh","Dr Rashid",
                              "Tanveer Fatima","Nisar Mamakhel","Jawad"],
                            y=[Total_lines,Total_lines1,
                              # sum,Total_lines4,
                              Total_lines5,Total_lines6,Total_lines11],
                            text=[Total_lines,Total_lines1,
                              # sum,Total_lines4,
                              Total_lines5,Total_lines6,Total_lines11],
                              marker_color=colour))
    fig.update_xaxes(title='Members',title_font_size=18, rangeselector_font_family="Times New Roman",
                                                rangeselector_font_size=10)
    fig.update_yaxes(title='Total Lines Reviewed',title_font_size=18)
    with col3:
    	st.plotly_chart(fig)

   
    if df.empty:
      MEM_1=0
      MEM_7=0
    else:
      MEM_1=len(df.loc[df['status'] == "APPROVED"])
      MEM_7=len(df.loc[df['status']=="CORRECTED"])
    if df1.empty:
      MEM_2=0
      MEM_8=0
    else:
      MEM_2=len(df1.loc[df1['status']=="APPROVED"])
      MEM_8=len(df1.loc[df1['status']=="CORRECTED"])
    if df5.empty:
      MEM_6=0
      MEM_14=0
    else:
      MEM_6=len(df5.loc[df5['status']=="APPROVED"])
      MEM_14=len(df5.loc[df5['status']=="CORRECTED"])
    if df6.empty:
      MEM_15=0
      MEM_16=0
    else:
      MEM_15=len(df6.loc[df6['status']=="APPROVED"])
      MEM_16=len(df6.loc[df6['status']=="CORRECTED"])
    if df11.empty:
      MEM_17=0
      MEM_18=0
    else:
      MEM_17=len(df11.loc[df11['status']=="APPROVED"])
      MEM_18=len(df11.loc[df11['status']=="CORRECTED"])



    APPROVED=[MEM_1,MEM_2,MEM_6,MEM_15,MEM_17]
    CORRECTED=[MEM_7,MEM_8,MEM_14,MEM_16,MEM_18]
    team=['Fakhra', 'Mehboob Bughti','Tanveer Fatima','Nisar Mamakhel','Jawad']
    fig1 = go.Figure(data=[go.Bar(name='Corrected', x=team, y=CORRECTED,text=CORRECTED,marker_color=colour1),go.Bar(name='Approved', x=team, y=APPROVED,text=APPROVED,marker_color=colour2)])
    fig1.update_xaxes(title='Members',title_font_size=18, rangeselector_font_family="Times New Roman",
                                                rangeselector_font_size=10)
    fig1.update_yaxes(title='Corrected vs Approved',title_font_size=18)
  # Change the bar mode
    fig1.update_layout(barmode='stack')
    with col4:
    	st.plotly_chart(fig1)
 
    sheet2=client.open("Data_review_phase2").get_worksheet(3)
    df2=pd.DataFrame(sheet2.get_all_records(),index=None)
    sheet3=client.open("Data_review_phase2").get_worksheet(0)
    df3=pd.DataFrame(sheet3.get_all_records(),index=None)
    sheet4=client.open("Data_review_phase2").get_worksheet(1)
    df4=pd.DataFrame(sheet4.get_all_records(),index=None)
    sheet7=client.open("Data_review_phase2").get_worksheet(6)
    df7=pd.DataFrame(sheet7.get_all_records(),index=None)


    Total_lines2=len(df2)
    Total_lines3=len(df3)
    Total_lines4=len(df4)
    Total_lines7=len(df7)
    sum_RP=Total_lines2+Total_lines3+Total_lines4+Total_lines7

    
    if df2.empty:
      RP_G_A=0
      RP_G_C=0
      RP_G_S=0
      RP_G_D=0
      RP_G_P=0
    else:
      RP_G_A=len(df2.loc[df2['status']=="APPROVED"])
      RP_G_C=len(df2.loc[df2['status']=="CORRECTED"])
      RP_G_S=len(df2.loc[df2['status']=="SKIP"])
      RP_G_D=len(df2.loc[df2['status']=="DELETE"])
      RP_G_P=len(df2.loc[df2['status']=="PEND"])
    if df3.empty:
      RP_F_A=0
      RP_F_C=0
      RP_F_S=0
      RP_F_D=0
      RP_F_P=0
    else:
      RP_F_A=len(df3.loc[df3['status']=="APPROVED"])
      RP_F_C=len(df3.loc[df3['status']=="CORRECTED"])
      RP_F_S=len(df3.loc[df3['status']=="SKIP"])
      RP_F_D=len(df3.loc[df3['status']=="DELETE"])
      RP_F_P=len(df3.loc[df3['status']=="PEND"])
    if df4.empty:
      RP_B_A=0
      RP_B_C=0
      RP_B_S=0
      RP_B_D=0
      RP_B_P=0
    else:
      RP_B_A=len(df4.loc[df4['status']=="APPROVED"])
      RP_B_C=len(df4.loc[df4['status']=="CORRECTED"])
      RP_B_S=len(df4.loc[df4['status']=="SKIP"])
      RP_B_D=len(df4.loc[df4['status']=="DELETE"])
      RP_B_P=len(df4.loc[df4['status']=="PEND"])
    if df7.empty:
      RP_C_A=0
      RP_C_C=0
      RP_C_S=0
      RP_C_D=0
      RP_C_P=0
    else:
      RP_C_A=len(df7.loc[df7['status']=="APPROVED"])
      RP_C_C=len(df7.loc[df7['status']=="CORRECTED"])
      RP_C_S=len(df7.loc[df7['status']=="SKIP"])
      RP_C_D=len(df7.loc[df7['status']=="DELETE"])
      RP_C_P=len(df7.loc[df7['status']=="PEND"])

    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    colour1='rgb('+str(r)+','+str(g)+','+str(b)+')'
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    colour2='rgb('+str(r)+','+str(g)+','+str(b)+')'
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    colour3='rgb('+str(r)+','+str(g)+','+str(b)+')'
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    colour4='rgb('+str(r)+','+str(g)+','+str(b)+')'
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    colour5='rgb('+str(r)+','+str(g)+','+str(b)+')'
    # MEM_9=MEM_3+MEM_4
    # MEM_13=MEM_10+MEM_11
    APPROVED_RP=  [RP_G_A,RP_F_A,RP_B_A,RP_C_A]
    CORRECTED_RP= [RP_G_C,RP_F_C,RP_B_C,RP_C_C]
    SKIP_RP=      [RP_G_S,RP_F_S,RP_B_S,RP_C_S]
    DELETE_RP=    [RP_G_D,RP_F_D,RP_B_D,RP_C_D]
    PEND_RP=      [RP_G_P,RP_F_P,RP_B_P,RP_C_P]
    corpus_RP= ['Glossary','Fakhra','Mehboob Bugti','Corpus']
    fig3 = go.Figure(data=[go.Bar(name='Corrected', 
                                   x=corpus_RP, y=CORRECTED_RP,text=CORRECTED_RP,marker_color=colour1),
                          go.Bar(name='Approved', 
                                    x=corpus_RP, y=APPROVED_RP,text=APPROVED_RP,marker_color=colour2),
                          go.Bar(name='Skipped', 
                                  x=corpus_RP, y=SKIP_RP,text=SKIP_RP,marker_color=colour3),   
                          go.Bar(name='Deleted', 
                                  x=corpus_RP, y=DELETE_RP,text=DELETE_RP,marker_color=colour4),    
                          go.Bar(name='Delayed', 
                                  x=corpus_RP, y=PEND_RP,text=PEND_RP,marker_color=colour5)])
    fig3.update_xaxes(title='Data Sets',title_font_size=18, rangeselector_font_family="Times New Roman",
                                                rangeselector_font_size=10)
    fig3.update_yaxes(title='Status',title_font_size=18)
    sheet8=client.open("Data_review_phase2").get_worksheet(4)
    df8=pd.DataFrame(sheet8.get_all_records(),index=None)
    sheet9=client.open("Data_review_phase2").get_worksheet(5)
    df9=pd.DataFrame(sheet9.get_all_records(),index=None)
    sheet10=client.open("Data_review_phase2").get_worksheet(2)
    df10=pd.DataFrame(sheet10.get_all_records(),index=None)

    Total_lines8=len(df8)
    Total_lines9=len(df9)
    Total_lines10=len(df10)
    sum_RH=Total_lines8+Total_lines9+Total_lines10
    
    if df8.empty:
      RH_G_A=0
      RH_G_C=0
      RH_G_S=0
      RH_G_D=0
      RH_G_P=0
    else:
      RH_G_A=len(df8.loc[df8['status']=="APPROVED"])
      RH_G_C=len(df8.loc[df8['status']=="CORRECTED"])
      RH_G_S=len(df8.loc[df8['status']=="SKIP"])
      RH_G_D=len(df8.loc[df8['status']=="DELETE"])
      RH_G_P=len(df8.loc[df8['status']=="PEND"])
    if df9.empty:
      RH_TF_A=0
      RH_TF_C=0
      RH_TF_S=0
      RH_TF_D=0
      RH_TF_P=0
    else:
      RH_TF_A=len(df9.loc[df9['status']=="APPROVED"])
      RH_TF_C=len(df9.loc[df9['status']=="CORRECTED"])
      RH_TF_S=len(df9.loc[df9['status']=="SKIP"])
      RH_TF_D=len(df9.loc[df9['status']=="DELETE"])
      RH_TF_P=len(df9.loc[df9['status']=="PEND"])
    if df10.empty:
      RH_NM_A=0
      RH_NM_C=0
      RH_NM_S=0
      RH_NM_D=0
      RH_NM_P=0
    else:
      RH_NM_A=len(df10.loc[df10['status']=="APPROVED"])
      RH_NM_C=len(df10.loc[df10['status']=="CORRECTED"])
      RH_NM_S=len(df10.loc[df10['status']=="SKIP"])
      RH_NM_D=len(df10.loc[df10['status']=="DELETE"])
      RH_NM_P=len(df10.loc[df10['status']=="PEND"])

    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    colour1='rgb('+str(r)+','+str(g)+','+str(b)+')'
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    colour2='rgb('+str(r)+','+str(g)+','+str(b)+')'
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    colour3='rgb('+str(r)+','+str(g)+','+str(b)+')'
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    colour4='rgb('+str(r)+','+str(g)+','+str(b)+')'
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    colour5='rgb('+str(r)+','+str(g)+','+str(b)+')'

    APPROVED_RH=  [RH_G_A,RH_TF_A,RH_NM_A]
    CORRECTED_RH= [RH_G_C,RH_TF_C,RH_NM_C]
    SKIP_RH=      [RH_G_S,RH_TF_S,RH_NM_S]
    DELETE_RH=    [RH_G_D,RH_TF_D,RH_NM_D]
    PEND_RH=      [RH_G_P,RH_TF_P,RH_NM_P]
    corpus_RH= ['Glossary','Tanveer Fatima','Nisar Mamakhel']
    fig4 = go.Figure(data=[go.Bar(name='Corrected', 
                                   x=corpus_RH, y=CORRECTED_RH,text=CORRECTED_RH,marker_color=colour1),
                          go.Bar(name='Approved', 
                                    x=corpus_RH, y=APPROVED_RH,text=APPROVED_RH,marker_color=colour2),
                          go.Bar(name='Skipped', 
                                  x=corpus_RH, y=SKIP_RH,text=SKIP_RH,marker_color=colour3),   
                          go.Bar(name='Deleted', 
                                  x=corpus_RH, y=DELETE_RH,text=DELETE_RH,marker_color=colour4),    
                          go.Bar(name='Delayed', 
                                  x=corpus_RH, y=PEND_RH,text=PEND_RH,marker_color=colour5)])
    fig4.update_xaxes(title='Data Sets',title_font_size=18, rangeselector_font_family="Times New Roman",
                                                rangeselector_font_size=10)
    fig4.update_yaxes(title='Status',title_font_size=18)
    title3="Total Lines reviewed by Prof. Dr. Rauf Parekh = "+str(sum_RP)
    fig3.update_layout(title=title3)
    title4="Total Lines reviewed Dr. Rashid Hameed = "+str(sum_RH)
    fig4.update_layout(title=title4)
    col5,col6=st.columns([1,5])
    with col5:
   	 st.header('Phase II Stats')	 
    col7,col8=st.columns([2,2])
    with col7:
      st.plotly_chart(fig3)
    with col8:
      st.plotly_chart(fig4)

   
