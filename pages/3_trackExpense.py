import streamlit as st
import calendar 
from datetime import datetime

incomes = ['Salary', 'Other Income']
expenses =['Rent','Utilities', 'Groceries','Fuel/Transport', 'Saving', 'Miscellanous']
page_title = 'Income and Expense Manager'
#TODO add page icon

years = [datetime.today().year, datetime.today().year + 1]
months = list(calendar.month_name[1:])
