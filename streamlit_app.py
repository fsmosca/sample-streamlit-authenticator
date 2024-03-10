import streamlit as st
from streamlit import session_state as ss
from modules.nav import MenuButtons
from pages.login import get_roles

# If user refreshes the page, go to the login page because
# in there we have the facility to check the login status.
if 'authentication_status' not in ss:
    st.switch_page('./pages/login.py')


MenuButtons(get_roles())
st.header('Home page')


# Protected content in home page.
if ss.authentication_status:
    st.write('This content is only accessible for logged in users.')
else:
    st.write('Please log in on login page.')
