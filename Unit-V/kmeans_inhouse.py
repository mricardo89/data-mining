import numpy as np
import matplotlib.pyplot as plt

class KMeansMatematico:
    def __init__(self, k=3, max_iters=100):
        self.k = k
        self.max_iters = max_iters
        self.centroides = None
        self.labels = None

    def calcular_distancia_euclidiana(self, X, centroides):
        # Implementación de ||x_i - \mu_j||^2 usando broadcasting de NumPy
        # X tiene forma (n, d), centroides (k, d). Transformamos para calcular distancias.
        distancias = np.linalg.norm(X[:, np.newaxis] - centroides, axis=2)
        return distancias

    def fit(self, X):
        n_muestras, n_caracteristicas = X.shape
        
        # 1. Inicialización (Selección aleatoria de K puntos de X)
        indices_aleatorios = np.random.choice(n_muestras, self.k, replace=False)
        self.centroides = X[indices_aleatorios]
        
        for i in range(self.max_iters):
            # 2. Asignación (Expectation)
            # Calculamos la distancia de cada punto a todos los centroides
            distancias = self.calcular_distancia_euclidiana(X, self.centroides)
            
            # argmin selecciona el índice del centroide más cercano para cada punto
            self.labels = np.argmin(distancias, axis=1)
            
            # Guardamos los centroides actuales para verificar convergencia luego
            centroides_antiguos = self.centroides.copy()
            
            # 3. Actualización (Maximization)
            for j in range(self.k):
                puntos_del_cluster = X[self.labels == j]
                # Si el clúster quedó vacío, evitamos división por cero
                if len(puntos_del_cluster) > 0:
                    self.centroides[j] = np.mean(puntos_del_cluster, axis=0)
                    
            # 4. Convergencia
            # Si los centroides no se movieron, el algoritmo convergió
            if np.all(centroides_antiguos == self.centroides):
                print(f"✅ Convergencia alcanzada en la iteración {i+1}.")
                break
                
        return self.labels

# --- Código para proyectar en clase ---
if __name__ == "__main__":
    from sklearn.datasets import make_blobs
    
    # Generamos datos sintéticos bidimensionales
    X, _ = make_blobs(n_samples=500, centers=4, cluster_std=0.8, random_state=42)
    
    # Instanciamos y entrenamos nuestro modelo puro
    modelo = KMeansMatematico(k=4)
    etiquetas = modelo.fit(X)
    
    # Visualización de los resultados y los centroides finales
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], c=etiquetas, cmap='viridis', alpha=0.6, s=30)
    plt.scatter(modelo.centroides[:, 0], modelo.centroides[:, 1], 
                c='red', marker='X', s=200, label='Centroides (μ)')
    
    plt.title("Implementación Matemática de K-Means (Desde cero)")
    plt.legend()
    plt.show()