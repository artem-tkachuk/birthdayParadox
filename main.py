import matplotlib.pyplot as plt
import numpy as np


def permutations(k, n):
    assert k > n, 'k must be larger than n'

    prod = 1
    for i in range(k - n, k):
        prod *= i
    return prod


def graph(n):
    x = np.arange(1, 101)
    y = [1 - permutations(365, i) / 365 ** i for i in range(n)]

    plt.scatter(x, y)
    plt.grid()
    plt.ylabel('P(>= 2 people have same birthday)')
    plt.xlabel('n - # of people')
    plt.show()


graph(n=100)  # number of people
print(1 - permutations(365, 60) / 365 ** 60)
