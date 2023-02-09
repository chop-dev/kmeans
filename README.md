# K-Means Clustering

## Introduction
This program is an implementation of the K-Means clustering algorithm. It can be used to group similar data points together and form clusters.

## Requirements
+ Python 3.x
+ Numpy
+ Matplotlib
+ CSV
## Usage
The program requires you to input the name of the file you want to use. You can choose from the following options:

+ data1953.csv
+ data2008.csv
+ dataBoth.csv

Next, you have to input the number of clusters you want to form and the number of iterations.
The program calculates the sum of distances for each iteration and returns the result.

## Functionality
The program contains several functions that perform the following tasks:

+ `distance` - Calculates the Euclidean distance between two data points.

+  `points_mean` - Finds the mean of a list of data points.

+ `centroid_selection` - Calculates the closest centroid to a data point.

+ `cluster_builder` - Assigns data points to clusters and adds clusters to a dictionary along with their data points.

## Results
The program returns the sum of distances for each iteration. These results can be used to determine the best number of clusters and iterations for a specific dataset.

## Conclusion
This K-Means clustering implementation is a useful tool for grouping similar data points into clusters. The user can input their desired number of clusters and iterations, and the program will return the sum of distances for each iteration.
