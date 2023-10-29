import streamlit as st
import pyqrcode 
from PIL import Image

n = st.text_input("", placeholder="Enter your name")
a = st.text_input("", placeholder="Enter your age")
m = st.text_input("", placeholder="Enter your address")
mo = st.text_input("", placeholder="Enter your mobile number")
abc = st.button("Submit")

if abc:
    # Create the QR code
    data = f"name:{n}, age:{a} , address:{m} , mobile number:{mo}"
    url = pyqrcode.create(data)

    # Save the QR code to a file
    url.png('myqr.png', scale=6)

    # Display the QR code image
    img = Image.open('myqr.png')
    st.image(img, caption='QR Code', use_column_width=True)
