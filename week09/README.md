# Week 09: Supervised Learning

This practical follows the lectures on learning from examples.
You implement decision tree learning and fit a linear regression model.

## Reading

AIMA Chapter 19, Sections 19.1 to 19.6.

## Tasks

- Read the `DataSet` class and the helper functions the notebook provides.
- Implement `DecisionTreeLearner` using the information gain computed for you.
- Train it on the restaurant dataset and classify new examples.
- Complete the linear regression learner and fit it to the provided data.

## Files

- `tutorial8-learning.ipynb`: the practical.
- `learning.py`: the dataset infrastructure from AIMA-Python.
- `aima-data/`: the datasets, including `restaurant.csv`.
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

A correct decision tree learner reproduces the restaurant tree from the lecture, with `Patrons` at the root, and classifies every training example correctly.
For regression, the notebook plots the line your model induces over the data, so a wrong fit is visible.
