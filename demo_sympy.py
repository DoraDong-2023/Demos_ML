# have similar function as mathematica
import sympy, math
from sympy import *
# function
x = sympy.Symbol('x')
print(sympy.sqrt(x) ** 2)

x, y, z, a, b, c = symbols('x, y, z, a, b, c')

# simplify
f = (2/3)*x**2 + (1/3)*x**2 + x + x + 1
f.simplify()
print(f)
# expand
f = (x+1)**2
print(expand(f))
# solve
f1 = 2*x - y + z - 10
f2 = 3*x + 2*y - z - 16
f3 = x + 6*y - z - 28
print(solve([f1, f2, f3]))
# limit
f = (x+1)**2 + 1
print(limit(f, x, a-1))# x=a-1
f = sin(x)/x
print(limit(f, x, 0))
print(limit(f, x, 0, dir='-'))# from left
f = cos(x)
dx = Symbol('dx')
print(limit(f, x, a))
print(limit(f, x, a-dx))
print(limit((limit(f,x,a)-limit(f,x,a-dx))/dx, dx, 0))
n = Symbol('n')
print(limit(((n+3)/(n+2))**n, n, oo))# inf=oo,-inf=-oo
# diff
print(diff(sin(2*x), x))
print(sin(2*x).diff(x) )
print(sin(x*y), x,2,y,3)# x 2nd-diff, y 3rd-diff
# dsolve
x = symbols("x", real=True)
print(dsolve(f(x).diff(x) + f(x)**2 + f(x), f(x)), hint="best")
# intergrate
integrate(exp(x), (x, -oo, 0))
integrate(3*x**2 + 1, x)
integrate((4/3)*x + 2*y, (x, 0, 1), (y, -x, x))
#
