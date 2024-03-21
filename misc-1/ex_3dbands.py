
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.ion()

kx = ky = np.linspace(-np.pi,np.pi,100)

eps = np.zeros((5,5,kx.shape[0],ky.shape[0]))

eps[0,0] = np.cos(kx[:,np.newaxis]) + np.cos(ky[np.newaxis,:])
eps[1,1] = -np.cos(kx[:,np.newaxis]) - np.cos(ky[np.newaxis,:]) + 5

mesh = np.meshgrid(kx,ky)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(mesh[0],mesh[1],eps[0,0])
ax.plot_surface(mesh[0],mesh[1],eps[1,1])

plt.show(block=True)

