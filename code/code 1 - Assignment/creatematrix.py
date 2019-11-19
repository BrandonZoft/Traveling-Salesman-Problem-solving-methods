import numpy as np

def save_matrix(number, size):
    matrix = np.random.randint(1001, size=(size, size))
    np.savetxt("inst{}_{}.csv".format(number, size), matrix, fmt='%i', delimiter=" ")

for i in range(4):
    save_matrix(i + 1, 4)
    save_matrix(i + 1, 10)
    save_matrix(i + 1, 25)
    save_matrix(i + 1, 50)
    save_matrix(i + 1, 200)


