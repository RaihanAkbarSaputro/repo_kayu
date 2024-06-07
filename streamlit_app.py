import streamlit as st
import os

# Mendapatkan jalur folder tempat aplikasi Streamlit berjalan
streamlit_folder = st.__path__[0]

# Menampilkan informasi jalur folder
st.write(f"Folder Streamlit: {streamlit_folder}")

# Menampilkan isi folder
folder_contents = os.listdir(streamlit_folder)
st.write("Isi folder Streamlit:")
for item in folder_contents:
    st.write(item)
