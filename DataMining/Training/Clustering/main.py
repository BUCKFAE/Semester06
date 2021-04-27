"""Clustering"""

import random

from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import math
import numpy as np

from typing import List, Dict, Tuple

features, true_labels = make_blobs(
    n_samples = 200,
    centers = 3,
    cluster_std = 2.1)

def k_means(points: List[List[float]], num_centers: int):

    # Stores the id of all centroids
    clusters = {0: [], 1: [], 2: []}

    centroid_coordinates = []

    # Creating three distinct random centroids
    while len(centroid_coordinates) < num_centers:
        random_node = random.choice(range(len(features)))
        random_point = (points[random_node][0], points[random_node][1])
        centroid_coordinates.append(random_point)

    # Initial assignment of point to clusters
    assign_points(points, clusters, centroid_coordinates)

    print(centroid_coordinates)

    new_centroid_coordinates = []

    while centroid_coordinates != new_centroid_coordinates:

        new_centroid_coordinates = centroid_coordinates.copy()
        clusters = {0: [], 1: [], 2: []}

        assign_points(points, clusters, centroid_coordinates)

        for c in clusters.keys():
            new_x = round(sum([points[point][0] for point in clusters[c]]) / len(clusters[c]), 4)
            new_y = round(sum([points[point][1] for point in clusters[c]]) / len(clusters[c]), 4)
            centroid_coordinates[c] = [new_x, new_y]


        print(centroid_coordinates)
            
    return clusters



def assign_points(points: List[List[float]], clusters: Dict[int, List[float]], centroid_coordinates: List[Tuple[float, float]]):
    for point in range(len(points)):
        clusters[get_closest_centroid(points, point, clusters, centroid_coordinates)].append(point)

def get_closest_centroid(points: List[List[float]], index: int, clusters: Dict[int, List[float]], centroid_coordinates: List[Tuple[float, float]]):
    return min(clusters.keys(), key=lambda centroid: get_distance(points[index], centroid_coordinates[centroid]))

def get_distance(p1: List[float], p2: List[float]) -> float:
    return math.sqrt(sum([abs(p1[d] - p2[d]) for d in range(len(p1))]))

def get_color_for_cluster(cluster_id: int):
    if cluster_id == 0:
        return 'red'
    if cluster_id == 1:
        return 'blue'
    if cluster_id == 2:
        return 'green'

clusters = k_means(features, 3)


current_id = 0
for cluster in clusters.values():
    for point in cluster:
        current_point = features[point]
        plt.scatter(current_point[0], current_point[1], marker='o', color=get_color_for_cluster(current_id))
    current_id += 1
plt.show()
