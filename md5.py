import streamlit as st
import hashlib

def md_5():
    input_str = st.text_area("Masukan plain text")
    if st.button("Hash"): 
        if len(input_str) == 0:
            st.error("Masukan Text!")
        else:
            hasil = hashlib.md5(input_str.encode())
            st.info(hasil.hexdigest())
            
        