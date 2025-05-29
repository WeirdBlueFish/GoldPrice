from base import *
import streamlit as st


def show():

    prices = getPrice()

    st.title(":blue[PRICES]")

    col1, col2 = st.columns(2)

    for k in prices:
        col2.write(k)
        col2.write('⎯' * 20)
        col1.write(f':green[_{prices[k]}_]')
        col1.write('⎯' * 20)

show()
btn = st.button('refresh')

if btn:
    st.rerun()
