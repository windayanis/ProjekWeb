import streamlit as st
import hashlib

def md_5():
    input_str = st.text_area("Masukan plain text")
    col1,col2 = st.columns([14,1])
    with col2:
        if st.button("Hash"): 
            if len(input_str) == 0:
                with col1:
                    st.error("Masukan Text!")
            else:
                hasil = hashlib.md5(input_str.encode())
                with col1:
                    st.info(hasil.hexdigest())
