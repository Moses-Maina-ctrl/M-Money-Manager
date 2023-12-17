from lxml import etree
import re

def findfile(file):
    try:
        doc = etree.parse(file)
        root = doc.getroot()
        for  element in root.iter("sms"):
            address = element.get("address")
            if address == "MPESA":
                body = element.get("body")
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
    except(ValueError, IndexError):
        return None

def extractTransactionCost(text):
    

def checkTypeOfTransaction(text):


def removeCurrency(value):
    match = re.search(r"\d+", value)
    if match:
        return int(match.group())
    else:
        return None
        