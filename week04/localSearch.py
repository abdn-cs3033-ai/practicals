from time import time
from types import FunctionType
from nqueens import SearchProblem


class localSearch(object):
    """Testing rig for local search algorithms.
    """
    def localSearch(self, problem: SearchProblem, search_type: FunctionType, i: int):
        """Tests a local search algorithm

        Args:
            problem (SearchProblem): A local search problem
            search_type (FunctionType): A local search algorithm
            i (int): number of repetitions for each algorithm being tested

        Returns:
            _type_: _description_
        """
        n_iterations = i
        cnt = 0
        start = time()
        s = []
        for i in range(n_iterations):
            result = search_type(problem)
            # print("Current state is "+str(result)+" h="+str(problem.heuristic(result)))
            if problem.heuristic(result) == 0:
                cnt += 1
                s.append(result)
        print(" - Hit rate: %2d/%d\tRuntime: %f" % (cnt, n_iterations, time() - start))
        return s
