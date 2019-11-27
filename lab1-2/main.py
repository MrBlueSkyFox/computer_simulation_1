from scipy.optimize import linprog
A = [
    [1, 1],
    [1, 0],
    [5, 8],
    [6, 4],
    [3, 1]
]
b = [12, 8, 81, 70, 26]
c = [-626, -656]
bounds = (0, None)
res = linprog(c, A_ub=A, b_ub=b, bounds=[bounds, bounds])

print('x1 =', round(res.x[0], 3))
print('x2 =', round(res.x[1], 3))
print('f(x) =', round(res.x[0] * -c[0] +
                      res.x[1] * -c[1], 3))

