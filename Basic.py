import streamlit as st
import pandas as pd
import numpy as np

# The following code creates a static table
st.set_page_config(page_title="Welcome Streamlit", page_icon="birthday.png")

st.markdown("# Handling outputs")
st.sidebar.success("Choose a page from above")

@st.cache_data
def example_table():
  return np.random.default_rng(42).normal(0, 10, size=(4, 3))

t1 = example_table()

st.table(t1)

# The following code creates an interactive table

df = pd.DataFrame(t1)

st.dataframe(df)

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

