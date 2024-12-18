# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Constant
DATASET1 = "../dataSets/DS_3Clusters_999Points.txt"
DATASET2 = "../dataSets/DS2_3Clusters_999Points.txt"
DATASET3 = "../dataSets/DS_5Clusters_10000Points.txt"
DATASET4 = "../dataSets/DS_7Clusters_100000Points.txt"
NUM_CLUSTERS = 3
MAX_ITERATIONS = 10
INITIALIZE_CLUSTERS = ['k-means++', 'random']
CONVERGENCE_TOLERANCE = 0.001
COLORS = ['red', 'blue', 'green', 'yellow', 'gray', 'pink', 'violet', 'brown','cyan', 'magenta']


def dataset_to_list_points(dir_dataset):
    """
    Read a txt file with a set of points and return a list of objects Point
    :param dir_dataset: path file
    """
    points = list()
    with open(dir_dataset, 'rt') as reader:
        for point in reader:
            points.append(np.asarray(list(map(float, point.split("::"))))) 
    return points


def print_results(centroids, num_cluster_points):
    print('\n\nFINAL RESULT:')
    for i, c in enumerate(centroids):
        print('\tCluster %d' % (i + 1))
        print('\t\tNumber Points in Cluster %d' % num_cluster_points.count(i))
        print('\t\tCentroid: %s' % str(centroids[i]))


def plot_results(centroids, num_cluster_points, points):
    plt.plot()
    for nc in range(len(centroids)):
        # plot points
        points_in_cluster = [boolP == nc for boolP in num_cluster_points]
        for i, p in enumerate(points_in_cluster):
            if bool(p):
                plt.plot(points[i][0], points[i][1], linestyle='None', color=COLORS[nc], marker='.')
        # plot centroids
        centroid = centroids[nc]
        plt.plot(centroid[0], centroid[1], 'o', markerfacecolor=COLORS[nc],
                 markeredgecolor='k', markersize=10)
    plt.show()


def k_means(dataset, num_clusters, max_iterations, init_cluster, tolerance):
    # Read data set
    
    # Object KMeans

    # Calculate Kmeans

    # Obtain centroids and number Cluster of each point

    # Print final result
    print_results(centroids, num_cluster_points)

    # Plot Final results
    plot_results(centroids, num_cluster_points, points)



if __name__ == '__main__':
    k_means(DATASET1, 3, MAX_ITERATIONS, INITIALIZE_CLUSTERS[0], CONVERGENCE_TOLERANCE)