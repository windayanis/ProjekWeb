import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import streamlit as st

def aes():
    plaintext = st.text_area("Masukkan PlainText/CipherText ")
    key = st.text_input("Masukkan Key")
    col1,col2,col3 = st.columns([10,1,1])
    BS = 16
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    unpad = lambda s : s[:-ord(s[len(s)-1:])]
    with col2:
        if st.button("Enkrip"):
            if len(plaintext) == 0:
                with col1:
                    st.error("Masukkan Text!")
            else:
                p_key = hashlib.sha256(key.encode("utf-8")).digest()
                raw = pad(plaintext)
                iv = Random.new().read(AES.block_size)
                cipher = AES.new(p_key, AES.MODE_CBC, iv)
                hasil = base64.b64encode(iv + cipher.encrypt(raw.encode()))
                with col1:
                    st.info(bytes.decode(hasil)) 
    with col3:
        try:
            if st.button("Dekrip"):          
                inputan = plaintext
                if len(inputan) == 0:
                    with col1:
                        st.error("Masukkan Text!")
                else:
                    p_key = hashlib.sha256(key.encode("utf-8")).digest()
                    plaintext = base64.b64decode(plaintext)
                    iv = plaintext[:BS]
                    cipher = AES.new(p_key, AES.MODE_CBC, iv)
                    hasil = unpad(cipher.decrypt(plaintext[BS:]))
                    with col1:
                        st.info(bytes.decode(hasil))
        except:
                with col1:
                    st.error("Kesalahan Input")

    with st.container():
        st.text("")
        st.header("Apa itu AES?")
        st.write("""
        AES (Advanced Encryption Standard) atau Standar Enkripsi Lanjutan merupakan standar enkripsi dengan kunci simetris yang diadopsi oleh Pemerintah Amerika Serikat. Standar ini terdiri dari tiga penyandian blok, yaitu AES-128, AES-192, dan AES-256. Tiap-tiap penyandian memiliki ukuran blok 128 bit dengan ukuran kunci masing-masing 128, 192, dan 256 bit. AES telah dianalisis secara luas dan sekarang digunakan di seluruh dunia, 
        seperti halnya dengan pendahulunya, Standar Enkripsi Data (DES).
        """)
