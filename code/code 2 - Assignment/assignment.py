import numpy as np
import time

start = time.time()

filename = 'inst2_10.csv'
matrix = np.loadtxt(filename, dtype=int, delimiter=',')

high_number = 100000
min_number = 0
assignment_function_cost = []
assignment_cost = 0

while True:
    print(matrix, '\n')

    # Finds the minimum number and the index in the matrix.
    min_number = matrix.min()
    min_index = np.unravel_index(matrix.argmin(), matrix.shape)

    # If there's no minimum number left in the matrix, the answer has been found and the loop ends.
    if min_number == high_number:
        break

    # Replaces the rows and columns when a minimum number has been found.
    matrix[:, min_index[1]] = high_number
    matrix[min_index[0], :] = high_number
    print('Minimum number: {} [{}, {}]\n'.format(min_number, min_index[0], min_index[1]))

    assignment_cost += min_number
    # print(assignment_cost)
    assignment_function_cost.append([min_index[0], min_index[1]])

assignment_function_cost.sort()

print(filename, '\n')
for i in range(len(assignment_function_cost)):
    print('Worker {} on Task {}'.format(
        i + 1, assignment_function_cost[i][1] + 1))

print('\nTotal cost:', assignment_cost)

end = time.time()
total_time = end - start
print('\nScript duration:', end - start, 'seconds')
