# 1.- Read TSP file.
# 2.- Write the coordenates in table.
# 3.- Write another table with the distances of each node through the euclidian distance formula.
# 4.- Solve TSP with nearest neightbor method.
# 5.- Solve TSP with cheapest insertion method.
# 6.- Print 1.- NN Method and 2.- CI Method.
# 7.- If optimial solution is available, calculate the cost and compare (print).
# 8.- Do this for each file simultaneously (print while also writing to a csv to do a chart report).

# notes: record computing time for each TSP file.

import requests

set_url = "http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/"
tsp_name = ["a280",
            "ali535",
            "att48",
            "att532",
            "berlin52",
            "bier127",
            "ch130",
            "ch150",
            "kroB200"]

for i in tsp_name:
    url = set_url + i + ".tsp"
    r = requests.get(url)
    filename = i + ".tsp"
    with open(filename, 'wb') as f:
        f.write(r.content)

for i in tsp_name:
    url = set_url + i + ".opt.tour"
    r = requests.get(url)
    filename = i + ".opt.tour"
    if r.status_code != 404:
        with open(filename, 'wb') as f:
            f.write(r.content)


