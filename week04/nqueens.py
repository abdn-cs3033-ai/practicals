from random import choice
from collections import Counter
from random import randrange
from typing import Any, Collection


class SearchProblem:
    def __init__(self, initial=None):
        """Creates a local search problem

        Args:
            initial (_type_, optional): an explicit initial state. Defaults to None.
        """
        pass

    def initial(self):
        """Returns the initial state of the problem"""
        pass

    def goal_test(self, state) -> bool:
        """Returns whether state is a goal state
        """
        pass

    def heuristic(self, state) -> int:
        """Returns the heuristic/objective value for state"""
        pass

    def nearStates(self, state) -> Collection:
        """Returns the set of neighbouring states to the current state"""
        pass

    def randomNearState(self, state) -> Any:
        """Picks a random neighbour"""
        return choice(self.nearStates(state))


class NQueensSearch(SearchProblem):
    def __init__(self, N):
        self.N = N

    def initial(self):
        return list(randrange(self.N) for i in range(self.N))

    #   Tests if any row / column / diagonal is populated by more than one queen
    def goal_test(self, state):
        a, b, c = (set() for i in range(3))
        for row, col in enumerate(state):
            if col in a or row - col in b or row + col in c:
                return False
            a.add(col)
            b.add(row - col)
            c.add(row + col)
        return True

    # Heuristic: h
    #   Number of pairs of queens attacking each other
    def heuristic(self, state):
        a, b, c = [Counter() for i in range(3)]
        for row, col in enumerate(state):
            a[col] += 1
            b[row - col] += 1
            c[row + col] += 1
        h = 0
        for count in [a, b, c]:
            for key in count:
                h += count[key] * (count[key] - 1) / 2
        return -h

    def nearStates(self, state):
        near_states = []
        for row in range(self.N):
            for col in range(self.N):
                if col != state[row]:
                    aux = list(state)
                    aux[row] = col
                    near_states.append(list(aux))
        return near_states
