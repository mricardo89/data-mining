import numpy as np
import matplotlib.pyplot as plt

class KMeansMatematico:
    def __init__(self, k:int=3, n_iter:int=100):
        self.iterations = n_iter
        self.k = k
        self.labels = None
        self.centroids = None

    def euclidean_distance(self, x:np.array, mu:np.array):
        return np.linalg.norm(x - mu, 2)

    def fit(self, X:np.array):
        # Obtenemos las dimensiones del dataset
        n_muestras, n_features = X.shape

        # Creamos posiciones aleatorias
        mu_current = np.random.choice(X, )