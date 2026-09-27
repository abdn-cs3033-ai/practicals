# Week 07: Planning Formalisms

This practical follows the lectures on planning.
You formalise two planning domains in PDDL and run a planner on them.

## Reading

AIMA Chapter 11, Section 11.1, and the PDDL guide referenced in the lecture.

## Tasks

- Encode the cup of tea domain and its problem from the description in `tutorial6-pddl.md`.
- Extend the blocks world domain to a robot with two grippers.
- Run a planner on each problem and analyse the plans it returns.

## Files

- `tutorial6-pddl.md`: the practical, with the description of both domains.
- `cup_of_tea/domain.pddl`: the cup of tea domain with its two actions left for you to write.
- `cup_of_tea/problem.pddl`: the cup of tea problem, given in full.
- `cup_of_tea/solution.plan`: the plan a planner finds once the domain is right, for you to compare against.
- `blocksworld/blocksworld.pddl` and `blocksworld/demo.pddl`: the single-gripper blocks world domain and a problem, which you extend to two grippers.
- `setting-up-a-local-planner.md`: how to run a planner on your own machine instead of in the browser.

## Setup

Use the online editor and planner at <http://editor.planning.domains>, which needs no installation.
Alternatively, edit the files locally with the VSCode PDDL plugin, following `setting-up-a-local-planner.md`.

## Checking your work

The planner is your check.
If it returns a plan, read the plan and confirm it achieves the goal you meant to state.
For the cup of tea domain, compare it with `cup_of_tea/solution.plan`; a different plan of the same length is fine, since the problem admits more than one.
If it returns no plan, the domain or the problem is wrong, and the error messages from the editor tell you where to look.
