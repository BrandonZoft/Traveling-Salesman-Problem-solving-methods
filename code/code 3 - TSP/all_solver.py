import time
import os.path
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

def run_file(filename):

    start1 = time.time()

    # 1.- Read .TSP file.
    with open(filename + '.tsp', 'r') as file:
        data = file.read()

    # 2.- Write the coordenates in list.
    # Only reads after NODE_COORD_SECTION and before EOF
    data = data.split("NODE_COORD_SECTION")[1].split("EOF")[0].strip().split('\n')
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
    high_number = 1000000
    nn_table = [x[:] for x in distances_table]
    starting_city = 0
    nn_solution = [starting_city]
    min_number_index = 0
    for i in range(len(nn_table)):
        # replaces initial zero with high number
        nn_table[min_number_index][min_number_index] = high_number
        for item in (nn_solution):
            nn_table[min_number_index][item] = high_number
        min_number = min(nn_table[min_number_index])
        min_number_index = nn_table[min_number_index].index(min_number)
        nn_solution.append(min_number_index)

    def total_cost_func(solution):
        # deleting last element of list(as i don't know if it's correct), and adding the starting city
        del solution[-1]
        solution.append(solution[0])

        if solution[0] == 1:
            for i in range(len(solution)):
                solution[i] = solution[i] - 1

        nn_total_cost = solution[:]
        nn_total_cost.append(nn_total_cost[-1]) # adding same last city to last so distances is zero

        total_cost = []

        for i in range(len(solution)):
            distance = getEuclideanDistance(matrix_list[nn_total_cost[i]], matrix_list[nn_total_cost[i + 1]])
            total_cost.append(distance)

        for i in range(len(solution)):
            solution[i] = solution[i] + 1

        total_cost = sum(total_cost)
        return total_cost


    nn_total_cost = total_cost_func(nn_solution)
    endNN = time.time()

    startCI = time.time()

    # 5.- Solve TSP with cheapest insertion method.
    def cheapest_insertion():
        ci_table = [x[:] for x in distances_table]
        i_city = starting_city
        ci_table[0][i_city] = high_number
        j_city = ci_table[i_city].index(min(ci_table[i_city]))
        route = [i_city, j_city]
        ci_table[i_city][j_city] = high_number
        j_city = ci_table[i_city].index(min(ci_table[i_city]))
        route.insert(1, j_city)
        all_cities = []
        for i in range(len(ci_table)):
            all_cities.append(i)
        k_cities = [x for x in all_cities if x not in route] # removes cities already in route

        for i in range(len(all_cities) - 3):
            insert_array = []
            for k_city in k_cities:
                formula_array = []
                for i in range(len(route) - 1):
                    i_city = route[i]
                    j_city = route[i + 1]
                    formula_result = ci_table[i_city][k_city] + ci_table[k_city][j_city] - ci_table[i_city][j_city]
                    formula_array.append(formula_result)
                insert_array.append(formula_array)
            min_cost = min([min(r) for r in insert_array])
            
            numpy_insert_array = np.asarray(insert_array)
            min_cost_index = np.argwhere(numpy_insert_array == min_cost)[0]
            city_to_add = k_cities[min_cost_index[0]]
            position = min_cost_index[1] + 1
            route.insert(position, city_to_add)
            k_cities = [x for x in all_cities if x not in route] # removes cities already in route once again

        route.append(starting_city)
        for i in range(len(route)):
            route[i] = route[i] + 1
        
        return route


    ci_solution = cheapest_insertion()
    ci_total_cost = total_cost_func(ci_solution)

    endCI = time.time()

    start2 = time.time()
    # 6.- Print 1.- NN Method and 2.- CI Method.
    print("-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#\nFilename:",
        filename + '.tsp\n')
    print("Cities to pass in the Nearest Neighbor method:", nn_solution)
    print("\nAnd total cost is:", nn_total_cost, '\n')

    print("Cities to pass in the Cheapest Insertion method:", ci_solution)
    print("\nAnd total cost is:", ci_total_cost, '\n')

    

    file_dict = {
        "filename": filename,
        "nn_solution_array": nn_solution,
        "nn_total_cost_array": nn_total_cost,
        "ci_solution_array": ci_solution,
        "ci_total_cost_array": ci_total_cost
    }

    filename = filename + ".opt.tour"
    # 7.- If optimial solution is available, calculate the cost and compare (print).
    if os.path.exists(filename) == True:
        with open(filename, 'r') as file:
            optimal_solution = file.read()

        print("----------------------------------\nAn optimal solution is available:\n----------------------------------")
        # Only reads after NODE_COORD_SECTION and before EOF
        optimal_solution = optimal_solution.split("TOUR_SECTION")[1].split("-1")[0].strip().split('\n')
        optimal_solution = [int(x) for x in optimal_solution]
        optimal_solution.append(optimal_solution[0])
        print("Optimal solution to go past every city is:", optimal_solution)
        optimal_cost = total_cost_func(optimal_solution)
        print("\nOptimal cost:", optimal_cost)


        decreaseNN = optimal_cost - nn_total_cost
        gapNN = abs(decreaseNN / optimal_cost * 100)
        file_dict['gapNN'] = gapNN
        print("\nNearest Neighbor Gap:", gapNN, '%')
        decreaseCI = optimal_cost - ci_total_cost
        gapCI = abs(decreaseCI / optimal_cost * 100)
        file_dict['gapCI'] = gapCI
        print("Cheapest Insertion Gap:", gapCI, '%\n')

        file_dict['optimal_solution'] = optimal_solution
        file_dict['optimal_cost'] = optimal_cost

    end2 = time.time()

    nn_time = round(endNN - startNN, 4)
    ci_time = round(endCI - startCI, 4)
    total_time = round(((end1 - start1) + (end2 - start2) + (endCI - startCI) + (endNN - startNN)), 4)
    print('Time to run Nearest Neighbor Method:', nn_time, 'seconds')
    print('Time to run Cheapest Insertion Method:', ci_time, 'seconds')
    print('Total time to run script:', total_time, 'seconds')
    file_dict['time'] = total_time
    file_dict['nn_time'] = nn_time
    file_dict['ci_time'] = ci_time
    
    return file_dict


# 8.- Do this for each file simultaneously (print while also writing to a csv to do a chart report).
all_dictionary = []
for i in tsp_name:
    dicc = run_file(i)
    all_dictionary.append(dicc)


with open('csvreport.csv', mode='w+') as report_csv:
    report_writer = csv.writer(report_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    report_writer.writerow(['name', 'time', 'ci_time', 'nn_time'])

    for i in range(len(all_dictionary)):
        name = all_dictionary[i].get('filename')
        # time = all_dictionary[i].get('time')
        # citime = all_dictionary[i].get('ci_time')
        # nntime = all_dictionary[i].get('nn_time')
        nn_cost = all_dictionary[i].get('nn_total_cost_array')
        ci_cost = all_dictionary[i].get('ci_total_cost_array')
        if 'optimal_cost' in all_dictionary[i]:
            optimal_cost = all_dictionary[i].get('optimal_cost')
            gapNN = all_dictionary[i].get('gapNN')
            gapCI = all_dictionary[i].get('gapCI')

            report_writer.writerow([name, optimal_cost, ci_cost, nn_cost, gapCI, gapNN])
        else:
            report_writer.writerow([name, 0, ci_cost, nn_cost, 0, 0])


