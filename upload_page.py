import streamlit as st


# Streamlit UI for upload
def app(email):
    st.title("Upload Page")

    st.write(f"Welcome, {email}!")

    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file:
        st.success(f"File '{uploaded_file.name}' uploaded successfully.")


if __name__ == "__main__":
    app("test@example.com")  # Replace with an actual email for testing
