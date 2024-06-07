import streamlit as st
import os

def main():
    st.title("List File dalam Folder")

    # Definisikan folder yang ingin Anda cek
    folder_path = "output_files/results"  # Ganti dengan path folder yang ingin Anda cek

    # Cek apakah folder tersebut ada
    if os.path.exists(folder_path):
        st.write(f"Daftar file dalam folder `{folder_path}`:")

        # Dapatkan daftar file dalam folder
        files = os.listdir(folder_path)

        # Tampilkan daftar file
        for file_name in files:
            st.write(file_name)
    else:
        st.write(f"Folder `{folder_path}` tidak ditemukan.")

if __name__ == "__main__":
    main()
