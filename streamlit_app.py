import streamlit as st
from streamlit import session_state as ss
from modules.nav import MenuButtons
from pages.account import get_roles

# If the user reloads or refreshes the page while still logged in,
# go to the account page to restore the login status. Note reloading
# the page changes the session id and previous state values are lost.
# What we are doing is only to relogin the user.
if 'authentication_status' not in ss:
    st.switch_page('./pages/account.py')


MenuButtons(get_roles())
st.header('Home page')


# Protected content in home page.
if ss.authentication_status:
    st.write('This content is only accessible for logged in users.')
else:
    st.write('Please log in on login page.')
