import streamlit as st
import base64

def base_64():
    input1 = st.text_area("Masukan string")
    col1,col2,col3 = st.columns([10,1,1])
    with col2:
        if st.button("Encode"):
            if len(input1) == 0:
                with col1:
                    st.error("Masukan Text!")
            else:
                hasil = input1.encode("ascii")
                base64_bytes = base64.b64encode(hasil)
                base64_string = base64_bytes.decode("ascii")
                st.text("")
                with col1:
                    st.info(base64_string)
    with col3:
        if st.button("Decode"):
            #a = input1 + '=' * (4 - len(input1) % 4)
            if len(input1) % 4 != 0:
                with col1:
                    st.error("Masukan yang benar!")
            elif len(input1) == 0:
                with col1:
                    st.error("Masukan Text!")
            else:
                hasil = input1.encode("ascii")
                sample_string_bytes = base64.b64decode(hasil)
                sample_string = sample_string_bytes.decode("ascii")
                with col1:
                    st.info(sample_string)