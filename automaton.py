from typing import Optional

class Automaton:
    def __init__(self):
        self.initial_state: Optional[int] = None
        self.transitions: list[AutomatonTransition] = []
        self.final_states: set[int] = set()

    def __str__(self):
        transitions_str = "\n".join(str(transition) for transition in self.transitions)
        return f"Initial State: {self.initial_state}, Transitions:\n{transitions_str}, Final States: {self.final_states}"

class AutomatonTransition:
    def __init__(self, from_state: int, to_state: int, formula: str):
        self.from_state = from_state
        self.to_state = to_state
        self.formula = formula

    def __str__(self):
        return f"From: {self.from_state}, To: {self.to_state}, Formula: {self.formula}"
