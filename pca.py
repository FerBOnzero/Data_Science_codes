# Método de matriz de covarianza
import numpy as np
import pandas as pd

import numpy as np

def pca_covariance(data, k): 
    '''
    Función para calcular los componentes principales de un conjunto de datos por método de matriz de covarianza
    --------------------------------
    data: datos a calcular pca
    k: Número de parámteros
    '''
    # Paso 1: Centrar los datos (restar la media)
    mean = np.mean(data, axis=0)
    centered_data = data - mean

    # Paso 2: Calcular la matriz de covarianza parcial
    partial_covariance = data.T@data

    # Paso 3: Calcular los primeros k autovalores y autovectores
    eigenvalues, eigenvectors = np.linalg.eigh(partial_covariance)

    # Ordenar los autovalores y autovectores en orden descendente
    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[sorted_indices]
    eigenvectors = eigenvectors[:, sorted_indices]

    # Paso 4: Proyectar los datos en el nuevo espacio de características
    principal_components = eigenvectors

    reduced_data = np.matmul(centered_data, principal_components)

    return reduced_data


data = pd.read_csv('Leukemia_GSE9476.csv')
#print(data.shape)
data = data.iloc[:,2:]
print(pca_covariance(data, 2))

