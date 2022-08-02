import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import aes
import base_64
import md5
import sha

st.set_page_config(page_title="Web Enkripsi",page_icon=":computer:",layout='wide')
selected = option_menu(
    menu_title=None,
    options = ["Home","AES","Base64","MD5","SHA"],
    icons = ["house","key","shield-lock","lock","shield-check"],
    menu_icon = "cast",
    default_index=0,
    orientation="horizontal",
    )

if selected == "Home":
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_q5pk6p1k.json")
    with st.container():
        st.title("Enkripsi, Dekripsi dan Hash")

    with st.container():
        st.write("---")
        st.header("Apa itu Enkripsi? :closed_lock_with_key:")
        left_column,right_column = st.columns(2)
    with left_column:
        st.write("""
        Enkripsi adalah cara mengacak data sehingga informasi tersebut hanya bisa dibaca oleh orang-orang yang memiliki aksesnya saja.
        Secara teknis, enkripsi adalah proses konversi teks biasa yang terbaca manusia (human-readable plaintext) menjadi teks yang tidak bisa dibaca dan dimengerti (incomprehensible text) yang biasa disebut ciphertext.
        Untuk bisa membacanya, dibutuhkan cryptographic key.
        """)
        st.text("")
        st.header("Apa itu Dekripsi? :unlock:")
        st.write("""
        Dekripsi adalah sebuah proses pembalikan yang mengubah teks-kode atau pesan yang tidak bisa dimengerti (ciphertext) menjadi sebuah teks-asli atau pesan yang dapat dimengerti (plaintext). 
        """)    
    with right_column:
        st_lottie(lottie_coding, height=350, key="encrypt")
    with st.container():
        left_column,right_column = st.columns([1,2])
        with left_column:
            st.text("")
            st.image("gambar/hashing.jpg")
        with right_column:
            st.text("")
            st.text("")
            st.header("Apa itu Hash? :lock:")
            st.write("""
            Hash adalah algoritma yang dipakai untuk mengubah informasi. 
            Data yang dimasukkan nantinya diolah menjadi angka, huruf, 
            atau karakter lain menjadi karakter terenkripsi tanpa mengubah ukuran. 
            Data yang terenkripsi lewat fungsi hash tak bisa lagi Anda kembalikan. Hal ini pula yang membuat algoritma tersebut dikenal sebagai One Way Function atau encryption satu arah.    
            """)
    with st.container():
        st.write("---")
        st.header("Jenis Enkripsi :mag:")
        st.text("")
    with st.container():
        st.write("""
                :one:
                Enkripsi Simetris, menggunakan satu kunci yang dibagikan oleh pengirim dan penerima dalam artian lain kunci yang sama digunakan untuk enkripsi dan dekripsi.
                
                :two:
                Enkripsi Asimetris, menggunakan dua kunci yang berbeda — tetapi terhubung secara logis
                untuk mengenkripsikan dan mendeskripsikan data. 
                Dua kunci tersebut adalah kunci publik dan pribadi. Kunci publik bisa disebarluaskan secara terbuka. Namun, kunci privat hanya diketahui oleh pemilik. 
                """)   
        st.text("")
        st.subheader("Contoh Algoritma Enkripsi :arrow_heading_down:")
        st.text("")
        st.text("")
        col1,col2,col3,col4,col5,col6 = st.columns([3,2,2,2,2,2])
        with col2:
            st.image("gambar/aes.png")
            st.subheader("AES")
        with col3:
            st.image("gambar/encoding.png")
            st.subheader("Base64")
        with col4:
            st.image("gambar/md5.png")
            st.subheader("MD5")
        with col5:
            st.image("gambar/sha.png")
            st.subheader("SHA")
if selected == "AES":
    aes.aes()
if selected == "Base64":
    base_64.base_64()
if selected == "MD5":
    md5.md_5()
if selected == "SHA":
    sha.sha()
