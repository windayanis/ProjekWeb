import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import streamlit as st

def aes():
    plaintext = st.text_area("Masukan plain text")
    key = st.text_input("Masukan key ")
    col1,col2,col3 = st.columns([10,1,1])
    BS = 16
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    unpad = lambda s : s[:-ord(s[len(s)-1:])]
    with col2:
        if st.button("Enkrip"):
            if len(plaintext) == 0:
                with col1:
                    st.error("Masukan Text!")
            else:
                p_key = hashlib.sha256(key.encode("utf-8")).digest()
                raw = pad(plaintext)
                iv = Random.new().read(AES.block_size)
                cipher = AES.new(p_key, AES.MODE_CBC, iv)
                hasil = base64.b64encode(iv + cipher.encrypt(raw.encode()))
                with col1:
                    st.info(bytes.decode(hasil)) 
    with col3:
        if st.button("Dekrip"):
            if len(plaintext) % 4 != 0:
                with col1:
                    st.error("Masukan yang benar!")
            elif len(plaintext) == 0:
                with col1:
                    st.error("Masukan Text!")
            else:
                p_key = hashlib.sha256(key.encode("utf-8")).digest()
                plaintext = base64.b64decode(plaintext)
                iv = plaintext[:BS]
                cipher = AES.new(p_key, AES.MODE_CBC, iv)
                hasil = unpad(cipher.decrypt(plaintext[BS:]))
                with col1:
                    st.info(bytes.decode(hasil))