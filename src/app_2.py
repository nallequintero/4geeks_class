import streamlit as st
import pickle
from pickle import load

# cargar el modelo

with open ('../models/clf_tree_model.pkl', 'rb') as file:
    model = pickle.load(file)

# diccionario classes/results

class_dict = {
    '0': 'iris setosa',
    '1': 'iris versicolor',
    '2': 'iris virginica'
}

# titulo de la aplicacion
st.title('prediccion de Iris')

# entrada de variables
sepal_length = st.slider('Sepal Length (cm)', min_value=3.0, max_value=9.0, step=0.1)
sepal_width = st.slider('Sepal Width (cm)', min_value=1.0, max_value=5.0, step=0.1)
petal_length = st.slider('Petal Length (cm)', min_value=0.1, max_value=11.0, step=0.1)
petal_width = st.slider('Petal Width (cm)', min_value=0.1, max_value=5.0, step=0.1)

# creacion boton

if st.button('Predict!!'):
    prediction = str(model.predict([[sepal_length,sepal_width,petal_length,petal_width]])[0])
    pred_class = class_dict[prediction]
    st.write('La prediccion:', pred_class)
