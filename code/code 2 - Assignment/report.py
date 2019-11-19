import csv
import numpy as np
import time

matrix = np.loadtxt('inst4_4.csv', dtype=int, delimiter=',')

def report(inst, m):
    start = time.time()

    matrix = np.loadtxt('inst{}_{}.csv'.format(inst, m), dtype=int, delimiter=',')

    high_number = 100000
    min_number = 0
    assignment_function_cost = ''
    assignment_cost = 0

    while True:
        # print(matrix, '\n')

        # Finds the minimum number and the index in the matrix.
        min_number = matrix.min()
        min_index = np.unravel_index(matrix.argmin(), matrix.shape)

        # If there's no minimum number left in the matrix, the answer has been found and the loop ends.
        if min_number == high_number:
            break

        # Replaces the rows and columns when a minimum number has been found.
        matrix[:, min_index[1]] = high_number
        matrix[min_index[0], :] = high_number
        # print('Minimum number: {} [{}, {}]\n'.format(min_number, min_index[0], min_index[1]))

        assignment_cost += min_number
        assignment_function_cost += '[{}, {}] + '.format(
            min_index[0], min_index[1])

    # print(assignment_function_cost[:-2], 'Total cost:', assignment_cost, '\n')

    end = time.time()
    total_time = round(end - start, 4)
    # print(assignment_function_cost)
    print('Total Cost: {}, M = {}, Duration: {} seconds, inst{}_{}.csv'.format(assignment_cost, m, total_time, inst, m  ))

    file = [m, total_time, inst, assignment_cost]

    return file


with open('csvreport.csv', mode='w+') as report_csv:
    report_writer = csv.writer(report_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    report_writer.writerow(['m', 'seconds', 'instance', 'cost'])

    for i in range(4):
        file = report(i + 1, 4)
        report_writer.writerow([file[0], file[1], file[2], file[3]])
        file = report(i + 1, 10)
        report_writer.writerow([file[0], file[1], file[2], file[3]])
        file = report(i + 1, 25)
        report_writer.writerow([file[0], file[1], file[2], file[3]])
        file = report(i + 1, 50)
        report_writer.writerow([file[0], file[1], file[2], file[3]])
        file = report(i + 1, 200)
        report_writer.writerow([file[0], file[1], file[2], file[3]])


#scheduling problem.
# presentation
# introduction - general description, motivation, real applications
# problem description - formal notation with model
# heuristic procedure to solve it
# small example
# references


# Carlier, Jacques, and Éric Pinson. "An algorithm for solving the job-shop problem." Management science 35.2 (1989): 164-176.
# Dell'Amico, M., & Trubian, M. (1993). Applying tabu search to the job-shop scheduling problem. Annals of Operations research, 41(3), 231-252.


# only references next week
# journals of heuristics
# ejor
# annals
