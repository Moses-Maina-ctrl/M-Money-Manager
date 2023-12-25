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
        beginningDate = pd.to_datetime(beginningDate)
        endDate = pd.to_datetime(endDate)
        monthlyTransactions = df[(df['date'] >= beginningDate) & (df['date'] <= endDate)]
        # TODO change beginningDate and EndDate to datetime object
        st.write(monthlyTransactions)
        df['tr']
if __name__ == "__main__":
    main()
        