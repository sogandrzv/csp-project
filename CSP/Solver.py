import os
import subprocess
import time
from collections import deque
from copy import deepcopy
from typing import Optional
from CSP.Constraint import Constraint
from CSP.Problem import Problem
from CSP.Variable import Variable


class Solver:

    def __init__(self, problem: Problem, use_mrv=False, use_lcv=False, use_forward_check=False):
        self.problem = problem
        self.use_lcv = use_lcv
        self.use_mrv = use_mrv
        self.use_forward_check = use_forward_check

    def is_finished(self) -> bool:
        return all([x.is_satisfied() for x in self.problem.constraints]) and len(
            self.problem.get_unassigned_variables()) == 0

    def solve(self):
        self.problem.calculate_neighbors()
        start = time.time()
        for var in self.problem.variables:
            if not self.forward_check(var):
                print("Problem Unsolvable")
                return
        result = self.backtracking()
        end = time.time()
        time_elapsed = (end - start) * 1000
        if result:
            print(f'Solved after {time_elapsed} ms')
        else:
            print(f'Failed to solve after {time_elapsed} ms')

    def backtracking(self):

        if self.is_finished():
            return True

        var = self.select_unassigned_variable()
        for value in self.order_domain_values(var):
            var.value = value
            if self.is_consistent(var):
                if self.use_forward_check:
                    self.forward_check(var)
                result = self.backtracking()
                if result:
                    return True
        var.value = None

        return False

    def forward_check(self, var):
        for neighbor in var.neighbors:
            if not neighbor.has_value:
                for neighbour_value in neighbor.domain:
                    neighbor.value = neighbour_value
                    if not self.is_consistent(neighbor):
                        neighbor.domain.remove(neighbour_value)
                    neighbor.value = None
                    if len(neighbor.domain) == 0:
                        return False

        return True

    def select_unassigned_variable(self) -> Optional[Variable]:
        if self.use_mrv:
            return self.mrv()
        unassigned_variables = self.problem.get_unassigned_variables()
        return unassigned_variables[0] if unassigned_variables else None

    def order_domain_values(self, var: Variable):
        if self.use_lcv:
            return self.lcv(var)
        return var.domain

    def mrv(self) -> Optional[Variable]:
        min_remaining_values = float('inf')
        selected_variable = None

        unassigned_var = self.problem.get_unassigned_variables()
        for var in unassigned_var:
            if len(var.domain) < min_remaining_values:
                selected_variable = var
                min_remaining_values = len(var.domain)

        return selected_variable

    
    def is_consistent(self, var: Variable):
        for constraint in self.problem.constraints:
            if var in constraint.variables and not constraint.is_satisfied():
                return False
        return True

    def lcv(self, var: Variable):
        values = sorted(var.domain, key=lambda x: self.count_inconsistency(var))
        return values

    def count_inconsistency(self, var):
        count = 0
        for val in var.domain:
            var.value = val
            if not self.is_consistent(var):
                count += 1
        return count
