#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


path = 'poblacion_global_2020.csv'


# # Ejercicio
# 
# Examina detenidamente el siguiente dataset y responde las siguientes preguntas:
# 
# * ¿Porqué cumple con las condiciones de Tidy Data?
# * ¿Cuál es el data point principal y cual es la meta data?
# * Si quisieramos saber más sobre los niveles educativos globales ¿Qué otras características necesitariamos para este data set?
# * ¿Qué tipo de análisis harías con este data set?

# In[3]:


df = pd.read_csv(path)

df.head()


# # Ejercicios:
# 
# Manipula el dataset, de manera que respondas las siguientes preguntas:
# 
# 1. ¿Cual es el promedio de Tasa de Fertilidad global?
# 2. ¿Que país tiene la Edad Promedio más alta y cual la más baja?
# 3. Agrupa los países por continente y obtén la mediana de la población urbana
# 4. ¿Qué otro de cálculo de interés (usando estas variables) crees pertinente para comparar la calidad de vida a nivel global? ¿Porqué?

# In[4]:


df_limpio=df[df['Tasa Fertilidad']!='N.A.']
df_limpio['Tasa Fertilidad']=df_limpio['Tasa Fertilidad'].astype('float')
print(df_limpio['Tasa Fertilidad'].mean())


# In[6]:


df_limpio=df[df['Edad Promedio']!='N.A.']
df_limpio['Edad Promedio']=df_limpio['Edad Promedio'].astype('float')
edad_min=df_limpio['Edad Promedio'].min()
edad_max=df_limpio['Edad Promedio'].max()
print(df_limpio[df_limpio['Edad Promedio']==edad_min].Pais)
print(df_limpio[df_limpio['Edad Promedio']==edad_max].Pais)


# In[8]:


df_cont=pd.read_csv('continente_pais.csv', sep=';')
df_cont
df_total = pd.merge(df_cont,df, how='right')
df_total['% Poblacion Urbaba'] = df_total['% Poblacion Urbaba'].str.replace(' %','')
df_total_sin_na=df_total[df_total['% Poblacion Urbaba']!='N.A.']
df_total_sin_na['% Poblacion Urbaba']=df_total_sin_na['% Poblacion Urbaba'].astype('float')
df_total_sin_na.groupby('Continente').median()['% Poblacion Urbaba']

