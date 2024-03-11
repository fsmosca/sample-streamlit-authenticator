import streamlit as st
from streamlit import session_state as ss
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from modules.nav import MenuButtons


CONFIG_FILENAME = 'config.yaml'

if 'is_register' not in ss:
    ss.is_register = False


with open(CONFIG_FILENAME) as file:
    config = yaml.load(file, Loader=SafeLoader)


def add_role(username_to_add_role, new_role='user'):
    """Append role to the config file.

    In the registration widget, there is a role selectbox. This is added
    because streamlit-authenticator does not support it.
    """
    with open(CONFIG_FILENAME) as file:
        config = yaml.load(file, Loader=SafeLoader)

    # Check if the necessary keys exist before modifying the config
    if 'credentials' in config and 'usernames' in config['credentials'] and username_to_add_role in config['credentials']['usernames']:
        config['credentials']['usernames'][username_to_add_role]['role'] = new_role

        with open(CONFIG_FILENAME, 'w') as file:
            yaml.dump(config, file, default_flow_style=False)


def get_roles():
    """Gets user roles based on config file."""
    with open(CONFIG_FILENAME) as file:
        config = yaml.load(file, Loader=SafeLoader)

    if config is not None:
        cred = config['credentials']
    else:
        cred = {}

    return {username: user_info['role'] for username, user_info in cred['usernames'].items() if 'role' in user_info}


st.header('Account page')


authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

login_tab, register_tab = st.tabs(['Login', 'Register'])

with login_tab:
    authenticator.login(location='main')

    if ss["authentication_status"]:
        authenticator.logout(location='main')    
        st.write(f'Welcome *{ss["name"]}*')

    elif ss["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif ss["authentication_status"] is None:
        st.warning('Please enter your username and password')

with register_tab:
    if not ss["authentication_status"]:

        # Adds custom role.
        st.selectbox(':green[Role]', options=['user', 'admin'], key='role')
        try:
            email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(preauthorization=False)
            if email_of_registered_user:
                st.success('User registered successfully')
                ss.is_register = True
        except Exception as e:
            st.error(e)

# We call below code in case of registration, reset password, etc.
with open(CONFIG_FILENAME, 'w') as file:
    yaml.dump(config, file, default_flow_style=False)

if ss.is_register:
    ss.is_register = False
    add_role(username_of_registered_user, ss.role)

# Call this late because we show the page navigator depending on who logged in.
MenuButtons(get_roles())
