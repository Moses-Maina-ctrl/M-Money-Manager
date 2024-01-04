import streamlit as st 
import pandas as pd
from expensePackage.pdfDataExtractor import readPDF
import plotly.express as px
def main():
    st.title('PesaPulse')
    pdf_path = st.file_uploader("Upload your financial statement", type=['pdf'])
    if pdf_path is not None:
        df = readPDF(pdf_path)
        df['PAID OUT'] = df['PAID OUT'].str.replace(',','')
        st.write(df)

        pieChart=px.pie(df,values='PAID OUT',names='TRANSACTION TYPE', title='Transaction Pie Chart')
        st.plotly_chart(pieChart, use_container_width=True)

if __name__ == "__main__":
    main()