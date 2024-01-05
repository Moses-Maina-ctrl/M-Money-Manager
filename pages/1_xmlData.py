import streamlit as st 
import pandas as pd
import numpy as np
from expensePackage.xmlDataExtractor import findfile
import datetime
import plotly.express as px

def main():
    st.title('PesaPulse')
    st.markdown(
        """
        This tool  uses the SMS Backup & Restore app available on [Google Play](https://play.google.com/store/apps/details?id=com.riteshsahu.SMSBackupRestore&hl=en_US).
        ### Instructions:
        -To review your transactions and expenses from your Mpesa Messages, just upload the message backup using the SMS Backup & Restore App

        -Once uploaded, the tool automatically extracts and displays your transactions

        -Download the transaction data for convenient use in your preferred spreadsheet application.
        
        """
    )
    xml_path = st.file_uploader("Upload XML file", type=['xml'])

    if xml_path is not None:
        
        st.subheader('Transactions:')
        currentYear = datetime.datetime.now().year
        currentMonth = datetime.datetime.now().month
        currentDay = datetime.datetime.now().day
        col1, col2 = st.columns(2)
        with col1:
            beginningDate = st.date_input("From: ", datetime.date(currentYear, currentMonth, 1))
        with col2:
            endDate = st.date_input("To: ", datetime.date(currentYear, currentMonth, currentDay))
        df=findfile(xml_path)
        df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
        df[['amount', 'transactionCost']] = df[['amount','transactionCost']].fillna(0)
        beginningDate = pd.to_datetime(beginningDate)
        endDate = pd.to_datetime(endDate)
        df['Total'] = df['amount'] +df['transactionCost']
        monthlyTransactions = df[(df['date'] >= beginningDate) & (df['date'] <= endDate)]
        if not monthlyTransactions.empty:

            st.write(monthlyTransactions)
            
        #Airtime = df.loc[df['transactionType'=='Airtime',]]
            total_by_transaction_type = monthlyTransactions.groupby('transactionType')['Total'].sum().reset_index()
            st.write(total_by_transaction_type)

            pieChart= px.pie(total_by_transaction_type, values='Total', names='transactionType', title='Transaction Pie Chart')
            
            st.plotly_chart(pieChart, use_container_width=True)
            

            st.subheader('Transaction Chart')
            st.bar_chart(total_by_transaction_type.set_index('transactionType')['Total'])
            
        else:
            st.warning("No M-Pesa messages found for the selected dates!😢")

st.set_page_config(
    page_title= "Mpesa Messages",
)
if __name__ == "__main__":
    main()
        