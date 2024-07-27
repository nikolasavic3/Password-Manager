import streamlit as st
from password_manager import PasswordManager

pm = PasswordManager()

def main():
    st.title("Password Manager")

    # Sidebar for selecting operation
    operation = st.sidebar.selectbox(
        "Select Operation",
        ["Initialize", "Get Password", "Store Password", "Reinitialize", "Reset"]
    )

    if operation == "Initialize":
        initialize()
    elif operation == "Get Password":
        get_password()
    elif operation == "Store Password":
        store_password()
    elif operation == "Reinitialize":
        reinitialize()
    elif operation == "Reset":
        reset()

def initialize():
    st.header("Initialize Password Manager")
    master_password = st.text_input("Enter Master Password", type="password")
    if st.button("Initialize"):
        pm.initialise(master_password)
        st.success("Password Manager Initialized!")

def get_password():
    st.header("Get Password")
    master_password = st.text_input("Enter Master Password", type="password")
    address = st.text_input("Enter Address")
    if st.button("Get Password"):
        password = pm.tryToGetPassword(master_password, address)
        if password:
            st.success(f"The password for {address} is: {password}")
        else:
            st.error("Password not found or incorrect master password.")

def store_password():
    st.header("Store Password")
    master_password = st.text_input("Enter Master Password", type="password")
    address = st.text_input("Enter Address")
    password = st.text_input("Enter Password", type="password")
    if st.button("Store Password"):
        if pm.storePassword(master_password, address, password):
            st.success(f"Password stored for {address}")
        else:
            st.error("Failed to store password.")

def reinitialize():
    st.header("Reinitialize Password Manager")
    old_master_password = st.text_input("Enter Old Master Password", type="password")
    new_master_password = st.text_input("Enter New Master Password", type="password")
    if st.button("Reinitialize"):
        if pm.verifyMasterPassword(old_master_password):
            pm.initialise(new_master_password)
            st.success("Password Manager Reinitialized!")
        else:
            st.error("Incorrect old master password.")

def reset():
    st.header("Reset Password Manager")
    master_password = st.text_input("Enter Master Password", type="password")
    if st.button("Reset"):
        if pm.verifyMasterPassword(master_password):
            pm.reset()
            st.success("Password Manager Reset!")
        else:
            st.error("Incorrect master password.")

if __name__ == "__main__":
    main()