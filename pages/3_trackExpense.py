import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# Initialize a DataFrame to store transactions (expenses and incomes)
transactions = pd.DataFrame(columns=['Date', 'Type', 'Category', 'Amount'])

# Streamlit app
def main():
    st.title("💰 Expense and Income Tracker 💸")

    # Date selection at the top
    current_date = st.date_input("📅 Select Month", datetime.now(), key='date_selector')
    first_day_of_month = datetime(current_date.year, current_date.month, 1)
    prev_month = first_day_of_month - relativedelta(months=1)

    if st.button("⬅️ Previous Month"):
        current_date -= relativedelta(months=1)

    if st.button("➡️ Next Month"):
        current_date += relativedelta(months=1)

    # File uploader for previous transactions
    uploaded_file = st.file_uploader("📤 Upload Previous Transactions (CSV)", type=['csv'])
    if uploaded_file is not None:
        global transactions
        previous_transactions = pd.read_csv(uploaded_file)
        transactions = pd.concat([transactions, previous_transactions], ignore_index=True)

    # Sidebar for adding transactions
    st.sidebar.header("➕ Add Transaction")
    transaction_type = st.sidebar.selectbox("Type", ['Expense', 'Income'])
    date = st.sidebar.date_input("📅 Date", datetime.now())
    category = st.sidebar.text_input("🏷️ Category")
    amount = st.sidebar.number_input("💲 Amount", min_value=0.01, step=0.01)

    if st.sidebar.button("➕ Add Transaction"):
        add_transaction(date, transaction_type, category, amount)

    # Filter transactions for the selected month
    filtered_transactions = transactions[(transactions['Date'] >= first_day_of_month) & (transactions['Date'] < first_day_of_month + relativedelta(months=1))]

    # Display transactions table
    st.header(f"📊 Transactions for {current_date.strftime('%B %Y')}")
    st.table(filtered_transactions)

    # Display total expenses and incomes
    total_expenses = filtered_transactions[filtered_transactions['Type'] == 'Expense']['Amount'].sum()
    total_incomes = filtered_transactions[filtered_transactions['Type'] == 'Income']['Amount'].sum()

    st.info(f"💸 Total Expenses: Ksh{total_expenses:.2f}")
    st.info(f"💰 Total Incomes: Ksh{total_incomes:.2f}")

    # Notice to download data
    st.warning("⚠️ Remember to download your data! Sessions are not saved, and your data will be lost when you close the browser.")

# Function to add transaction to DataFrame
def add_transaction(date, transaction_type, category, amount):
    global transactions
    new_transaction = pd.DataFrame({'Date': [date], 'Type': [transaction_type], 'Category': [category], 'Amount': [amount]})
    transactions = pd.concat([transactions, new_transaction], ignore_index=True)

# Run the app
if __name__ == '__main__':
    main()
