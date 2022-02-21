import scipy.io as sp
import numpy as np

mat = sp.loadmat("linedata.mat")
x = mat['x']

N = 100  # datasize
temp2 = np.empty(100)

matrix_1 = np.array([[(2*(2*N-1))/(N+1), -6/(N+1) ], [-6/(N+1), 12/((N^2)-1)]])



temp1 = (np.sum(x))
sum_1 = (1/N) * temp1


for n in range(0, 100) :
    temp2 =np.sum(n * x)
sum_2 = (1/N) * temp2


matrix_2 = np.array([[temp1],[temp2]])

AB_matrix = matrix_1 * matrix_2

print(AB_matrix.shape)
