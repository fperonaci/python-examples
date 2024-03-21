
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root

def fun(x):
  return [fun1(x),fun2(x)]

def fun1(x):
  return x[0]+0.5*(x[0]-x[1])**3-1

def fun2(x):
  return 0.5*(x[1]-x[0])**3+x[1]

def jac(x):
  return [jac1(x),jac2(x)]

def jac1(x):
  return 1+1.5*(x[0]-x[1])**2,-1.5*(x[0]-x[1])**2

def jac2(x):
  return -1.5*(x[1]-x[0])**2,1+1.5*(x[1]-x[0])**2,

sol = root(fun=fun,x0=[0,0],jac=jac)

print(sol.success)

