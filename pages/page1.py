import streamlit as st
from streamlit import session_state as ss
from modules.nav import MenuButtons


# If user refreshes the page, go to the main page because
# in there we have the facility to check the login status.
if 'authentication_status' not in ss:
    st.switch_page('streamlit_app.py')


MenuButtons()
st.header('Page 1')