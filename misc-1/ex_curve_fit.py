
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

xs = np.linspace (0,10,100)
ys = np.sin(xs) + np.random.random(xs.shape[0])

fit = curve_fit (lambda x,a,b: b+np.sin(a*x),xs,ys)

plt.plot (xs,ys)
plt.plot (xs,np.sin(xs*fit[0][0])+fit[0][1])

plt.show()

