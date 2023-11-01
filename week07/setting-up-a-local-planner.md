
# CS3033: Artificial Intelligence

## Tutorial 06: Planning Formalisms

#### Prof. Felipe Meneguzzi

In this guide, you will learn how to use various planners for solving problems specified in PDDL. PDDL is a widely-used language for representing planning problems in artificial intelligence. Different planners can be used to find solutions to PDDL problems, and this guide will walk you through the steps.

## Prerequisites

Before you begin, ensure you have a way to locally edit PDDL files on your system. This can be achieved by something like a text editor, or more preferably, this should be done using VSCode with the [PDDL plugin](https://marketplace.visualstudio.com/items?itemName=jan-dolejsi.pddl) enabled.

## Planner Selection

### 1. Fast Downward

Fast Downward is a domain-independent classical planning system. It can deal with general deterministic planning problems encoded in the propositional fragment of PDDL2.2.

Fast Downward uses a hierarchical decomposition of planning tasks for computing its heuristic function, called the causal graph heuristic. This heuristic is very different from traditional HSP-like heuristics based on ignoring negative interactions of operators.

It is known for its speed and ability to solve a wide range of planning problems. It is one of the most popular planning systems in use today, and it is used by researchers and practitioners in a variety of fields, including robotics, logistics, and scheduling.

---

### Installation

**Linux/MacOS:** you need a C++ compiler, CMake and GNU make.
  To run the planner, you also need Python 3.

  On Debian/Ubuntu, the following should install all these dependencies:
  ```
  sudo apt install cmake g++ make python3
  ```

  You will also be required to clone the `downward` repository:
  ```bash
  git clone https://github.com/aibasel/downward.git
  ```
  
  To build the planner:
```bash
cd path/to/downward
chmod 700 ./build.py
./build.py
```

**Windows:** install [Visual Studio >= 2017](https://visualstudio.microsoft.com/de/vs/older-downloads/), [Python](https://www.python.org/downloads/windows/), and [CMake](http://www.cmake.org/download/). During the installation of Visual Studio, the C++ compiler is not installed by default, but the IDE prompts you to install it when you create a new C++ project.

---

### Compiling on Windows

Windows does not interpret the shebang in Python files, so you have to call `build.py` as `python3 build.py` (make sure `python3` is on your `PATH`). Also note that options are passed without `--`, e.g., `python3 build.py build=debug`.

Note that compiling from the terminal is only possible with the right environment. The easiest way to get such an environment is to use the `Developer PowerShell for VS 2019` or `Developer PowerShell`.

Alternatively, you can [create a Visual Studio Project](https://www.fast-downward.org/ForDevelopers/CMake#Custom_Builds), open it in Visual Studio and build from there. Visual Studio creates its binary files in subdirectories of the project that our driver script currently does not recognise. If you build with Visual Studio, you have to run the individual components of the planner yourself.

If you are not familiar with the individual compilation and installation steps for windows, and have access to the Windows Subsystem for Linux (WSL), please use that instead and follow the instructions above.

---

### Testing Your Installation
To test your build, `cd` into the directory containing your built `fast-downward` file, and run:
```bash
./fast-downward.py misc/tests/benchmarks/miconic/s1-0.pddl --search "astar(lmcut())"
```
If a solution is found, then your installation is complete, and you can now use fast downward any PDDL problem it can handle.

---

### Troubleshooting
* If you changed the build environment, delete the `builds` directory and rebuild.
* **Windows:** If you cannot execute the Fast Downward binary in a new command line, then it might be unable to find a dynamically linked library.
  Use `dumpbin /dependents PATH\TO\DOWNWARD\BINARY` to list all required libraries and ensure that they can be found in your `PATH` variable.
* **MacOS:** If your compiler doesn't find flex or bison when building VAL, your include directories might be in a non-standard location. In this case you probably have to specify where to look for includes and libraries in VAL's   
  Makefile (probably `/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr`).
  
---
### Usage
To use the Fast Downward planner, you can use the following commands. Please note that each command _should_ return you a plan - assuming that your problem and domain files are valid, and that your goal state can be achieved.
```bash
# landmark-cut heuristic
 ./fast-downward.py domain.pddl task.pddl --search "astar(lmcut())"
 
# iPDB heuristic with default settings
 ./fast-downward.py domain.pddl task.pddl --search "astar(ipdb())"
 
# blind heuristic
 ./fast-downward.py domain.pddl task.pddl --search "astar(blind())"
 
## using FF heuristic and context-enhanced additive heuristic (previously: "fFyY")
 ./fast-downward.py domain.pddl task.pddl \
 --evaluator "hff=ff()" --evaluator "hcea=cea()" \
 --search "lazy_greedy([hff, hcea], preferred=[hff, hcea])"
  
## using FF heuristic (previously: "fF")
 ./fast-downward.py domain.pddl task.pddl \
 --evaluator "hff=ff()" \
 --search "lazy_greedy([hff], preferred=[hff])"
  
## using context-enhanced additive heuristic (previously: "yY")
 ./fast-downward.py domain.pddl task.pddl \
 --evaluator "hcea=cea()" \
 --search "lazy_greedy([hcea], preferred=[hcea])"
```
Note that the fast-downward planner has a few key components:
- `domain.pddl` - this is the domain file relating to the problem you wish to solve.
- `task.pddl` - this is the problem that runs on the domain.
-- If either (or both) of your domain or problem files happen to be in other directories, you will have to provide the path to them.
- `--search "..."` provides the search algorithm with specific settings. For example, `--search "astar(lmcut())"` indicates the use of the A* search with the landmark-cut heuristic.
-- Run each of the above with one of your problems. 
-- Do you notice anything about the results that get given to you?
-- Do you always get a result back?
-- How timely is the planner?

---

### 2. ENHSP - Expressive Numeric Heuristic Planner
 ENHSP is a forward heuristic search planner, but it is expressive in that it can handle:
1. Classical Planning
2. Numeric Planning with linear and non-linear expressions
3. Planning with discretised autonomous processes and events
4. Global constraints, which are the analogous of always constraints of PDDL

The planner reads in input a PDDL domain and problem file, and if you are lucky and your problem is not too complex, it provides you with a plan (a sequence of actions). In the case of planning with processes, the plan is a time-stamped plan (associated to each action, you find the time at which that instance of the action has to be executed). In dealing with autonomous processes, ENHSP discretises the problem (with a delta=1sec by default); so the plan is guaranteed to be valid only with respect to that discretisation.

The input language for the planner is PDDL. PDDL is the standard de facto language to express planning problems. The domain file expresses the signature of your predicates, functions and all the actions/processes/events available, in a parametrized way. The problem file expresses the particular instance of the planning problem (e.g., what is the initial value of predicate A? What is the goal?). For more information on PDDL I suggest you to start from [its wikipedia page](https://en.wikipedia.org/wiki/Planning_Domain_Definition_Language#cite_note-opt-15), and follow the links. ENHSP supports PDDL 2.1 in particular, and PDDL+ (for the support of autonomous processes) and also events (only recently introduced). We also allow to employ global constraint as a direct construct of the language (via the :constraint syntax).

The planner has been developed taking ideas from different papers (heuristics, decoupled deltas for discretisation): 
E. Scala, P. Haslum, S. Thiebaux: **Heuristics for Numeric Planning via Subgoaling**, IJCAI 2016
E. Scala, P. Haslum, S. Thiebaux, M. Ramirez, **Interval-Based Relaxation for General Numeric Planning**, ECAI 2016
E. Scala, P. Haslum, D. Magazzeni, S. Thiebaux: **Landmarks for Numeric Planning Problems**, IJCAI 2017
M. Ramirez, E. Scala, P. Haslum, S. Thiebaux: **Numerical Integration and Dynamic Discretization in Heuristic Search Planning over Hybrid Domains** in arXiv
D. Li, E. Scala, P. Haslum, S. Bogomolov **Effect-Abstraction Based Relaxation for Linear Numeric Planning** In IJCAI 2018

The planner builds on the PPMaJaL library, which can be found [here](https://gitlab.com/enricos83/PPMAJAL-Expressive-PDDL-Java-Library). PPMaJaL provides parsing, data structures, heuristics and search engine for ENHSP.

---

### Installation 

To save the hassle of compiling ENHSP, the developers have put the Java binary of ENHSP up on Google Drive, readily available for you to download [here](https://drive.google.com/file/d/1GfVLQNEgeeNnNeI6HkrCtAUrrSzdSW8g/view?usp=sharing).

You shall also be required to have **at least** Java 15 installed for the planner to work correctly. Versions can be found on the [Oracle](https://www.oracle.com/uk/java/technologies/downloads/) page. Install whichever distribution & version you require for your operating system.

---

### Usage
The planner can be run by using the following command:
```bash
java -jar path/to/enhsp/enhsp.jar -o /path/to/domain/<domain_file> -f /path/to/problem/<problem_file>
```
Should you wish to run the planner with specific search options, you can add options to it:
```bash
java -jar path/to/enhsp/enhsp.jar -o /path/to/domain/<domain_file> -f /path/to/problem/<problem_file> -planner "<heuristic>"
```
Where `<heuristic>` can be replaced with one of `"sas" "opt" "aibr" "lm_opt" "sat-hmrp" "sat-hmrph" "sat-hmrphj" "sat-hadd" "sat-hradd" "sat-aibr" "sat-haddabs" "opt-hmax" "opt-hrmax"  "opt-hlm" "opt-hlmrc"`.

If you are finding that you are running out of heap space, feel free to add the maximum memory allocation flag to your command. `5G` is 5GB, `512M` would be 512MB, etc.
```bash
java -Xmx5G -jar .... 
```

## Acknowledgments

This material was adapted from the [FastDownward](https://github.com/aibasel/downward) and [ENHSP](https://gitlab.com/enricos83/ENHSP-Public) repositories.
