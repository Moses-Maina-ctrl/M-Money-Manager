import streamlit as st 
import pandas as pd
import numpy as np
from expensePackage.xmlDataExtractor import findfile
import datetime


def main():
    st.title('PesaPulse')
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
        st.write(monthlyTransactions)
       #Airtime = df.loc[df['transactionType'=='Airtime',]]
        total_by_transaction_type = monthlyTransactions.groupby('transactionType')['Total'].sum().reset_index()

        st.write(total_by_transaction_type)
        st.subheader('Transaction Chart')
        st.bar_chart(total_by_transaction_type.set_index('transactionType')['Total'])

st.set_page_config(
    page_title= "Mpesa Messages",
)
if __name__ == "__main__":
    main()
        