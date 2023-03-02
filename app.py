import streamlit as st
import pandas as pd
import numpy as np
import json
import plotly.graph_objects as go
dfA = pd.read_csv("full-huf.csv")
st.title('HUF Duplicates')
number = st.number_input('Move the index up or down to see different matches', value=0)
st.write('Index', number)
with open("full_match.json", "r") as fp:
    matches = json.load(fp)

# fig = go.Figure(data=[go.Table(
#     header=dict(values=list(dfA.columns),
#                 fill_color='paleturquoise',
#                 align='left'),
#     cells=dict(values=dfA.iloc[[x for x in matches[number]]].transpose().values.tolist(),
#                fill_color='lavender',
#                align='left'))
# ])

# st.write(fig)

st.dataframe(dfA.iloc[[x for x in matches[number]]], width=1500, height=1000)



