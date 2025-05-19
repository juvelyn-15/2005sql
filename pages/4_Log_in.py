import streamlit as st
from Modules import VisualHandler
VisualHandler.initial() 
import streamlit as st

# Dummy user credentials
users = {
    "student01": "password123",
    "student02": "mypassword",
    "admin": "admin123"
}

# def process_log_in(username, password):
#     try:
#         with open(".env", "w") as env_file:
#             env_file.write(f"DB_USER={username}\n")
#             env_file.write(f"DB_PASS={password}\n")
#             env_file.write(f"DB_HOST=localhost\n")
#             env_file.write(f"DB_NAME=school_management")
#         st.session_state.log = True
#     except Exception as e:
#         return f"Error : {e}"

def display_login():
    if st.session_state.log == False:
        st.title("🔐 Login")

        st.subheader("Please enter your credentials:")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):# process_log_in(username, password)
            if username in users and users[username] == password:
                    st.session_state.log = True
                    st.success(f"Welcome {username}!")
                    st.switch_page("pages/2_Dashboard.py")
            
    else:
        st.switch_page("pages/2_Dashboard.py")
display_login()
