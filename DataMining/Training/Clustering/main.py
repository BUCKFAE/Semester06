"""Clustering"""

import random

from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import math
import numpy as np

from typing import List, Dict

features, true_labels = make_blobs(
    n_samples = 200,
    centers = 3,
    cluster_std = 2.5)

def k_means(points: List[List[float]], num_centers: int):

    # Stores the id of all centroids
    clusters = {}

    # Creating three distinct random centroids
    while len(clusters.keys()) < num_centers:
        random_center = random.choice(range(len(features)))
        if random_center not in clusters.keys():
            clusters[random_center] = []

    # Initial assignment of point to clusters
    assign_points(points, clusters)

    new_clusters = {}

    # Improving clusters each iteration until there is no improvement anymore
    while clusters.keys() != new_clusters.keys():
        new_clusters = clusters.copy()
        assign_points(points, new_clusters)

    return clusters


def assign_points(points: List[List[float]], clusters: Dict[int, List[int]]):
    for point in range(len(points)):
        clusters[get_closest_centroid(points, point, clusters)].append(point)

def get_closest_centroid(points: List[List[float]], index: int, clusters: Dict[int, List[int]]):
    return min(clusters.keys(), key=lambda centroid: get_distance(points, centroid, index))

def get_distance(points: List[List[float]], i: int, j: int):
    return math.sqrt(sum([abs(points[i][d] - points[j][d]) for d in range(len(points[0]))]))

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