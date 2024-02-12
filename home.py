import streamlit as st 
from st_pages import Page, Section, show_pages, add_page_title


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
        - **Track your Expenses and Income📊**

        Start managing your finances effortlessly with PesaPulse! 💰
        """
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.link_button("Use Mpesa Messages💬", url = "/Use Mpesa Messages")
    with col2:
        st.link_button("Use Mpesa Statements🧾", url = "/Use Mpesa Statements")
    with col3:
        st.link_button("Track your Expenses 📊", url = "/Expense Tracker")
    
    

st.set_page_config(
    page_title="PesaPulse",
    page_icon="💲",
)
if __name__ == "__main__":
    main()

show_pages(
    [
        Page("home.py", "Home", "🏠"),
        Section("Track Mpesa Transactions"),
        Page("pages/1_xmlData.py", "Use Mpesa Messages", "💬"),
        Page("pages/2_PDFData.py", "Use Mpesa Statements", "🧾"),
        Section("Track Expenses"),
        Page("pages/3_trackExpense.py", "Expense Tracker", "📊"),

    ]
)
