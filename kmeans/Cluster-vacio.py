# -*- coding: utf-8 -*-


import numpy as np

class Cluster:
    """
    Class to represent a Cluster: set of points and their centroid
    """

    def __init__(self, points):
        if len(points) == 0:
            raise Exception("Cluster cannot have 0 Points")
        else:
            self.points = points
            self.dimension = points[0].dimension

        # Check that all elements of the cluster have the same dimension
        for p in points:
            if p.dimension != self.dimension:
                raise Exception(
                    "Point %s has dimension %d different with %d from the rest "
                    "of points") % (p, len(p), self.dimension)

        # Calculate Centroid
        self.centroid = self.calculate_centroid()
        self.converge = False

    def calculate_centroid(self):
        """
         Centroid of cluster
        """
       

    def update_cluster(self, points):
        """
        New centroid, check if converge
        """
        

    def __repr__(self):
        cluster = 'Centroid: ' + str(self.centroid) + '\nDimension: ' + str(
            self.dimension)
        for p in self.points:
            cluster += '\n' + str(p)

        return cluster + '\n\n'
