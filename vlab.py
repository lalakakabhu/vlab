import streamlit as st
import plotly.graph_objs as go
import numpy as np

st.title("Plotly examples")

st.header("Chart with two lines")

trace0 = go.Scatter(x=[1, 2, 3, 4], y=[10, 15, 13, 17])
trace1 = go.Scatter(x=[1, 2, 3, 4], y=[16, 5, 11, 9])
data = [trace0, trace1]
st.write(data)
