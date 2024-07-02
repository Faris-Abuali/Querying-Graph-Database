import json
from automaton import Automaton, AutomatonTransition
from global_var_factory import GlobalVarFactory
from graph import Graph, NodeAttributes
from mytypes import Z3VarType

class JSONParser:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.graph_db = Graph()
        self.attributes = NodeAttributes()
        self.automaton = Automaton()
        self.attribute_map: dict[str, tuple] = {}
        self.global_vars: dict[str, Z3VarType] = {}

    def parse(self) -> tuple[Graph, NodeAttributes, Automaton, dict[str, Z3VarType]]:
        with open(self.file_path, "r") as file:
            json_data = json.load(file)

        self._parse_graph_db(json_data["Graph Database"]["Edges"])
        self._parse_attributes(json_data["Attributes"])
        self._parse_automaton(json_data["Automaton"])
        self._parse_global_vars(json_data["Global Variables"])

        return self.graph_db, self.attributes, self.automaton, self.global_vars

    def _parse_graph_db(self, edges: list[str]):
        for edge in edges:
            from_node, to_node = map(int, edge.split(" -> "))
            self.graph_db.add_edge(from_node, to_node)

    def _parse_attributes(self, attributes: dict):
        for vertex, attr in attributes.items():
            for attr_name, attr_value in attr.items():
                self.attributes.add_variable(attr_name, attr_value)

        for vertex, attr in attributes.items():
            attr_tuple = tuple(attr.values())
            self.attribute_map[vertex] = attr_tuple
        self.attributes.attribute_map = self.attribute_map

    def _parse_automaton(self, automaton_data: dict):
        self.automaton.initial_state = automaton_data["Initial State"]
        self.automaton.final_states = set(automaton_data["Final States"])
        self.automaton.transitions = [
            AutomatonTransition(t["from"], t["to"], t["formula"])
            for t in automaton_data["Transitions"]
        ]

    def _parse_global_vars(self, global_vars: dict):
        for name, type in global_vars.items():
            self.global_vars[name] = GlobalVarFactory.create_global_var(name, type)
