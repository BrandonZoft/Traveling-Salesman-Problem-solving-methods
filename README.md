Read at https://github.com/BrandonZoft/Traveling-Salesman-Problem-solving-methods

# Traveling-Salesman-Problem-solving-methods

<p align="center"><img src="TSO table.PNG" alt="drawing" width="500"/></p>

This is a set of data analysis/manipulation for the entirety class of [Selected	Topics	on	Optimization	(Temas	Selectos	de	Optimización)
Introduction	to	Combinatorial	Optimization AGO-DIC 2019](https://www.fime.uanl.mx/wp-content/uploads/2020/10/Optimizacion.pdf) with Dr. María Angélica. You can download the paper [here.](https://github.com/BrandonZoft/Traveling-Salesman-Problem-solving-methods/raw/master/TSO.pdf)

This uses a number of Python packages like Numpy and Pandas for data manipulation and matplotlib for visualization.

# Requirements
[Python 3.7](https://www.python.org/) or [Anaconda 3.7](https://www.anaconda.com/distribution/).
If using normal python 3, install requirements by doing
```
pip install -r requirements.txt
```

# About
```
web2file.py
```
Downloads TSP files from http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/.
Default files are:
- "a280",
- "ali535",
- "att48",
- "att532",
- "berlin52",
- "bier127",
- "ch130",
- "ch150",
- "kroB200"
```
plot.py
```
Plots on matplotlib based on csv files.

```
creatematrix.py
```
Creates a matrix of random numbers.
# Homework 1 - Assignment

Numbers found at matrix have to be lower than variable "high_number".

# Homework 2 - Assignment 
```
assignment.py
```
Solves a single file.
```
report.py
```
Solves all files created from creatematrix.py.
# Homework 4 - TSP solving methods
```
all_solver.py
```
Solves all files from web2file.py, creates a csv file for plotting.
# Homework 5 - TSP Local Search
```
all_localsearch_fulltime.py
```
Solves all files from web2file.py, by the full neighborhood local search method (reverse 2opt).
Default time limit for the full neighborhood is 1800 seconds (30 minutes, line 260). 
```
all_localsearch_firstimprov.py
```
Solves all files from web2file.py, by the first improvement method (reverse 2opt).
Default number of attempts is 500 (line 232). 
# Project 
```
project.py
```
Solves all files from web2file.py, starting from nearest neighbor method and the first improvement method (reverse 2opt).









