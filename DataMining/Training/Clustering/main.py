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

features = [[1, 5], [6, 2], [8, 1], [3, 5], [2, 4], [2, 6], [6, 1], [6, 8],  [7, 3], [7, 6], [8, 3], [8, 7]]

s1 = "3    3    4    4    5    6    7    7    8    9    1    2    2    3    4    5    5    6    7    7"
s2 = "1    2    2    3    3    4    4    6    5    7    3    4    5    6    6    7    8    8    8    9"

s1 = [int(s) for s in s1.split(" ") if s != ""]
s2 = [int(s) for s in s2.split(" ") if s != ""]

print(s1)
print(s2)

features = list(zip(s1, s2))

def k_means(points: List[List[float]], num_centers: int):

    # Stores the id of all centroids
    clusters = {0: [], 1: []}

    centroid_coordinates = []

    for i in range(0, 2):
        centroid_coordinates.append((features[i][0], features[i][1]))

    # Initial assignment of point to clusters
    assign_points(points, clusters, centroid_coordinates)

    print(centroid_coordinates)

    new_centroid_coordinates = []

    while centroid_coordinates != new_centroid_coordinates:

        new_centroid_coordinates = centroid_coordinates.copy()
        clusters = {0: [], 1: []}

        assign_points(points, clusters, centroid_coordinates)

        for c in clusters.keys():
            new_x = round(sum([points[point][0] for point in clusters[c]]) / len(clusters[c]), 4)
            new_y = round(sum([points[point][1] for point in clusters[c]]) / len(clusters[c]), 4)
            centroid_coordinates[c] = [new_x, new_y]


        print(centroid_coordinates)

        plt.clf()


        current_id = 0
        for cluster in clusters.values():
            for point in cluster:
                current_point = features[point]
                plt.scatter(current_point[0], current_point[1], marker='o', color=get_color_for_cluster(current_id))
                plt.scatter(centroid_coordinates[current_id][0], centroid_coordinates[current_id][1], marker='o', color='black')
            current_id += 1
        # plt.show()
            
    return clusters, centroid_coordinates



def assign_points(points: List[List[float]], clusters: Dict[int, List[float]], centroid_coordinates: List[Tuple[float, float]]):
    for point in range(len(points)):
        clusters[get_closest_centroid(points, point, clusters, centroid_coordinates)].append(point)

def get_closest_centroid(points: List[List[float]], index: int, clusters: Dict[int, List[float]], centroid_coordinates: List[Tuple[float, float]]):
    return min(clusters.keys(), key=lambda centroid: get_distance(points[index], centroid_coordinates[centroid]))

def get_distance(p1: List[float], p2: List[float]) -> float:
    return 1 - (sum([p1[i] * p2[i] for i in range(len(p1))])) / (math.sqrt(sum([p1[i] ** 2 for i in range(len(p1))]) * sum([p2[i] ** 2 for i in range(len(p1))])))

def get_distance2(p1: List[float], p2: List[float]) -> float:
    return math.sqrt(sum([abs(p1[d] - p2[d]) for d in range(len(p1))]))

def get_color_for_cluster(cluster_id: int):
    if cluster_id == 0:
        return 'pink'
    if cluster_id == 1:
        return 'blue'
    if cluster_id == 2:
        return 'purple'

clusters, centroid_coordinates = k_means(features, 2)


current_id = 0
plt.clf()
for cluster in clusters.values():
    for point in cluster:
        current_point = features[point]
        plt.scatter(current_point[0], current_point[1], marker='o', color=get_color_for_cluster(current_id))
        plt.scatter(centroid_coordinates[current_id][0], centroid_coordinates[current_id][1], marker='o', color='black')
    current_id += 1
plt.show()
