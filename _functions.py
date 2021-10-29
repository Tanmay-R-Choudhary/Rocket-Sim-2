import numpy as np
import matplotlib.pyplot as plt

plt.style.use("dark_background")


def plot(mode, *data):
    if mode == "new":
        for x, y in data:
            plt.figure()
            plt.plot(x, y)
    if mode == "same":
        plt.figure()
        for x, y in data:
            plt.plot(x, y)

    plt.show()


def integrate_graph(time, array):
    res_array = [0]
    for n in range(0, len(time) - 1):
        res_array.append(res_array[-1] + 0.5 * (array[n + 1] + array[n]) * (time[n + 1] - time[n]))

    return np.array(res_array)
