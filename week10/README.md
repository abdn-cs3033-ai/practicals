# Week 10: Reinforcement Learning

This practical follows the lecture on reinforcement learning.
It is a bonus practical: there is no timetabled session for it, and it is not assessed, so work through it in your own time if the lecture interested you.
You implement a passive temporal-difference agent and an active Q-learning agent, and compare what they learn against the optimal solution of the underlying MDP.

## Reading

AIMA Chapter 22.

## Tasks

- Implement the update of the passive TD agent.
- Compare its utility estimates with those from value iteration.
- Implement the update of the Q-learning agent.
- Compare the policy it learns with the optimal policy.

## Files

- `tutorial9-rl.ipynb`: the practical.
- `mdp4e.py`: the MDP implementation from week 08, used as the oracle to compare against.
- `utils4e.py` and `notebook.py`: helper code the notebook imports.
- `requirements.txt`: the plotting and data packages the notebook needs.

## Setup

Open the notebook in Jupyter, or in Colab through the badge at the top of the notebook.
In Colab, the first code cell clones this repository and installs the packages.
Locally, install them first:

```bash
pip install -r requirements.txt
```

## Checking your work

The notebook computes the optimal utilities and policy with value iteration and plots them next to what your agents learn.
The estimates converge towards the value iteration results as the number of trials grows, and the learned policy must match the optimal one in the states the agent visits often.
