# Week 03: Search and Heuristics

This practical follows the lectures on uninformed and heuristic search.
You implement greedy best-first search and A* search and use them to solve instances of the 8-puzzle.

## Reading

AIMA Chapter 3, in particular Sections 3.5 and 3.6 on informed search and heuristics.

## Tasks

- Implement `GreedyBestFirstSearch` by translating the pseudocode from the lecture into Python.
- Implement `AStarSearch` in the same way.
- Implement the Manhattan distance heuristic for the 8-puzzle and compare it with the misplaced-tiles heuristic.

## Files

- `tutorial2-search.ipynb`: the practical.
- `notebook.py`: helper code the notebook imports.
- `requirements.txt`: the extra package the notebook needs.

## Setup

Open the notebook in Jupyter, or in Colab through the badge at the top of the notebook.
In Colab, the first code cell clones this repository and installs what the notebook needs.
Locally, install the extra package first:

```bash
pip install -r requirements.txt
```

## Checking your work

The Testing section at the end of the notebook runs a set of unit tests against your implementation.
Run that cell after each change.
A failing test prints the case that failed and the result it expected.
