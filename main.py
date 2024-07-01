#!/bin/env python3

import z3
from typing import Literal, Optional, TypeAlias, Union
from console import Console
from data_utils import DataUtils
from json_parser import JSONParser

if __name__ == "__main__":
    solver = z3.Solver()
    file_path = "example1.json"  # Path to your JSON file

    json_parser = JSONParser(file_path)

    # Parse JSON file
    parsed_graph, parsed_attributes, parsed_automaton, global_vars = json_parser.parse()

    # Example usage to access the parsed data
    print(Console.blue("Graph Database: "), parsed_graph)
    print(Console.blue("Automaton: "), parsed_automaton)
    print(Console.blue("\nAttributes:  "), parsed_attributes)
    print(Console.blue("Alphabet: "), parsed_attributes.alphabet)
    print(Console.blue("Formula: "), parsed_automaton.transitions[0].formula)
    print(Console.blue("Global Vars: "), global_vars)

    all_variables = DataUtils.merge_dicts(parsed_attributes.alphabet, global_vars)
    print(Console.blue("All Vars: "), all_variables)
    
    # Parse smt2 string with declared vars; returns vector of assertions, in our case always 1
    test0 = z3.parse_smt2_string(
        parsed_automaton.transitions[0].formula, decls=all_variables
    )[0]
    print("\ntest0: ", Console.green(test0))
    solver.add(test0) # Assert constraints into the solver.
    solver.check() # Check model
    print(Console.green("model 1:", back=True), solver.model())
    
    
    test1 = z3.parse_smt2_string(
        parsed_automaton.transitions[1].formula, decls=all_variables
    )[0]
    print("\ntest1:", Console.green(test1))
    solver.add(test1) # Assert constraints into the solver.
    solver.check() # Check model
    print(Console.green("model 2:", back=True), solver.model())


    # Replace age by value 2
    test4 = parsed_attributes.alphabet["age"]
    test5 = global_vars["p1"]
    # test0[0] is the first assert in the z3 ast vector
    expr2 = z3.substitute(test0, (test4, z3.RealVal(2.0))) # substitute(formula, *(from, to))
    print("\nSubstitute age by 2: ", expr2)

    # print(expr2)
    # solver.add(expr2) # Assert constraints into the solver.
    # is_sat = solver.check() # Check model
    # print(is_sat)
