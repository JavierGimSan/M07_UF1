import numpy as np

arr = np.array(range(50), dtype = 'int32') #Es crea un ndarray de 50 elements(0-49)
arr2 = np.diag(arr)

np.save('exercici1.npy', arr2)








