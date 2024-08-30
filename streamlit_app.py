import streamlit as st
import pandas as pd

st.title('Machine Learning App 🥽')

st.info("Testing a Machine Learning App build on Streamlit")

with st.exapnder('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df
