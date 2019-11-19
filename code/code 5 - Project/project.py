import time
import os.path
import random
import math
import numpy as np
import csv

# 1.- Read .TSP file.
# 2.- Write the coordenates in list.
# 3.- Write another table with the distances of each node through the euclidian distance formula.
# 4.- Solve TSP with nearest neighbor method.
# 5.- Solve TSP with cheapest insertion method.
# 6.- Print 1.- NN Method and 2.- CI Method.
# 7.- If optimial solution is available, calculate the cost and compare (print).
# 8.- Do this for each file simultaneously (print while also writing to a csv to do a chart report).

# notes: record computing time for each .TSP file.

tsp_name = ["a280",
            "ali535",
            "att48",
            "att532",
            "berlin52",
            "bier127",
            "ch130",
            "ch150",
            "kroB200"]

filename = 'att48'



start1 = time.time()

# 1.- Read .TSP file.
with open(filename + '.tsp', 'r') as file:
    data = file.read()

# 2.- Write the coordenates in list.
# Only reads after NODE_COORD_SECTION and before EOF
data = data.split("NODE_COORD_SECTION")[
    1].split("EOF")[0].strip().split('\n')
matrix_list = [item.strip().split() for item in data]
matrix_list = [list(map(float, i)) for i in matrix_list]

def getEuclideanDistance(a, b):
    distance = math.sqrt(pow(b[1] - a[1], 2) + pow(b[2] - a[2], 2))
    return distance

# 3.- Write another table with the distances of each node through the euclidian distance formula.
distances_table = []
for i in range(len(matrix_list)):
    row = []
    for k in range(len(matrix_list)):
        distance = getEuclideanDistance(matrix_list[i], matrix_list[k])
        row.append(distance)
    distances_table.append(row)

end1 = time.time()
startNN = time.time()

# 4.- Solve TSP with nearest neighbor method.
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]


def meta_tsp(cmax, cmin, alph):
    result = cmin + (alph * (cmax - cmin))
    return result

