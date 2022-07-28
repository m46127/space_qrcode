import streamlit as st
import qrcode
from PIL import Image


st.title('QRcode自動生成アプリ')

url = st.text_input('QRcodeを生成したいURL:')


if st.button('QRcode生成'):
    _img =qrcode.make(url)
    _img.save('qrcode.png')
    img = Image.open('qrcode.png')
    st.image(img)
