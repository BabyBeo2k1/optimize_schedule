from ortools.linear_solver import pywraplp
from math import floor
import numpy as np

def create_data_model():
    """Create the data for the example."""
    data = {}
    min_num = np.random.randint(low=20, high=50, size=12)
    cost = np.random.uniform(low=20, high=60, size=(12,))
    total_cost = 6000
    area_cost = np.random.uniform(low=20, high=60, size=(12,))
    area = 10000
    profit = np.random.uniform(low=100, high=200, size=(12,))
    num_prod = len(cost)

    upper_bound = [floor(min([total_cost/cost[i], area/area_cost[i]])) for i in range(num_prod)]

    data['min_num'] = min_num
    data['cost'] = cost
    data['total_cost'] = total_cost
    data['area_cost'] = area_cost
    data['area'] = area
    data['upper_bound'] = upper_bound
    data['profit'] = profit
    data['num_prod'] = num_prod

    return data

def main():
    data = create_data_model()

    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Variables
    x = {}
    for i in range(data['num_prod']):
        x[i] = solver.IntVar(0, data['upper_bound'][i], f"x_{i}")

    u = {}
    for i in range(data['num_prod']):
        u[i] = solver.IntVar(0, 1, f"u_{i}")


    # Constraints
    # The cost and area is limited.
    solver.Add(sum(x[i] * data['cost'][i] for i in range(data['num_prod'])) <= data['total_cost'])

    solver.Add(sum(x[i] * data['area_cost'][i] for i in range(data['num_prod'])) <= data['area'])

    for i in range(data['num_prod']):
        solver.Add(u[i]*data['min_num'][i] <= x[i])
        solver.Add(u[i]*data['upper_bound'][i] >= x[i])

    # Objective
    objective = solver.Objective()

    for i in range(data['num_prod']):
        objective.SetCoefficient(x[i], data['profit'][i])
    objective.SetMaximization()

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print("Cost limit:", data['total_cost'])
        print("Area limit:", data['area'])
        print('Total profit:', int(objective.Value()))

        for i in range(data['num_prod']):
            if x[i].solution_value() > 0:
                print('Product', i+1, '- profit:', data['profit'][i], '- cost:', data['cost'][i], '- area required:', data['area_cost'][i], '- minimum quantity:', data['min_num'][i], '- quantity:', int(x[i].solution_value()))
    else:
        print('The problem does not have an optimal solution.')


if __name__ == '__main__':
    main()