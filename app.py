import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
import pandas as pd
import time
from sklearn.datasets import fetch_california_housing
st.title('🏠House Price prediction using ML')

st.image('https://media1.giphy.com/media/v1.Y2lkPTZjMDliOTUyajczcTNpM294ejB0enp2YmFoMDZmeTh3bWg4bjlocTdxN2k3eGViZyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Ee1i8QNLQO0UnlKjr7/giphy.gif')
df = pd.read_csv('house_data.csv')
X = df.iloc[:,:-3]
y = df.iloc[:,-1]

st.sidebar.title('😃 Select House features ')
st.sidebar.image('https://media1.giphy.com/media/v1.Y2lkPTZjMDliOTUyajczcTNpM294ejB0enp2YmFoMDZmeTh3bWg4bjlocTdxN2k3eGViZyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Ee1i8QNLQO0UnlKjr7/giphy.gif')
all_value = []

for i in X:
  ans = st.sidebar.slider(f' Select {i} value')
  all_value.append(ans)

st.write(all_value)

