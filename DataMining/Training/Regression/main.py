import matplotlib.pyplot as plt
from sklearn import datasets
import random

"""Example for Linear regression and gradient descent"""

def main():
    # Data from the example sheet
    data_x, data_y = datasets.make_regression(n_samples=100, n_features=1, noise=5, bias=10)


    # Initial theta 0 and theta 1
    t0 = random.random()
    t1 = random.random()

    for iter_no in range(0, 100):
        current_error = (1 / len(data_x)) * sum([(t0 + t1 * data_x[i] - data_y[i]) ** 2 for i in range(len(data_x))])
        print(f"{iter_no=}:{current_error=}")

        # Calculating gradient
        tmp1 = (1 / len(data_x)) * sum([2 * (t0 + t1 * data_x[i] - data_y[i]) for i in range(len(data_x))])
        tmp2 = (1 / len(data_x)) * sum([2 * data_x[i] * (t0 + t1 * data_x[i] - data_y[i]) for i in range(len(data_x))])

        t0 -= tmp1 * 0.03
        t1 -= tmp2 * 0.03

    # Plotting model
    line_x = [x for x in range(int(min(data_x) - 1), int(max(data_x) + 2))]
    line_y = [t0 + t1 * x for x in range(int(min(data_x) - 1), int(max(data_x) + 2))]

    # Plotting data
    plt.plot(data_x, data_y, '.', label = "Data")
    plt.plot(line_x, line_y, label = "Model")
    plt.legend()
    plt.title(f"Linear Regression\ny = {t0}x + {t1}")
    plt.show()


if __name__ == "__main__":
    main()