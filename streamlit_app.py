import streamlit as st
import os

# Function to list directory contents along with their sizes and handle subdirectories
def list_directory_contents(directory, level=0):
    try:
        contents = os.listdir(directory)
        content_details = []
        indent = "  " * level  # Indentation to show folder hierarchy
        for item in contents:
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                size = os.path.getsize(item_path)
                content_details.append((indent + item, 'File', size))
            elif os.path.isdir(item_path):
                content_details.append((indent + item, 'Directory', None))
                # Recursively list contents of the subdirectory
                sub_contents = list_directory_contents(item_path, level + 1)
                content_details.extend(sub_contents)
        return content_details
    except Exception as e:
        st.error(f"Error reading directory: {e}")
        return []

# Function to display directory contents in the app
def display_directory_contents(directory):
    st.write(f"Contents of directory: {directory}")
    contents = list_directory_contents(directory)
    for item, item_type, size in contents:
        if item_type == 'File':
            st.write(f"File: {item} (Size: {size} bytes)")
        elif item_type == 'Directory':
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
