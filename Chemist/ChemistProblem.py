from CSP.Problem import Problem
from CSP.Variable import Variable
from Chemist.ChemistConstraint import ChemistConstraint


class ChemistProblem(Problem):

    def __init__(self):
        super().__init__([], [], "Chemist Problem")

        x1 = Variable[str](['green', 'red', 'black', 'purple', 'blue'], 'aldo')
        x2 = Variable[str](['green', 'red', 'black', 'purple', 'blue'], 'beaatris')
        x3 = Variable[str](['green', 'red', 'black', 'purple', 'blue'], 'ignatious')
        x4 = Variable[str](['green', 'red', 'black', 'purple', 'blue'], 'lorenzo')
        x5 = Variable[str](['green', 'red', 'black', 'purple', 'blue'], 'orsolla')

        y1 = Variable[str](['acid', 'poison', 'healing', 'different', 'invisible'], 'aldo1')
        y2 = Variable[str](['acid', 'poison', 'healing', 'different', 'invisible'], 'beaatris1')
        y3 = Variable[str](['acid', 'poison', 'healing', 'different', 'invisible'], 'ignatious1')
        y4 = Variable[str](['acid', 'poison', 'healing', 'different', 'invisible'], 'lorenzo1')
        y5 = Variable[str](['acid', 'poison', 'healing', 'different', 'invisible'], 'orsolla1')

        c0 = ChemistConstraint([x1, x2, x3, x4, x5, y1, y2, y3, y4, y5])
        self.constraints = [c0]
        self.variables = [x1, x2, x3, x4, x5, y1, y2, y3, y4, y5]
