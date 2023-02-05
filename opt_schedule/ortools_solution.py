from ortools.linear_solver import pywraplp
from math import floor
import numpy as np
import os

def create_data_model(path='test.txt'):
    """Create the data for the example."""
    with open(path, "r") as file:
            # read the file line by line
        lines = file.readlines()
        # convert each line to integer and append to the list
    
        read_file= [[int(i)for i in line.strip().split(' ')] for line in lines]
    
    read_file=np.array(read_file)
    data={}
    data['num_prod'] = read_file[0][0]
    data['min_num'] = read_file[4]
    data['cost'] = read_file[1]
    data['total_cost'] = read_file[0][2]
    data['area_cost'] = read_file[2]
    data['area'] = read_file[0][1]
    data['upper_bound'] = [floor(min([data['total_cost']/data['cost'][i], data['area']/data['area_cost'][i]])) for i in range(data['num_prod'])]  #[read_file[0][1]/i for i in read_file[1]]
    data['profit'] = read_file[3]
    

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
        print('Total profit:', round(objective.Value()))

        for i in range(data['num_prod']):
            if x[i].solution_value() > 0:
                print('Product', i+1, '- profit:', data['profit'][i], '- cost:', data['cost'][i], '- area required:', data['area_cost'][i], '- minimum quantity:', data['min_num'][i], '- quantity:', int(x[i].solution_value()))
    else:
        print('The problem does not have an optimal solution.')


if __name__ == '__main__':
    main()