# Querying Graph Databases using z3 SAT Solver

## Overview
- Developed as part of the Automated Reasoning course at RPTU Kaiserslautern, this project focuses on the innovative application of the z3 SAT solver for querying graph databases. 

- The project integrates the capabilities of z3, a renowned SMT (Satisfiability-Module-Theory) solver, to enhance the efficiency and scalability of querying complex graph structures. 

- By translating graph queries into SAT problems, the project provides a robust framework for solving intricate graph-related challenges, demonstrating a significant advancement in database querying techniques and automated reasoning.

## Project Description
Graph databases are widely used to model and store complex relationships between data entities. However, querying such databases efficiently can be challenging. This project addresses this challenge by leveraging the z3 SAT solver to handle graph queries. By encoding graph queries as SAT problems, the z3 solver can determine the satisfiability of these queries and help in retrieving relevant information from the graph database.

## Features
- Integration with z3 SAT Solver: We used the z3 SAT solver to encode and solve graph queries.
- Graph Query Encoding: Transforming graph database queries into SAT problems that can be handled by z3.
- Efficient Query Resolution: Leveraging the z3 solver's capabilities to provide solutions to complex graph queries.

## Getting Started
### Prerequisites
- [Python](https://www.python.org/) (version 3.x)
- [z3-solver](https://pypi.org/project/z3-solver/) (Python bindings for the z3 SAT solver)

### Installation
1. Clone the repository:
```git
git clone https://sci-git.cs.rptu.de/m_elsayed24/automated-reasoning-ss2024-project.git
cd automated-reasoning-ss2024-project
```
2. Install required Python packages:
```python
pip install -r requirements.txt
```

### Documentation
For detailed documentation on how to prepare your graph data, encode queries, and interpret results, please refer to the [project documentation](https://github.com/Faris-Abuali/Querying-Graph-Database/blob/main/project.pdf).

### Group Members
- Mahmoud M. Hamido (Mtr. No. 428723)
- Faris H. Abu Ali (Mtr. No. 429085)

