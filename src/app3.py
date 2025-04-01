import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plost

df_raw = pd.read_csv('../data/raw/coffee.csv')

df_baking = df_raw.copy()
df_baking = df_raw.copy()    
var = ['total_cup_points', 'species', 'country_of_origin','aroma', 'flavor','aftertaste', 'acidity', 'body', 'balance', 'uniformity', 'clean_cup',
       'sweetness', 'cupper_points', 'moisture']
df =  df_baking[var]

st.title('Coffe Data Set Navigator')

st. text('Information that you would like to show to your audience')
st.markdown('**Streamlit** is a good **tool**')
st.dataframe(df)

df_describe = df.describe(include='number').T
st.dataframe(df_describe)


plost.line_chart(df,
  x='total_cup_points'
  y=('species', 'country_of_origin'),  # 👈 This is magic!
)
