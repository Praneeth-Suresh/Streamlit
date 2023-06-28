import streamlit as st
import pandas as pd
import numpy as np
import time
import tensorflow as tf

# The following code creates a static table

st.markdown("# Handeling outputs")
st.sidebar.success("Choose a page from above")

@st.cache_data
def GetTensor():
  return tf.random.normal([4, 3]) * 10

t1 = GetTensor()

st.table(t1)

# The following code creates an interactive table woth a highlight

df = pd.DataFrame(t1)

st.dataframe(df.style.highlight_min(axis=0))

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# The following makes a map

points = pd.DataFrame({
  'LAT': [1.365298],
  'LON': [103.749390]
})

st.map(points)

