from tabula import read_pdf

def readPDF(text):
    df = read_pdf(text)
    print(df)