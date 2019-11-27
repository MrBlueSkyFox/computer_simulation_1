from pulp import *

x1 = pulp.LpVariable("x1", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("x2", lowBound=0, cat='Integer')
problem = pulp.LpProblem('0', pulp.LpMaximize)
problem += 626 * x1 + 656 * x2, "Функция цели"
problem += 1 * x1 + 1 * x2 <= 12, "1"
problem += 1 * x1 + 0 * x2 <= 8, "2"
problem += 5 * x1 + 8 * x2 <= 81, "3"
problem += 6 * x1 + 4 * x2 <= 70, "4"
problem += 3 * x1 + 1 * x2 <= 26, "5"
problem.solve()
print("Результат:")
for variable in problem.variables():
    print(variable.name, "=", variable.varValue)
print("Passengers:")
print(value(problem.objective))
