import streamlit as st
import pandas as pd
import time
import numpy as np

st.markdown("## Moving on to layout ...")
st.sidebar.markdown("# Layout")

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

st.write(f"The sidebar tells me that you prefer to be contacted by {add_selectbox}.")

left, right = st.columns(2)

if left.button('Say hello to me here on the left!'):
  left.write('Why hello there')
else:
  left.write('Goodbye')

with right:
  chosen = st.radio(
      'Sorting hat',
      ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
  st.write(f"You are in {chosen} house!")

st.markdown("## Lets get your progress")

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Web time: {i+1 / 100}')
  bar.progress(i + 1)
  time.sleep(1 / 100)