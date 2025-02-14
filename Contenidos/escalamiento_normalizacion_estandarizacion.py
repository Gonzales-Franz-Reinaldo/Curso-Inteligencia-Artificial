# -*- coding: utf-8 -*-
"""Escalamiento_Normalizacion_Estandarizacion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NDo-rDazRjE_zoqf_wt6U79sbrSK3OL_
"""

# Escala, Normaliza & Estandariza
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing

datos = pd.read_csv('/content/datos_personas.csv')
datos

# =======================================================================================================

# Graficando los datos en escala original
fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)

ax1.set_title('Datos Originales Juntos')
ax1.plot(datos)
ax2.set_title('Ingreso')
ax2.plot(datos['ingreso'], linewidth=0, marker='*', color='blue', markersize=6)
ax3.set_title('Carros')
ax3.plot(datos['carros'], linewidth=0, marker='+', color='orange', markersize=16)
plt.show()

# =======================================================================================================

# Distribución de los datos originales
fig = plt.figure(figsize=(8, 8))
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

ax1.set_title('Ingreso')
ax1.plot(datos['ingreso'], linewidth=0, marker='o', color='blue', markersize=6)
ax2.set_title('Carros')
ax2.plot  (datos['carros'], linewidth=0, marker='+', color='orange', markersize=16)
ax3.set_title('Ingreso')
ax3.hist(datos['ingreso'], bins=100, color='blue')
ax4.set_title('Carros')
ax4.hist(datos['carros'], color='orange')
plt.show()

# =======================================================================================================

# Escala en función del mínimo y máximo
datos_min_max = preprocessing.MinMaxScaler().fit_transform(datos)

datos_min_max

# =======================================================================================================

# Normaliza en función de la Norma del Vector
datos_normalizer = preprocessing.Normalizer().transform(datos.T)
datos_normalizer = datos_normalizer.T
# normalizado = x / raiz_cuadrada(x_1^2 + x_2^2 + x_3^2 + ...)

datos_normalizer

# =======================================================================================================

# Estandarización (desv_std = 1, media = 0)
datos_standard_scaler = preprocessing.StandardScaler().fit_transform(datos)
# estandarización = (X - media) / std

datos_robust_scaler = preprocessing.RobustScaler().fit_transform(datos)
# estandarizado = (X - rango_intercuartílico) / std

datos_standard_scaler, datos_robust_scaler

# =======================================================================================================

# Columna 'ingreso': Comparación de métodos

# convierte vectores de numpy a DataFrames para graficarlos
datos_min_max = pd.DataFrame(datos_min_max, columns=['ingreso', 'carros'])
datos_normalizer = pd.DataFrame(datos_normalizer, columns=['ingreso', 'carros'])
datos_standard_scaler = pd.DataFrame(datos_standard_scaler, columns=['ingreso', 'carros'])
datos_robust_scaler = pd.DataFrame(datos_robust_scaler, columns=['ingreso', 'carros'])

# crea una figura con 5 subfiguras para comparar los métodos
fig = plt.figure(figsize=(15, 3))
ax1 = fig.add_subplot(1, 5, 1)
ax2 = fig.add_subplot(1, 5, 2)
ax3 = fig.add_subplot(1, 5, 3)
ax4 = fig.add_subplot(1, 5, 4)
ax5 = fig.add_subplot(1, 5, 5)

# crea y personaliza series de datos
ax1.set_title('INGRESOS')
ax1.plot(datos['ingreso'], linewidth=0, marker='*', color='red', markersize=4)

ax2.set_title('Min Max')
ax2.plot(datos_min_max['ingreso'], linewidth=0, marker='*', color='red', markersize=4)

ax3.set_title('Normalizer')
ax3.plot(datos_normalizer['ingreso'], linewidth=0, marker='*', color='red', markersize=4)
ax3.set_ylim(0, 1)

ax4.set_title('Standard Scaler')
ax4.plot(datos_standard_scaler['ingreso'], linewidth=0, marker='*', color='red', markersize=4)

ax5.set_title('Robust Scaler')
ax5.plot(datos_robust_scaler['ingreso'], linewidth=0, marker='*', color='red', markersize=4)

plt.show()


# crea una figura con 5 subfiguras para mostrar histogramas
fig = plt.figure(figsize=(15, 3))
ax1 = fig.add_subplot(1, 5, 1)
ax2 = fig.add_subplot(1, 5, 2)
ax3 = fig.add_subplot(1, 5, 3)
ax4 = fig.add_subplot(1, 5, 4)
ax5 = fig.add_subplot(1, 5, 5)

# crea y personaliza series de datos de los histogramas
ax1.set_title('INGRESOS')
ax1.hist(datos['ingreso'], color='red', bins=100)

ax2.set_title('Min Max')
ax2.hist(datos_min_max['ingreso'], color='red', bins=100)

ax3.set_title('Normalizer')
ax3.hist(datos_normalizer['ingreso'], color='red', bins=100)
# ax3.set_ylim(0, 1)

ax4.set_title('Standard Scaler')
ax4.hist(datos_standard_scaler['ingreso'], color='red', bins=100)

ax5.set_title('Robust Scaler')
ax5.hist(datos_robust_scaler['ingreso'], color='red', bins=100)

plt.show()

# =======================================================================================================

# Columna 'carros': Comparación de métodos

# crea una figura con 5 subfiguras para comparar los métodos
fig = plt.figure(figsize=(15, 3))
ax1 = fig.add_subplot(1, 5, 1)
ax2 = fig.add_subplot(1, 5, 2)
ax3 = fig.add_subplot(1, 5, 3)
ax4 = fig.add_subplot(1, 5, 4)
ax5 = fig.add_subplot(1, 5, 5)

# crea y personaliza series de datos
ax1.set_title('CARROS')
ax1.plot(datos['carros'], linewidth=0, marker='*', color='blue', markersize=4)

ax2.set_title('Min Max')
ax2.plot(datos_min_max['carros'], linewidth=0, marker='*', color='blue', markersize=4)

ax3.set_title('Normalizer')
ax3.plot(datos_normalizer['carros'], linewidth=0, marker='*', color='blue', markersize=4)
ax3.set_ylim(0, 1)

ax4.set_title('Standard Scaler')
ax4.plot(datos_standard_scaler['carros'], linewidth=0, marker='*', color='blue', markersize=4)

ax5.set_title('Robust Scaler')
ax5.plot(datos_robust_scaler['carros'], linewidth=0, marker='*', color='blue', markersize=4)

plt.show()


# crea una figura con 5 subfiguras para mostrar histogramas
fig = plt.figure(figsize=(15, 3))
ax1 = fig.add_subplot(1, 5, 1)
ax2 = fig.add_subplot(1, 5, 2)
ax3 = fig.add_subplot(1, 5, 3)
ax4 = fig.add_subplot(1, 5, 4)
ax5 = fig.add_subplot(1, 5, 5)

# crea y personaliza series de datos de los histogramas
ax1.set_title('CARROS')
ax1.hist(datos['carros'], color='blue')

ax2.set_title('Min Max')
ax2.hist(datos_min_max['carros'], color='blue')

ax3.set_title('Normalizer')
ax3.hist(datos_normalizer['carros'], color='blue')
# ax3.set_ylim(0, 1)

ax4.set_title('Standard Scaler')
ax4.hist(datos_standard_scaler['carros'], color='blue')

ax5.set_title('Robust Scaler')
ax5.hist(datos_robust_scaler['carros'], color='blue')

plt.show()