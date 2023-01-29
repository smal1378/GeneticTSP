# GeneticTSP
A genetic algorithm to solve traveling salesman problem.
<br><br>
---
### Problem Explanation:
There are some city coordinates given (20 cities in my case), assuming that all cities are 
connected to each other through a straight line. <br>
The goal is to find a path through these cities where traveled distance is minimum
and all cities are seen without seeing a city twice.
<br><br>
----
### Chromosome Representation
Each chromosome is an object created from Solution class which contains it's fittness value 
and a list of cities to go through in order. While each city is a tuple of `(x, y)`.
<br><br>
---
### Fittness Function
The fittness function is `min(0, 5000 - total_distance)` <br>
Where `total_distance` is the sum of euclidean distance between all cities in path. 
<br><br>
---
### Recommended Parameters
- Generation Count: `100`
- Population Size: `300`
- Probability Of Crossover: `0.90`
- Probability Of Mutation: `0.10`
- K (For K-Tournament Parent Selection): `2`
<br><br>
---
### Algorithm Operators:
- Parent Selection: K-Tournament Selection.
- Crossover: Customized One-Point Crossover, Implemented crossover will use a simple
one point crossover but prevents repetitive cities in a chromosome.
- Mutation: Implemented method will swap two random selected cities within a chromosome.
<br><br>
---
### How To Run
Simply clone or download the project, run `run.py` file, make sure you've installed `matplotlib`.
The output plots will show you the path and cities and average, best, worst fittness per generation.
<br><br>
---
#### Author
- Esmail Mahjoor