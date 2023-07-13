import streamlit as st

import pandas as pd
import streamlit.components.v1 as components
from PIL import Image
img=Image.open('images/NWC.png')
st.set_page_config(page_title='NWC',page_icon=img)



def read_style():
    with open("design.html") as f:
        return f.read()


def read_style2():
    with open("style.css") as f:
        return st.markdown(f'<style> {f.read()} </style>',unsafe_allow_html=True)
    




with st.expander(label="Import Your File"):
    st.title('Welcome to Dashboard')
    st.subheader('import excel file: ')
    excel = st.file_uploader('Chose your file:', type='xlsx')

        





def read(file):
    x = pd.ExcelFile(file)
    sheetnames = x.sheet_names
    selected = st.selectbox(
        "Select a sheet",
        sheetnames
    )
    df = x.parse(selected)
    return df,selected

overall=st.sidebar.button("Overall")
delayed=st.sidebar.button("Delayed")
trubled=st.sidebar.button("Trubled")
suspended=st.sidebar.button("Suspended")
timeoverrun=st.sidebar.button("Timeoverrun")
withdrawn=st.sidebar.button("Withdrawn")
performance=st.sidebar.button("Performance")

if excel:
      if overall:
        x=pd.read_excel(excel,None)
        sheetnames=x.keys()
        selected = st.selectbox(
        "Select a sheet",
        sheetnames
    )
        st.write(x)
            
            
            
    if delayed:
        x = pd.ExcelFile(excel)
        st.write("Delayed")
        delayed_sheet = x.parse('المتأخر')
        st.dataframe(delayed_sheet)
    if trubled:
        x = pd.ExcelFile(excel)
        st.write("Troubled")
        trubled_sheet = x.parse('متعثر')
        st.dataframe(trubled_sheet)
    if suspended:
        x = pd.ExcelFile(excel)
        st.write("Suspended")
        suspended_sheet = x.parse('المتوقفة')
        st.dataframe(suspended_sheet)
    if timeoverrun:
        pass



read_style2()
