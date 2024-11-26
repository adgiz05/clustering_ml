# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage

# Constant
DATASET1 = "./dataSets/DS_3Clusters_999Points.txt"
DATASET2 = "./dataSets/DS2_3Clusters_999Points.txt"
DATASET3 = "./dataSets/DS_5Clusters_10000Points.txt"


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


def plot_gap(dataset):
    points = dataset_to_list_points(dataset)

    # Calculate distances between points or groups of points
    Z = linkage(points, metric='euclidean', method='ward')

    # Obtain the last 10 distances between points
    last = Z[-10:, 2]
    num_clustres = np.arange(1, len(last) + 1)

    # Calculate Gap
    gap = np.diff(last, n=2)  # second derivative
    plt.plot(num_clustres[:-2] + 1, gap[::-1], 'ro-', markersize=8, lw=2)
    plt.show()


if __name__ == '__main__':
    plot_gap(DATASET1)
