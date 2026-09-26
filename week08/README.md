# Week 08: Markov Decision Processes

This practical follows the lecture on stochastic planning.
You implement the two classic algorithms for solving a Markov decision process and study how its parameters change the optimal policy.

## Reading

AIMA Chapter 17, Sections 17.1 to 17.3.

## Tasks

- Implement the Bellman update inside value iteration.
- Implement policy extraction from a utility function.
- Implement policy iteration.
- Reproduce the four reward settings from the lecture and explain the policy each one produces.

## Files

- `tutorial7-mdp.ipynb`: the practical.
- `utils4e.py`: helper functions from AIMA-Python.
- `notebook.py`: helper code the notebook imports.

## Setup

Open the notebook in Jupyter, or in Colab through the badge at the top of the notebook.
In Colab, the first code cell clones this repository.
The notebook needs no packages beyond the root `requirements.txt`.

## Checking your work

The notebook runs your algorithms on the 4x3 grid world from the lecture and AIMA Section 17.1, and draws the resulting utilities and policy.
Compare them with the ones in the book and the lecture slides.
Value iteration and policy iteration must agree on the optimal policy.
