# -*- coding: utf-8 -*-
"""Prácticas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NDo-rDazRjE_zoqf_wt6U79sbrSK3OL_
"""

# Reto 1
# Crear una lista de listas llamada nueva _ lista que contenga 3 registros de 3 registros cada uno
# (el contenido no importa). Imprimir el segundo valor del segundo registro.

nueva_lista = [
    ['a', 'c', 'd'],
    ['e', 'f', 'g'],
    ['h', 'i', 'j']
]

print(nueva_lista[1][1])

# Reto 2
# Crear una lista de diccionarios con tres diccionarios, donde cada diccionario registre los valores para curso, inscritos y aprobados
# Luego imprimir:
# • la cantidad de inscritos en el tercer registro
# • la cantidad de aprobados en el último registro

lista_diccionario = [
    {
        'curso': 5,
        'inscritos': 10,
        'aprobados': 20
    },
    {
        'curso': 6,
        'inscritos': 20,
        'aprobados': 50
    },
    {
        'curso': 8,
        'inscritos': 30,
        'aprobados': 50
    }
]

print(lista_diccionario[2]['inscritos'])
print(lista_diccionario[2]['aprobados'])

# Datos categóricos
nombres = ['Juan', 'Pedro', 'Carlos', 'Marcelo', 'Maria']
correlativo = [23, 45, 2, 4, 5]

# Datos continuos
altura = [2.3, 4.5, 1.5, 3.2, 1.7]

# Crear un diccionario de listas para almacenar datos categóricos y continuos
estructura = {
    'nombres' : nombres,
    'correlativo' : correlativo,
    'altura' : altura
}

# print(estructura)

# Reto extra:
# Utilizando la variable "estructura", imprimir ei nombre, correlativo y altura del  cuarto registro
# Debe mostrar algo similar 'Cndq', 155, 2.9

print(estructura['nombres'][3])
print(estructura['correlativo'][3])
print(estructura['altura'][3])

# Aplicando pandas
import pandas as pd

datos = pd.DataFrame(estructura)

datos

# Para mostrar solo una columna de datos
datos['nombres']

# Para mostrar por posiciones por filas
datos.loc[2]