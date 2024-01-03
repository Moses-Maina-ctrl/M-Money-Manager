import streamlit as st
import pandas as pd
from datetime import datetime

# Create a DataFrame to store expenses
expenses = pd.DataFrame(columns=['Date', 'Category', 'Amount'])

# Streamlit app
def main():
    st.title("💰 Expense Tracker 💸")

    # Sidebar for adding expenses
    st.sidebar.header("➕ Add Expense")
    date = st.sidebar.date_input("📅 Date", datetime.now())
    category = st.sidebar.text_input("🏷️ Category")
    amount = st.sidebar.number_input("💲 Amount", min_value=0.01, step=0.01)

    if st.sidebar.button("➕ Add Expense"):
        add_expense(date, category, amount)

    # Display expenses table
    st.header("📊 Expenses")
    st.table(expenses)

    # Display total expenses
    total_expenses = expenses['Amount'].sum()
    st.info(f"💸 Total Expenses: ${total_expenses:.2f}")

# Function to add expense to DataFrame
def add_expense(date, category, amount):
    global expenses
    new_expense = pd.DataFrame({'Date': [date], 'Category': [category], 'Amount': [amount]})
    expenses = pd.concat([expenses, new_expense], ignore_index=True)

# Run the app
if __name__ == '__main__':
    main()
