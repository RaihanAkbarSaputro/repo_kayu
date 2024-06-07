import streamlit as st
import os

# Function to list directory contents
def list_directory_contents(directory):
    try:
        contents = os.listdir(directory)
        return contents
    except Exception as e:
        st.error(f"Error reading directory: {e}")
        return []

# Function to display directory contents in the app
def display_directory_contents(directory):
    st.write(f"Contents of directory: {directory}")
    contents = list_directory_contents(directory)
    for item in contents:
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            st.write(f"File: {item}")
        elif os.path.isdir(item_path):
            st.write(f"Directory: {item}")

# Main function for the Streamlit app
def main():
    st.title("Directory Viewer")

    # Define the directory you want to view
    directory_to_view = st.text_input("Enter directory path:", value=".")

    # Display the contents of the specified directory
    if st.button("View Directory"):
        display_directory_contents(directory_to_view)

if __name__ == "__main__":
    main()
