import streamlit as st 
import pandas as pd
from expensePackage.pdfDataExtractor import readPDF

def main():
    st.title('PesaPulse')
    pdf_path = st.file_uploader("Upload your financial statement", type=['pdf'])
    if pdf_path is not None:
        readPDF(pdf_path)

if __name__ == "__main__":
    main()