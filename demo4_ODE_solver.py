# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 10:48:42 2022

@author: https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html

usage: A demo for solving ODE function using scipy 
"""

from scipy.integrate import solve_ivp
# tut1
def exponential_decay(t, y):
    return -0.5 * y
sol = solve_ivp(exponential_decay, [0, 10], [2, 4, 8],
                t_eval=[0, 1, 2, 4, 10])
print(sol.t)
print(sol.y)





def upward_cannon(t, y):
    return [y[1], -0.5]
def hit_ground(t, y):
    return y[0]
def apex(t, y):
    return y[1]

hit_ground.terminal = True
hit_ground.direction = -1
sol = solve_ivp(upward_cannon, [0, 100], [0, 10], events=(hit_ground,apex), dense_output=True)
print(sol.t_events)
print(sol.t)
print(sol.sol(sol.t_events[1][0]))
print(sol.y_events)

def lotkavolterra(t, z, a, b, c, d):
    x, y = z
    return [a*x - b*x*y, -c*y + d*x*y]
    
sol = solve_ivp(lotkavolterra, [0, 15], [10, 5], args=(1.5, 1, 3, 1),
                dense_output=True)

t = np.linspace(0, 15, 300)
z = sol.sol(t)
import matplotlib.pyplot as plt
plt.plot(t, z.T)
plt.xlabel('t')
plt.legend(['x', 'y'], shadow=True)
plt.title('Lotka-Volterra System')
plt.show()


