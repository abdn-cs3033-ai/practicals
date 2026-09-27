# Week 05: Constraint Satisfaction

This practical follows the lectures on constraint satisfaction and on logic and inference.
You describe two problems as sets of constraints and let the Z3 solver find the solutions.

## Reading

AIMA Chapter 6, and Chapter 7 for the connection between constraints and satisfiability.

## Tasks

- Encode the N-Queens problem as constraints over one integer variable per queen.
- Compare the size of this encoding with the local search implementation from week 04.
- Encode Sudoku as constraints and solve a given puzzle.

## Files

- `tutorial4-csp.ipynb`: the practical.
- `printBoard.py`: draws a board.
- `requirements.txt`: the Z3 solver package.

## Setup

Open the notebook in Jupyter, or in Colab through the badge at the top of the notebook.
In Colab, the first code cell clones this repository and installs Z3.
Locally, install it first:

```bash
pip install -r requirements.txt
```

## Checking your work

Each solving cell is followed by a validity check.
The check asserts that the solution Z3 returned satisfies the problem, so it accepts any valid solution rather than one fixed answer.
An `AssertionError` in a check means the constraints in the cell above it are wrong.
