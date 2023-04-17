import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return np.exp(x)


def g(x):
    return np.math.factorial(x)


def h(x):
    return x ** x


x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

y1 = f(x)

y2 = []
for i in x:
    y2.append(g(i))

y3 = h(x)

fig = plt.figure(figsize=(10, 8))

plt.yscale("log")

lines = plt.plot(x, y1, x, y2, x, y3, 'o')

plt.setp(lines[0], linewidth=1, color="r", linestyle='dashed')
plt.setp(lines[1], linewidth=2, color="g", linestyle='dotted')
plt.setp(lines[2], linewidth=3, color="b", linestyle='solid')

plt.legend(('y = e^x', 'y = x!', 'y = x^x'), loc='upper left')
plt.title('Function Graph')

plt.show()
