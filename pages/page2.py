import streamlit as st
from streamlit import session_state as ss
from modules.nav import MenuButtons
from pages.login import get_roles


# If user refreshes the page, go to the login page because
# in there we have the facility to check the login status.
if 'authentication_status' not in ss:
    st.switch_page('./pages/login.py')

MenuButtons(get_roles())
st.header('Page 2')

st.write('This page is accessible by all users including the admins.')
