from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st


with st.echo(code_location='below'):
    total_points = st.slider("Voltage", 1, 50, 200)
    num_turns = st.slider("Current", 1, 100, 9) 
    Point = namedtuple('Point', 'x y') 
    data = []
    resistance = total_points / num_turns
    for curr_point_num in range(total_points):
        x = total_points
        y = num_turns
        data.append(Point(x, y))
        
    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
                    .encode(x='x:Q', y='y:Q'))
