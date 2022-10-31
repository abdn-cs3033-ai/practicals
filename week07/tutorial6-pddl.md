# CS3033: Artificial Intelligence

## Tutorial 06: Planning Formalisms

#### Prof. Felipe Meneguzzi

Adapted from code in the [AI Planning Community Modelling](https://github.com/AI-Planning/modeling-in-pddl) public repository.

---

## PDDL Formalisation

In this tutorial, we will formalise two domains in PDDL:

1. [Cup of tea for grandpa](#cup-of-tea-for-grandpa)
2. [Extended BlocksWorld](#extended-blocksworld)

Your task is to read the description of the domains and encode both the domain description (i.e. the operator descriptions) and the problems described. You will accomplish this by filling in the template files provided in this repository.

### Planning.Domains

In order to run this tutorial, we will use an online PDDL Editor and Planner available at [editor.planning.domains](http://editor.planning.domains). This web tool includes both a syntax-highlighting element and an underlying planning algorithm that solves problems described in PDDL. 

Alternatively, you can use the VSCode-based PDDL plugin and work offline on the files made available in this repository. 

Editor.Planning.Domains Tutorial

[![](http://img.youtube.com/vi/HCVoVtAFkLo/0.jpg)](http://www.youtube.com/watch?v=HCVoVtAFkLo "Micro Tutorial on Editor")

VScode PDDL Tutorial: 

[![](http://img.youtube.com/vi/XW0z8Oik6G8/0.jpg)](http://www.youtube.com/watch?v=XW0z8Oik6G8 "PDDL Modeling Course")

---

### Cup of tea for grandpa

You have a robot and grandpa. Robot can pick up a cup of tea in the kitchen and deliver it to grandpa, who deserves it. Grandpa may be in either the kitchen or the living room. The robot can move through the doorway between the kitchen and living room. We provide two PDDL files for you to get started, and a reference plan created using our formalisation:

1. [Domain](cup_of_tea/domain.pddl)
2. [Problem](cup_of_tea/problem.pddl)
3. [Solution Plan](cup_of_tea/solution.plan)

Hint: modify the problem file to be able to develop the domain incrementally and test each new action.

For example: to unit test the _pick-up cup_ action, set the goal this way:

```lisp
(:goal
    ;(delivered cup-of-tea grandpa)
    (and
        (holding cup-of-tea)
        (not (handempty))
    )
)
```

Similarly, to test the move action, define the goal this way:

```lisp
(:goal
    ;(delivered cup-of-tea grandpa)
    (and
        (in living-room)
        (not (in kitchen))
    )
)
```

#### Challenges

- What if you have two cups and two thirsty grand parents in two different rooms?
- Rooms are separated by walls. What if some rooms are not interconnected by door ways?

#### Credits

Maria Fox, Derek Long, Schlumberger AI Planning course

---

### Extended BlocksWorld

Objective: Change the BlocksWorld domain so that there are 2 (or more) grippers instead of the implicit single gripper. Similar to the previous formalisation, we provide a few files to get you started:

1. [Domain](blocksworld/blocksworld.pddl)
2. [Problem](blocksworld/demo.pddl)
3. [Solution Plan](cup_of_tea/solution.plan)

#### Things to consider

- What types do we need to add?
- What predicates do we need to change?
- What objects do we need to add?
- How do we change the actions?

#### Testing your solution

Run the planner by right-clicking on the domain or problem files and selecting _PDDL: Run the planner and display the plan_.
You can try to build the problem file visually, or just animate your plan on the [Blocksworld animation](https://blocks-dot-ai-planning.appspot.com/) page.

#### Need help?

The PDDL constructs exercised are:

- [Types](https://planning.wiki/ref/pddl/domain#object-types)
- [Objects](https://planning.wiki/ref/pddl/problem#objects)

If you are unsure where to start, the live coding demo is in this video: [Modeling in PDDL - Episode 1 - Blocksworld](https://youtu.be/_NOVa4i7Us8).

#### Credits

Jan Dolejší, Schlumberger AI Planning course