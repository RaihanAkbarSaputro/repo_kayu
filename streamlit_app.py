import streamlit as st
import os

def show_folder_contents(folder_path):
    st.write(f"Isi folder {folder_path}:")
    folder_contents = os.listdir(folder_path)
    for item in folder_contents:
        st.write(item)

def main():
    st.title("Penjelajah Folder")

    # Input untuk memasukkan jalur folder
    folder_path = st.text_input("Masukkan jalur folder:", "/")
    if st.button("Cek Folder"):
        if os.path.exists(folder_path):
            show_folder_contents(folder_path)
        else:
            st.error("Folder tidak ditemukan.")

if __name__ == "__main__":
    main()
