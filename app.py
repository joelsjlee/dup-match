import streamlit as st
import pandas as pd
import numpy as np
import json
dfA = pd.read_csv("full-huf.csv")
st.title('HUF Duplicates')
st.write('Out of 54023 entries (Published, all events, newspapers with coverage) there are 1781 known articles where there exists at least two identical copies. Out of these 1781 article duplicates, there are 4313 known entries, because some articles (ex. type in 5. One article but 6 duplicate entries) there exists many duplicate copies.')
number = st.number_input('Change the index from 0 to 1780 see different matches.', value=0)
st.write('Index', number)
with open("full_match.json", "r") as fp:
    matches = json.load(fp)
st.dataframe(dfA.iloc[[x for x in matches[number]]])



