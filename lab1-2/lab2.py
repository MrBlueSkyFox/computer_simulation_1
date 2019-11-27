from sympy import init_printing

init_printing()
from sympy import Symbol, Function, Derivative, dsolve, solve, pprint

x = Symbol('x')
y = Function('y')(x)
dy = Derivative(y)
F = 2 * y - y * dy + x * dy ** 2
F.doit()
print(F)
dFdy = Derivative(F, y)
dFd1y = Derivative(F, dy)
dFdy.doit()
dFd1y.doit()
L = dFdy - Derivative(dFd1y, x)
sol = dsolve(L)
print("Общее решение: \n")
print(sol)
eq1 = sol.subs({x: 3, y: 4})
eq2 = sol.subs({x: 1, y: 1})
coeffs = solve([eq1, eq2])
print(coeffs)
res = sol.subs(coeffs)
print('\nИтоговый вид экстремали: \n')
print(res.evalf())
print('y(x) = x+ log3(x)')
pprint(res)
