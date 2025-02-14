# -*- coding: utf-8 -*-
"""Datos_Entrenamiento_Validacion_Prueba.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NDo-rDazRjE_zoqf_wt6U79sbrSK3OL_
"""

# Separación de Datos
# 60% Entrenamiento, 20% Validación, 20% Prueba

import pandas as pd
from sklearn.model_selection import train_test_split

pacientes = pd.read_csv('/content/problemas_del_corazon.csv')

resto, prueba, resto_clase, prueba_clase = train_test_split(
    pacientes[['edad', 'genero', 'presion', 'colesterol', 'diabetico']],
    pacientes['cardiaco'],
    test_size=0.20
)


entrena, valida, entrena_clase, valida_clase = train_test_split(
    resto[['edad', 'genero', 'presion', 'colesterol', 'diabetico']],
    resto_clase,
    test_size=0.25
)

valida.shape[0]