s_best = 0
s_best_solution = 0
iterations = 500
for k in range(iterations):
    fortime1 = time.time()
    alpha = 0.4
    high_number = 1000000
    nn_table = [x[:] for x in distances_table]
    starting_city = 0
    nn_solution = [starting_city]
    min_number_index = 0
    s = True
    for i in range(len(nn_table)):
        # replaces initial zero with high number
        nn_table[min_number_index][min_number_index] = high_number
        for item in (nn_solution):
            nn_table[min_number_index][item] = high_number
        # if s == True:
        #     print(nn_table[min_number_index])
        #     s = False
        if i != len(nn_table) - 1:
            copied_list = remove_values_from_list(((nn_table[min_number_index])[:]), high_number)
        min_number = min(copied_list)
        max_number = max(copied_list)
        meta_result = (meta_tsp(max_number, min_number, alpha))
        meta_list = [i for i in nn_table[min_number_index] if i <= meta_result]
        if i != len(nn_table) - 1:
            random_from_meta = random.choice(meta_list)
            random_index = nn_table[min_number_index].index(random_from_meta)
            nn_solution.append(random_index)
            min_number_index = random_index
        else:
            nn_solution.append(starting_city)

    def total_cost_func(solution):
        # deleting last element of list(as i don't know if it's correct), and adding the starting city
        del solution[-1]
        solution.append(solution[0])

        if solution[0] == 1:
            for i in range(len(solution)):
                solution[i] = solution[i] - 1

        nn_total_cost = solution[:]
        # adding same last city to last so distances is zero
        nn_total_cost.append(nn_total_cost[-1])

        total_cost = []

        for i in range(len(solution)):
            distance = getEuclideanDistance(
                matrix_list[nn_total_cost[i]], matrix_list[nn_total_cost[i + 1]])
            total_cost.append(distance)

        for i in range(len(solution)):
            solution[i] = solution[i] + 1

        total_cost = sum(total_cost)
        return total_cost

    nn_total_cost = total_cost_func(nn_solution)
    endNN = time.time()

    start2 = time.time()
    # 6.- Print 1.- NN Method and
    # print("-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#\nFilename:",
    #         filename + '.tsp\n')
    # print("Cities to pass in the Nearest Neighbor method:", nn_solution)
    # print("\nAnd total cost is:", nn_total_cost, '\n')

    # print("----------------------------------\nUsing local search\n----------------------------------")
    solution = nn_solution
    cost = nn_total_cost

    best_dict_cost = cost
    best_found_cost = cost

    start3 = time.time()

    def reverse(city1, city2, solutionfunc):
        new_solution = solutionfunc[:]
        start = new_solution.index(city1) - 1
        end = new_solution.index(city2)
        reversed_set = new_solution[end:start:-1]
        if start == -1:
            reversed_set = new_solution[end:None:-1]
            start = 0

        start = 1 + start
        del new_solution[start:end + 1]
        new_solution[start:start] = reversed_set

        return new_solution

    dict_best_cost_found = 0
    counter = 0
    max_counter = 500
    while True:
        sliced_list = solution[1:-1]
        city1 = random.choice(sliced_list[:-1])
        city1index = sliced_list.index(city1)
        list_for_city2 = sliced_list[city1index::]
        city2 = random.choice(list_for_city2[1::])
        reverse_costsol = reverse(city1, city2, solution)
        ls_cost = total_cost_func(reverse_costsol)
        if (ls_cost < best_found_cost):
            # print('A better solution was found based on first improvement local search reverse method:')
            # print(reverse_costsol)
            # print('cost:', ls_cost, '\n')
            solution = reverse_costsol
            best_found_cost = ls_cost
            dict_best_cost_found = best_found_cost
            counter = 0
        else:
            counter = counter + 1
        if counter == max_counter:
            # print('Attempted maximum number of tries before finding a better solution:', max_counter)

            decrease = cost - best_found_cost
            gap = round(abs(decrease / cost * 100), 4)

            # print('improved cost by', abs(best_found_cost -
                                        # cost), 'with a gap of', gap, '%\n')
            break

    if k == 0:
        s_best = nn_total_cost 
        s_best_solution = nn_solution

    if(s_best >= best_found_cost):
        s_best = best_found_cost
        s_best_solution = solution



    end3 = time.time()
    end2 = time.time()
    fortime2 = time.time()

    nn_time = round(endNN - startNN, 4)
    ls_time = round(end3 - start3, 4)
    fortime = round(fortime2 - fortime1, 4)
    total_time = round(fortime2 - start1, 4)

    print('Iteration: {}, Computational Time: {}'.format(k, fortime))

filename_tour = filename + ".opt.tour"
# 7.- If optimial solution is available, calculate the cost and compare (print).
if os.path.exists(filename_tour) == True:
        with open(filename_tour, 'r') as file:
            optimal_solution = file.read()

        print("----------------------------------\nAn optimal solution is available:\n----------------------------------")
        # Only reads after NODE_COORD_SECTION and before EOF
        optimal_solution = optimal_solution.split(
            "TOUR_SECTION")[1].split("-1")[0].strip().split('\n')
        optimal_solution = [int(x) for x in optimal_solution]
        optimal_solution.append(optimal_solution[0])
        print("Optimal solution to go past every city is:", optimal_solution)
        optimal_cost = total_cost_func(optimal_solution)
        print("\nOptimal cost:", optimal_cost)

        decreaseNN = optimal_cost - nn_total_cost
        gapNN = abs(decreaseNN / optimal_cost * 100)
        print('Initial NN cost:', nn_total_cost)
        print("Initial Nearest Neighbor Gap:", gapNN, '%\n')

print('Reached end of {} iterations'.format(iterations))
print('Best solution found:', s_best_solution)
print('Best cost found:', s_best)
print('Total time:', total_time, 'seconds')