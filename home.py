import streamlit as st 



def main():
    st.title('💲PesaPulse')
    st.subheader('M-Money Manager and Expense Tracker')
    st.markdown(
        """
        Welcome to PesaPulse! 🚀

        Manage and analyze your transactions and expenses seamlessly through your Mpesa messages or financial statements. 
        Choose your preferred option below to get started:

        - **Use Mpesa Messages💬**: Analyze transactions from your text messages.
        - **Use Mpesa Financial Statements🧾**: Analyze transactions from your financial statements.

        Start managing your finances effortlessly with PesaPulse! 💰
        """
    )

    col1, col2 = st.columns(2)
    with col1:
        st.link_button("Use Mpesa Messages💬", url = "/xmlData")
    with col2:
        st.link_button("Use Mpesa Financial Statements🧾", url = "/PDFData")

st.set_page_config(
    page_title="PesaPulse",
    page_icon="💲",
)
if __name__ == "__main__":
    main()
