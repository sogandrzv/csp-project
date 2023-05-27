from CSP.Constraint import Constraint


class ChemistConstraint(Constraint):
    def is_satisfied(self) -> bool:
        if self.variables[0].value == "red" and self.variables[0].value == "green" and self.variables[
            5].value != "different":
            return False

        if self.variables[1].value != "blue" and self.variables[6].value == "acid" and self.variables[
            6].value != "healing":
            return False

        if self.variables[2].value == "purple" and self.variables[2].value == "black" and self.variables[
            7].value != "poison":
            return False

        if self.variables[3].value != "green" and self.variables[8].value == "poison":
            return False

        if self.variables[4].value == "black" and self.variables[4].value == "blue" and self.variables[
            9].value != "invisible":
            return False
