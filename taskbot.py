import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="to do list app",
    page_icon="👌"
)

st.title("to-do list")
st.sidebar.success("select a page above")


from datetime import datetime
import streamlit as st

# Function to get the date from user input
def get_date():
    date_str = st.text_input("Enter the due date (YYYY-MM-DD):")
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        return date
    except ValueError:
        st.error("Invalid date format. Please try again.")

