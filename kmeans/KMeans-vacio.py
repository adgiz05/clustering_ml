# -*- coding: utf-8 -*-

import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
from Point import Point
from Cluster import Cluster

DATASET1 = "../dataSets/DS_3Clusters_999Points.txt"
DATASET2 = "../dataSets/DS2_3Clusters_999Points.txt"
DATASET3 = "../dataSets/DS_5Clusters_10000Points.txt"
DATASET4 = "../dataSets/DS_7Clusters_100000Points.txt"

NUM_CLUSTERS = 3
ITERATIONS = 10

COLORS = ['red', 'blue', 'green', 'yellow', 'gray', 'pink', 'violet', 'brown', 'cyan', 'magenta']


def dataset_to_list_points(dir_dataset):
    """
    Read a txt file with a set of points and return a list of objects Point
    :param dir_dataset:
    """
    
    return points


def get_nearest_cluster(clusters, point):
    """
    Calculate the nearest cluster
    """


def print_clusters_status(it_counter, clusters):
    print('\nITERATION %d' % it_counter)
    for i, c in enumerate(clusters):
        print('\tCentroid Cluster %d: %s' % (i + 1, str(c.centroid)))


def print_results(clusters):
    print('\n\nFINAL RESULT:')
    for i, c in enumerate(clusters):
        print('\tCluster %d' % (i + 1))
        print('\t\tNumber Points in Cluster %d' % len(c.points))
        print('\t\tCentroid: %s' % str(c.centroid))


def plot_results(clusters):
    plt.plot()
    for i, c in enumerate(clusters):
        # plot points
        x, y = zip(*[p.coordinates for p in c.points])
        plt.plot(x, y, linestyle='None', color=COLORS[i], marker='.')
        # plot centroids
        plt.plot(c.centroid[0], c.centroid[1], 'o', color=COLORS[i],
                 markeredgecolor='k', markersize=10)
    plt.show()


def k_means(dataset, num_clusters, iterations):
    # Read data set

    # Select N points random to initiacize the N Clusters
   
    # Create N initial Clusters

    # Inicialize list of lists to save the new points of cluster

    converge = False
    it_counter = 0
    
    while (not converge) and (it_counter < iterations):
        # Assign points in nearest centroid
    
        # Set new points in clusters and calculate de new centroids
       
        # Check that converge all Clusters
       
        # Increment counter and delete lists of clusters points

        # Print clusters status
        print_clusters_status(it_counter, clusters)
        

    # Print final result
    print_results(clusters)

    plot_results(clusters)

    # Plot Final results
    #plot_results(clusters)


if __name__ == '__main__':
    #k_means(DATASET1, NUM_CLUSTERS, ITERATIONS)
    k_means(DATASET3, 5, ITERATIONS)
