from lxml import etree
import re

expenses=[]

class Expense:
    def __init__(self, transactionType, amount, transactionCost, total, date):
        self.transactionType= transactionType
        self.amount= amount
        self.transactionCost =transactionCost
        self.total=total

def findfile(file):
    try:
        doc = etree.parse(file)
        root = doc.getroot()
        for  element in root.iter("sms"):
            address = element.get("address")
            if address == "MPESA":
                body = element.get("body")
                transaction = checkTypeOfTransaction(body)
                if transaction:
                    expenses.append(transaction)
    except Exception as e:
        print(f"Error reading the XML file: {e}")

xml_path = "/mnt/g/My Drive/backup/sms-20231217000653.xml"
findfile(xml_path)


def extractAmount(text,priorWord):
    try:
        words= text.split()
        index =words.index(priorWord)
        value = words[index+1]
        amount = removeCurrency(value)
        return amount
    except(ValueError, IndexError):
        return None
def extractTransactionCost(text):
    try:
        priorWord='cost'
        words =text.split()
        index= words.index(priorWord)
        value = words[index+1]
        TransactionCost = removeCurrency(value)
        return TransactionCost
    except (ValueError,IndexError):
        return None
    
def processTransactionCost(text, transactionType,priorWord):
    amount, transactionCost, totalAmount, date = extractTransactionInfo(text,priorWord)
    expense =Expense(transactionType, amount, transactionCost, totalAmount, date)

def checkTypeOfTransaction(text):
    if 'airtime' in text:
        priorWord = 'bought'
        transactionType='airtime'       
    elif 'sent' in text:
        priorWord = 'Confirmed.'
        transactionType='Send Money'
       
    elif 'paid' in text:
        priorWord ='Confirmed.'
        transactionType='Buy Goods'
    elif 'pay' in text:
        priorWord ='Confirmed.'
        transactionType='Fuliza Payment'
    elif 'received' in text:
        priorWord ='Confirmed.'
        transactionType='Receive'
    else:
        return None
    return processTransactionCost(text, transactionType, priorWord)

def extractTransactionInfo(text, priorWord):
    amount= extractAmount(text,priorWord)
    transactionCost =extractTransactionCost(text)
    totalAmount = amount + transactionCost
    date =extractDate(text)
    return amount, transactionCost, totalAmount, date



def removeCurrency(value):
    match = re.search(r"\d+", value)
    if match:
        return int(match.group())
    else:
        return None
    
def extractDate(text):
    try:
        words=text.split()
        priorWord='on'
        index =words.index(priorWord)
        date = words[index+1]
    except(ValueError, IndexError):
        return None

        