# Week 04: Local Search

This practical follows the lecture on local search.
You solve the N-Queens problem with three local search algorithms and compare how they behave.

## Reading

AIMA Chapter 4, Sections 4.1 and 4.2.

## Tasks

- Implement hill climbing.
- Implement hill climbing with random restarts.
- Implement simulated annealing.
- Compare the three algorithms on boards of increasing size.

The notebook fixes the API each algorithm must follow, so the checking code can call your implementation.
How you organise the rest of the code is up to you.

## Files

- `tutorial3-local-search.ipynb`: the practical.
- `nqueens.py`: the `NQueensSearch` problem model your algorithms search over.
- `localSearch.py`: the checking code the notebook runs against your implementation.
- `printBoard.py`: draws a board.

## Setup

Open the notebook in Jupyter, or in Colab through the badge at the top of the notebook.
In Colab, the first code cell clones this repository.
The notebook needs no packages beyond the root `requirements.txt`.

## Checking your work

The section titled Test your code runs each of your algorithms against a reference implementation.
For each algorithm it runs several searches and prints the hit rate, that is how many of them reached a goal state, and the total runtime.
Hill climbing can legitimately stop at a local optimum, so expect a hit rate below 100% for plain hill climbing and compare it with the other two.
