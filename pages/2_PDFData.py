import streamlit as st 
import pandas as pd
from expensePackage.pdfDataExtractor import readPDF
import plotly.express as px
def main():
    st.title('PesaPulse')
    st.markdown(
        """
        ### Instructions:
        -To review your transactions and expenses from your Mpesa Statements, just upload your financial statement from [Safaricom](https://www.safaricom.co.ke/personal/m-pesa/do-more-with-m-pesa/m-pesa-statement)

        -Once uploaded, the tool automatically extracts and displays your transactions
        
        -Download the transaction data for convenient use in your preferred spreadsheet application.
        
        """
    )
    pdf_path = st.file_uploader("Upload your financial statement", type=['pdf'])
    if pdf_path is not None:
        df = readPDF(pdf_path)
        df['PAID OUT'] = df['PAID OUT'].str.replace(',','')
        st.write(df)

        pieChart=px.pie(df,values='PAID OUT',names='TRANSACTION TYPE', title='Transaction Pie Chart')
        st.plotly_chart(pieChart, use_container_width=True)

if __name__ == "__main__":
    main()
