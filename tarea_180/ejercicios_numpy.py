#!/usr/bin/env python
# coding: utf-8

# ------------------------------------------------------------------------------------------------------<br>
# <h3 style="background:#87a1c2; color:#ffffff; padding:20px; border-radius:5px;">✍ EJERCICIOS NUMPY PARA @EGGERS</h3><br>
# ------------------------------------------------------------------------------------------------------<br>

# 1. Crea un vector entre 7 y 66.
# 2. Invierte el vector generado anteriormente.
# 3. Matriz de 4x4 con valores entre 0 y 15.
# 5. Crea la matriz identidad de 5x5.
# 6. Crea una matriz de 5x5 donde la posición central y todas las posiciones que conforman el marco valgan 1 y el resto 0.
# 7. Matriz de 4x4 donde cada fila valga entre 3 y 0. Valores in crescendo.
# 8. Crea un array de ceros de 2x7.
# 9. Crea un array de ceros de 5x4 excepto toda la primera fila que valga 1.
# 10. Crea un array que represente una tabla de ajedrez. Negras 1 y blancas 0.

# In[3]:


import numpy as np
vector=np.arange(7,67,dtype=int)
vector


# In[8]:


vector[::-1]


# In[6]:


matriz=np.arange(0,16,dtype=int)
matriz2=np.reshape(matriz, (4, 4))
matriz2


# In[51]:


np.identity(5,dtype=int)


# In[52]:


matriz_central_5x5=np.ones([5,5],dtype=int)
matriz_central_5x5[1::2,1:4]=0
matriz_central_5x5[2,1::2]=0
matriz_central_5x5


# In[53]:


matriz_crescendo=np.zeros([4,4],dtype=int)
matriz_crescendo[::,1]=1
matriz_crescendo[::,2]=2
matriz_crescendo[::,3]=3
matriz_crescendo


# In[54]:


np.zeros((2,7),dtype=int)


# In[56]:


matriz=np.zeros([5,4],dtype=int)
matriz[0,::]=1
matriz


# In[58]:


ajedrez=np.zeros([8,8],dtype=int)
ajedrez[::2,0::2]=1
ajedrez[1::2,1::2]=1
ajedrez

