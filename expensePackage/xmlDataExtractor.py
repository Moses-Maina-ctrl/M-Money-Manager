from lxml import etree
import re
from datetime import datetime
import pandas as pd

dateFormat = "%d/%m/%y"
expenses=[]

class Expense:
    def __init__(self, transactionType, amount, transactionCost, date):
        self.transactionType =transactionType
        self.amount= amount
        self.transactionCost =transactionCost
        self.date = date

def removeCurrency(value):
    val0=value.replace(',','')
    match = re.search(r"\d+", val0)
    if match:
        return float(match.group())
    else:
        pass
    
def extractAmount(text):
    priorWord= None
    try:
        if 'airtime' in text:
            priorWord = 'bought'
        elif 'sent' in text:
            priorWord = 'Confirmed.'
        elif 'paid' in text:
            priorWord ='Confirmed.'
        elif 'pay' in text:
            priorWord ='Ksh'
        elif 'received' in text and 'Airtime' not in text:
            priorWord ='received'
        else:
            pass
        words= text.split()
        index = words.index(priorWord)
        extractedData = words[index+1]
        amount = removeCurrency(extractedData)
        return amount
    except (ValueError, IndentationError):
        return None
    
def checkTypeOfTransaction(text):
    if 'airtime' in text:
        transactionType='Airtime'       
    elif 'sent' in text:
        transactionType='Send Money'
    elif 'paid' in text:
        transactionType='Buy Goods'
    elif 'pay' in text:
        transactionType='Fuliza Payment'
    elif 'received' in text and 'Airtime' not in text:
        transactionType='Receive'
    else:
        return None
    return transactionType
    
def extractTransactionCost(text):
    try:
        priorWord='cost,'
        words =text.split()
        index= words.index(priorWord)
        transCost = words[index+1]
        value = removeCurrency(transCost)
        return value
    except (ValueError,IndexError):
        return None

def extractDate(text):
    try:
        words=text.split()
        priorWord='on'
        index =words.index(priorWord)
        dateString = words[index+1]
        dates = datetime.strptime(dateString, dateFormat)
        dates = dates.replace(minute=0, second=0)
        date =dates.strftime("%d/%m/%Y")
        return date
    except(ValueError, IndexError):
        return None
    
def findfile(file):
    try:
        doc = etree.parse(file)
        root = doc.getroot()
        for  element in root.iter("sms"):
            address = element.get("address")
            if address == "MPESA":
                body = element.get("body")
                transactionType=checkTypeOfTransaction(body)
                amount= extractAmount(body)
                transactionCost= extractTransactionCost(body)
                date = extractDate(body)
                if amount is not None and transactionType is not None:
                    expense =Expense(transactionType,amount, transactionCost, date)
                    expenses.append(expense)
        if expenses:
            df = pd.DataFrame([exp.__dict__ for exp in expenses])
            return df
        else:
            print("No valid transactions found")

    except Exception as e:
        print(f"Error reading the XML file: {e}")
