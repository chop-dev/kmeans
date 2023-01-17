# K-Means clustering implementation

# Import Libraries
import matplotlib.pyplot as plt
import math
import csv
import random
import numpy as np


# ====
# Define a function that computes the euclidean distance between two data points
def distance(x_y, point):
    return math.sqrt((point[0] - x_y[0]) ** 2 + (point[1] - x_y[1]) ** 2)


# Find mean of list of data points
def points_mean(data_points):

    # Intialise the sum variables for each point
    y_sum = 0
    x_sum = 0

    # Iterate over the elements in the list
    for point in data_points:
        x_sum += point[0]
        y_sum += point[1]

    return [x_sum / len(data_points), y_sum / len(data_points), ]


# Calculate closest centroid
def centroid_selection(centroids, point):
    # Initialise close_centroid_index & centroid_distance
    close_centroid_index = 0
    centroid_distance = distance(centroids[0], point)

    for centroid_index, centroid in enumerate(centroids):
        temp_dist = distance(centroid, point)
        if temp_dist < centroid_distance:
            centroid_distance = temp_dist
            close_centroid_index = centroid_index
    return close_centroid_index


# Assign data points to clusters as determined by user input and add clusters to dictionary, data points to each cluster
def cluster_builder(centroid, data_points):
    # Create list of clusters to assign data_points in to
    clusters = [{'center_point': center_point, 'data_points': []} for center_point in centroid]

    # Append points into cluster with shortest centroid distance
    for point in data_points:
        close_centroid_index = centroid_selection(centroid, point)
        clusters[close_centroid_index]['data_points'].append(point)
    return clusters


if __name__ == '__main__':

    # Request the file name
    file = input("""\nPlease enter the file name you want to use:
                        data1953.csv
                        data2008.csv
                        dataBoth.csv \n""")

    # Initialise number of clusters k and iterations
    cluster_input = 2
    iteration_input = 6

    # Request user Input on Clusters 
    while True:
        try:
            cluster_input = int(input("\nPlease enter the number of clusters: "))
            break
        except ValueError:
            print("Error. Please enter a valid number of clusters: ")

    # Request User Input on Iterations
    while True:
        try:
            iteration_input = int(input("\nPlease enter the number of iterations: "))
            break
        except ValueError:
            print("Error. Please enter a valid number of clusters: ")

    # List to store x and y values for each countries data
    countries_info = []

    # Open csv file
    # Read data and store into birth and life
    with open(file, 'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        # Loop through file to find x and y values
        for line in readCSV:

            if line[0] != 'Countries':
                birth_rate = float(line[1])
                life_expectancy = float(line[2])

                # Append data point to countries_info
                countries_info.append([birth_rate, life_expectancy])

    # Empty list to store clusters in
    complete_clusters = []

    # Start the clustering

    #===
    # Iterate over data as requested by user
    for i in range(iteration_input):

        # Initialise iteration_sum_distances
        iteration_sum_distances = 0.0

        if i == 0:

            # First iteration selects random points from countries_info
            cluster_centroids = random.sample(countries_info, cluster_input)
        else:

            # On each subsequent pass, calculate a new mean 'centroid' for each cluster
            cluster_centroids = [points_mean(cent['data_points']) for cent in complete_clusters]

        # Add clusters to complete_clusters list 
        complete_clusters = cluster_builder(cluster_centroids, countries_info)

        # Calculate distance and mean for each iteration
        for cluster in complete_clusters:
            mean = cluster['center_point']

            for point in cluster['data_points']:
                iteration_sum_distances += distance(point, mean)

        # Print sum of distance for each iteration
        print(f"\n Iteration {i + 1}: Sum of distance squared: {iteration_sum_distances}.")

    # Create figure
    figure = plt.figure()
    plt.title('World Birth rate + Life expectancy')
    plt.xlabel('Birth Rate')
    plt.ylabel('Life Expectancy')

    # Store number of countries and clusters
    cluster_count = 1
    country_list = []

    # Loop through the clusters to plot the points
    # Set colours for each cluster
    for cluster in complete_clusters:

        # Color list created with random choices
        colours = [[random.random(), random.random(), random.random()]]

        # Initialise Country Count
        count_country = 0

        # Loop through data points in cluster, sepearate into x and y values to calculate average
        for point in cluster['data_points']:
            x = point[0]
            y = point[1]
            sum_x = 0
            sum_y = 0
            sum_x += x
            sum_y += y

            # Add data points to graph within their respective cluster
            plt.scatter(point[0], point[1], c=colours)

            # Add 1 for each data_point added to graph
            count_country += 1

            # Add country names to cty_info once added to clusters
            with open(file, 'r') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')

                for line in readCSV:
                    if line[0] != 'Countries' and x == float(line[1]) and y == float(line[2]):
                        country_name = str(line[0])
                        country_list.append(country_name)

        # Print results
        print(f"\nCluster {cluster_count}: {count_country} countries.")
        print(f"\nCluster {cluster_count} Country List: {country_list}")
        print(f"\nCluster {cluster_count} average birth rate = {sum_x}")
        print(f"\nCluster {cluster_count} average life expectancy = {sum_y}")

        # Clear data
        country_list.clear()
        cluster_count += 1

    # Print to user
    plt.show()

# References:
# https://docs.python.org/2/library/csv.html

# https://towardsdatascience.com/pca-using-python-scikit-learn-e653f8989e60

# https://www.geeksforgeeks.org/numpy-argmin-python/

# https://realpython.com/k-means-clustering-python/

# https://www.tutorialspoint.com/numpy/numpy_insert.htm#:~:text=This%20function%20inserts%20values%20in,the%20input%20array%20is%20flattened.

# https://numpy.org/doc/stable/reference/generated/numpy.vstack.html

# https://www.askpython.com/python/examples/k-means-clustering-from-scratch

# https://stackoverflow.com/questions/34226400/find-the-index-of-the-k-smallest-values-of-a-numpy-array
