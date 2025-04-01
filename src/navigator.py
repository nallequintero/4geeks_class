import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_raw = pd.read_excel('../data/raw/concrete_data.xls')

df_baking = df_raw.copy()
df_baking.columns = ['cement', 'blast_furnace_slag', 'fly_ash', 'water', 'superplasticizer', 'coarse_aggregate', 'fine_aggregate', 'age', 'compressive_strength']
df = df_baking.copy()

st.title('Concrete Data Set Navigator')

st. text('Information that you would like to show to your audience')
st.markdown('**Streamlit** is a good **tool**')
st.dataframe(df)

plt.figure(figsize=(8,8))
plt.scatter(x=df['cement'], y=df['compressive_strength'])
plt.title('Compressive strength vs concrete density')
st.pyplot(plt)

