import numpy as np
import pandas as pd
import streamlit as st

DATE_COLUMN = "date/time"

st.title("Synthetic NYC pickups")
st.caption("Generated example data, not real trips.")

@st.cache_data
def load_data():
    rng = np.random.default_rng(42)
    return pd.DataFrame({
        DATE_COLUMN: pd.date_range("2025-01-01", periods=480, freq="7min"),
        "lat": rng.uniform(40.71, 40.78, size=480),
        "lon": rng.uniform(-74.02, -73.95, size=480),
    })

data = load_data()
if st.checkbox("Show sample data"):
    st.dataframe(data)

st.subheader("Pickups by hour")
hist = data[DATE_COLUMN].dt.hour.value_counts().reindex(range(24), fill_value=0)
hist.index.name = "Hour"
st.bar_chart(hist)

hour = st.slider("Hour of the day", 0, 23, 17)
points = data.loc[data[DATE_COLUMN].dt.hour == hour, ["lat", "lon"]]
st.subheader(f"Pickups at {hour:02d}:00")
st.map(points)
