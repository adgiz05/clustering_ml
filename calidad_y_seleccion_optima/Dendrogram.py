# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Constant
DATASET1 = "../dataSets/DS_3Clusters_999Points.txt"
DATASET2 = "../dataSets/DS2_3Clusters_999Points.txt"
DATASET3 = "../dataSets/DS_5Clusters_10000Points.txt"


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


def plot_dendrogram(dataset):
    points = dataset_to_list_points(dataset)

    # Calculate distances between points or groups of points
    Z = linkage(points, metric='euclidean', method='ward')

    plt.title('Dendrogram')
    plt.xlabel('Points')
    plt.ylabel('Euclidean Distance')

    # Generate Dendrogram
    dendrogram(
        Z,
        truncate_mode='lastp',
        p=12,
        leaf_rotation=90.,
        leaf_font_size=12.,
        show_contracted=True
    )

    plt.show()


if __name__ == '__main__':
    plot_dendrogram(DATASET1)
