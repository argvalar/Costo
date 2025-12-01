import numpy as np
import streamlit as st
import pandas as pd

st.write(''' # Predicción del costo de una actividad''')
st.image("gasto.jpg", caption="Predicción del costo de una actividad de una persona.")

st.header('Datos')

def user_input_features():
  # Entrada
  Presupuesto = st.number_input('Presupuesto:', min_value=0, max_value=3000, value = 0, step = 1)
  Tiempo_invertido = st.number_input('Tiempo invertido en la actividad (minutos):',  min_value=0, max_value=200, value = 0, step = 1)
  Tipo = st.number_input('Tipo', min_value=0, max_value=4, value = 0, step = 1)
  Momento = st.number_input('Momento (mañana:1, tarde:2, noche:3):', min_value=0, max_value=3, value = 0, step = 1)
  No_de_personas = st.number_input('Número de personas que realizaron la actividad:', min_value=0, max_value=50, value = 0, step = 1)



  user_input_data = {'Presupuesto': Presupuesto,
                     'Tiempo invertido': Tiempo_invertido,
                     'Tipo': Tipo,
                     'Momento': Momento,
                     'No. de persona': No_de_personas
                     }

  features = pd.DataFrame(user_input_data, index=[0])

  return features

df = user_input_features()
datos =  pd.read_csv('datos.csv', encoding='latin-1')
X = datos.drop(columns='Costo')
y = datos['Costo']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=1613706)
LR = LinearRegression()
LR.fit(X_train,y_train)

b1 = LR.coef_
b0 = LR.intercept_
prediccion = b0 + b1[0]*df['Presupuesto'] + b1[1]*df['Tiempo_invertido'] + b1[2]*df['Tipo'] + b1[3]*df['Momento'] + b1[4]*df['No_de_personas']

st.subheader('Cálculo del costo de la actividad')
st.write('El costo es ', prediccion)
