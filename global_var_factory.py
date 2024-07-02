from typing import Union
import z3

from mytypes import GlobalVarType, Z3VarType

class GlobalVarFactory:
    @staticmethod
    def create_global_var(var_name: str, type: GlobalVarType) -> Z3VarType:
        if type == "Real":
            return z3.Real(var_name) # type: ignore
        elif type == "String":
            return z3.String(var_name) # type: ignore
        else:
            raise ValueError("Unsupported attribute type")

