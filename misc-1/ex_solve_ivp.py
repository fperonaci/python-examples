
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def pend(t, y, b, c):
  theta, omega = y
  dydt = [omega, -b*omega - c*np.sin(theta)]
  return dydt

b = 0.25
c = 5.0

y0 = [np.pi-0.1,0.0]
t = np.linspace(0,10,101)

sol = solve_ivp(lambda t,y: pend(t,y,b,c), t_span=(0,10), y0=y0, t_eval=t)

plt.plot(sol.t, sol.y[0], 'b', label='theta(t)')
plt.plot(sol.t, sol.y[1], 'g', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()

