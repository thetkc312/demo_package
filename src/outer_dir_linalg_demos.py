import numpy as np

class LinalgDemos:
    def __init__(self, size: int):
        self.size = size

    def get_random_matrix(self):
        return np.random.rand(self.size, self.size)
    
    def get_random_vector(self):
        return np.random.rand(self.size)
    
    def get_identity_matrix(self):
        return np.eye(self.size)
    
    def get_zeros_matrix(self):
        return np.zeros((self.size, self.size))
    
    def get_ones_matrix(self):
        return np.ones((self.size, self.size))
    
    def matrix_addition(self, A: np.array, B: np.array):
        return A + B
    
    def matrix_subtraction(self, A: np.array, B: np.array):
        return A - B
    
    def matrix_multiplication(self, A: np.array, B: np.array):
        return A @ B
    
    