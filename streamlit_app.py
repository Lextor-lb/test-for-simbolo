import streamlit as st

input_number_1 = st.number_input('Insert a number_1')
input_number_2 = st.number_input('Insert a number_2')
st.write('The addition is ', input_number_1 + input_number_2)