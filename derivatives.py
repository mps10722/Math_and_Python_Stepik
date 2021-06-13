import matplotlib.pyplot as plt
import numpy_ex as np


def f(value):
    return round(np.exp(value), 3)


def g(value):
    return a * value + b


x0 = 110
dx = 0.001
a = (f(x0 + dx) - f(x0)) / dx
b = f(x0) - a * x0
x = np.arange(-100, 100, 0.1)
y = []
y2 = []
print(f'x: {3}, f(x): {round(f(x0), 3)}, g(x0): {round(g(x0), 3)}, '
      f'alpha: {round(np.arctan(g(x0)), 2) * 180 / np.pi}deg')
for v in x:
    y.append(f(v))
    y2.append(g(v))
    # print(f'x: {v}, f(x): {round(y[-1])}')


#  Range x_min, x_max, y_min, y_max
plt.axis([-1000, 1000, -5, 1000])

#  Set text attributes for line names
plt.xlabel('x', fontweight='bold', fontsize=14)
plt.ylabel('y', rotation=0, fontweight='bold', fontsize=14)

#  Grid attributes
# Show the major grid lines
plt.grid(b=True, which='major', linewidth=0.5)

# Show the minor grid lines
plt.minorticks_on()
plt.grid(b=True, which='minor', linewidth=0.25)

#  Bold zero axis
plt.axhline(y=0, color='#000', linewidth=0.7)
plt.axvline(x=0, color='#000', linewidth=0.7)

#  Adjust paddings
plt.tight_layout()

#  Plots attributes
plt.plot(x, y,
         color='#222299',
         # marker='.',
         markeredgecolor='#880000',
         markerfacecolor='#880000',
         linewidth=0.8,
         label='f(x)')
plt.plot(x, y2,
         color='#229922',
         # marker='.',
         markeredgecolor='#880000',
         markerfacecolor='#880000',
         linewidth=0.8,
         label='g(x)')

#  Show legend (with attributes)
plt.legend(prop={'weight': 'bold'})

#  Show plot window
plt.show()
