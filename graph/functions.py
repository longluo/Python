import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def f(x):
    return np.exp(x)


def g(x):
    return x ** x


def h(x):
    return np.math.factorial(n)


x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

y1 = f(x)
y2 = g(x)

fig = plt.figure(figsize=(10, 8))

plt.yscale("log")

plt.plot(x, y1, color="red", linestyle='-')
plt.plot(x, y2, color="green", marker='o')

y3 = []

for n in x:
    y3.append(h(n))

plt.plot(x, y3, color="blue", marker='*')

plt.xlabel("X Axis--------->")
plt.ylabel("Y Axis--------->")

plt.show()

# df = pd.DataFrame(zip(x, y1, y2, y3), columns= ['x', 'y=e^x', 'y=x^x', 'y=x!']).set_index('x')
# fig, ax = plt.subplots()

# Plot sns.lineplot() to the ax
# sns.set_palette('Set2')
# sns.set_style('ticks')
# sns.lineplot(df, ax=ax)
# ax.set_title('Plotting Functions in Matplotlib', size=14)
# ax.set_xlim(-5, 5)
# ax.set_ylim(-5, 25)
#
# # Despine the graph
# sns.despine()
# plt.show()
