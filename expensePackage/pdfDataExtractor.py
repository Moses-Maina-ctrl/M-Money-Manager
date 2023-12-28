from tabula import read_pdf

def readPDF(text):
    dfs = read_pdf(text)
    tablez =len(dfs)
    df = dfs[0]
    return df
    