import streamlit as st
from streamlit import session_state as ss
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from modules.nav import MenuButtons


def get_roles():
    """Gets user roles based on config file."""
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    credentials = config['credentials']    
    return {username: user_info['role'] for username, user_info in credentials['usernames'].items()}


with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)


st.header('Login/out page')


authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

authenticator.login(location='main')

if ss["authentication_status"]:
    authenticator.logout(location='main')    
    st.write(f'Welcome *{ss["name"]}*')

elif ss["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif ss["authentication_status"] is None:
    st.warning('Please enter your username and password')

# We call below code in case of registration, reset password, etc.
with open('config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)

# Call this late because we show the page navigator depending on who logged in.
MenuButtons(get_roles())
