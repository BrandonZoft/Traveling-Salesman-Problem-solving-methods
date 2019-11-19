import numpy as np
import time

start = time.time()

matrix = np.loadtxt('inst1_4.csv', dtype=int)

min_number = 0
assignment_function_cost = ''
assignment_cost = 0
high_number = 100000

while True:

    # Finds the minimum number and the index in the matrix.
    min_number = matrix.min()
    min_index = np.unravel_index(matrix.argmin(), matrix.shape)

    # If there's no minimum number left in the matrix, the answer has been found and the loop ends.
    if min_number == high_number:
        break

    # Replaces the rows and columns when a minimum number has been found.
    matrix[:, min_index[1]] = high_number
    matrix[min_index[0], :] = high_number

    assignment_cost += min_number
    assignment_function_cost += '[{}, {}] + '.format(min_index[0], min_index[1])


print(assignment_function_cost[:-2])
print('Total cost:', assignment_cost)

end = time.time()
total_time = end - start
print('\nScript duration:', end - start, 'seconds')
