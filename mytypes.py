from typing import TypeAlias, Literal
import z3

Node: TypeAlias = str

GlobalVarType = Literal["Real", "String"]

Z3VarType = z3.ArithRef | z3.SeqRef 
