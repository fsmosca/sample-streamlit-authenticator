import streamlit as st
from streamlit import session_state as ss


ROLES = {'jsmith': 'admin', 'rbriggs': 'user'}


def HomeNav():
    st.sidebar.page_link("streamlit_app.py", label="Home", icon='🏠')


def Page1Nav():
    st.sidebar.page_link("pages/page1.py", label="Page 1", icon='✈️')


def Page2Nav():
    st.sidebar.page_link("pages/page2.py", label="Page 2", icon='📚')


def MenuButtons():
    if 'authentication_status' not in ss:
        ss.authentication_status = False

    # Always show the home navigator.
    HomeNav()

    # Show the other page navigators depending on the users' role.
    if ss["authentication_status"]:

        # (1) Only the admin role can access page 1 and page 2.
        # In a pre-defined ROLES, get all the usernames with admin role.
        admins = [k for k, v in ROLES.items() if v == 'admin']

        # Show page 1 if the username that logged in is an admin.
        if ss.username in admins:
            Page1Nav()

        # (2) roles with users and admin have access to page 2.
        Page2Nav()     
