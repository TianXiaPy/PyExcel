import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

x = np.arange(0, 10)
y = np.exp(-x / 3.0)
help(np.exp)
f = interpolate.interp1d(x, y)
xnew = np.arange(0, 9, 0.1)
ynew = f(xnew)  # use interpolation function returned by `interp1d`
plt.plot(x, y, 'o', xnew, ynew, '-')
plt.show()
