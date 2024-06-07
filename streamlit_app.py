import os

# Fungsi untuk menampilkan struktur folder
def display_folder_structure(folder_path):
    st.write(f"### Isi folder: {folder_path}")
    with st.expander("Lihat struktur folder"):
        for root, dirs, files in os.walk(folder_path):
            if not files and not dirs:
                st.write(f"{root} (folder kosong)")
            else:
                for file_name in files:
                    st.write(os.path.join(root, file_name))
                for dir_name in dirs:
                    st.write(os.path.join(root, dir_name))

# Tentukan folder yang ingin ditelusuri
app_folder = "."  # Direktori aplikasi Streamlit

# Panggil fungsi untuk menampilkan struktur folder
display_folder_structure(app_folder)
