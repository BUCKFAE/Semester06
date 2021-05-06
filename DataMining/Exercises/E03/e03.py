"""Python-Script to help out with E03"""

import matplotlib.pyplot as plt
import math

def task2():
    """Task2"""
    data = [-0.39, 0.12, 0.94, 1.67, 1.76, 2.44, 3.72, 4.28, 4.92, 5.53, 0.06, 0.48, 1.01, 1.68, 1.8, 3.25, 4.12, 4.6, 5.28, 6.22]
    print("Data: {}".format(data))

    bins = [x / 2 for x in range(-2, 16)]
    print("Bins: {}".format(bins))

    plt.hist(data, density=True, bins = bins)
    plt.show()

def task3():
    """Task3"""
    pass

def task4():
    
    points = [(1, 0), (1, 2), (2, 1), (7, 1), (9, 2), (9, 1), (5, 2)]

    cluster = [points[:3], points[3:]]

    # Calculating the DB index
    db = (1 / len(cluster)) * sum([max([([math.sqrt(1 / len(c) * sum([manhattan(i, [sum([c[i][dim] for i in range(len(c))]) / len(c) for dim in range(len(c[0]))]) ** 2 for i in c])) for c in cluster][i] + [math.sqrt(1 / len(c) * sum([manhattan(i, [sum([c[i][dim] for i in range(len(c))]) / len(c) for dim in range(len(c[0]))]) ** 2 for i in c])) for c in cluster][j]) / manhattan([sum([cluster[i][j][dim] for j in range(len(cluster[i]))]) / len(cluster[i]) for dim in range(len(cluster[i][0]))], [sum([cluster[j][i][dim] for i in range(len(cluster[j]))]) / len(cluster[j]) for dim in range(len(cluster[j][0]))]) if i != j else 0 for j in range(len(cluster))]) for i in range(len(cluster))])

    print(db)

    # Plotting the points
    plt.scatter([p[0] for p in points], [p[1] for p in points])
    plt.show()


def manhattan(x, y):
    return sum([abs(x[i] - y[i]) for i in range(len(x))])

if __name__ == "__main__":
    task4()