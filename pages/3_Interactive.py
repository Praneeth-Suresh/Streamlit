import streamlit as st
import pandas as pd
import time
import numpy as np

st.markdown("# Let's move on to making the page interactive")
st.sidebar.markdown("# Interactive page")

x = st.slider('x', min_value=0., max_value=10., step=0.00001)  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.text_input("Your name", key="name") # Can alternatively be written as: name = st.text_input("Your name")

st.session_state.name

st.write("Now lets do checkboxes")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']) # SInce this is random generationa and since the whole code is re-run, the data in the table will update each time the checkbox is checked

if st.checkbox('Show dataframe'):
    chart_data

st.write("How about selectboxes?")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column']) # Crtees a drop down

st.write('You selected: ', option, 'whose square is ', option ** 2)

