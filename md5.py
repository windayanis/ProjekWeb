import streamlit as st
import hashlib

def md_5():
    input_str = st.text_area("Masukkan Plain Text")
    col1,col2 = st.columns([14,1])
    with col2:
        if st.button("Hash"): 
            if len(input_str) == 0:
                with col1:
                    st.error("Masukkan Text!")
            else:
                hasil = hashlib.md5(input_str.encode())
                with col1:
                    st.info(hasil.hexdigest())

    with st.container():
        st.text("")
        st.header("Apa itu MD5?")
        st.write("""
        MD5 adalah salah satu dari serangkaian algortima message digest yang didesain oleh Profesor Ronald Rivest dari MIT (Rivest, 1994). 
        Saat kerja analitik menunjukkan bahwa pendahulu MD5 yaitu MD4 mulai tidak aman, 
        MD5 kemudian didesain pada tahun 1991 sebagai pengganti dari MD4 (kelemahan MD4 ditemukan oleh Hans Dobbertin).
        Dalam kriptografi, MD5 (Message-Digest algortihm 5) ialah fungsi hash kriptografik yang digunakan secara luas dengan hash value 128-bit. 
        Pada standart Internet (RFC 1321), MD5 telah dimanfaatkan secara bermacam-macam pada aplikasi keamanan, dan MD5 juga umum digunakan untuk melakukan pengujian integritas sebuah file.
        """)
    
 
