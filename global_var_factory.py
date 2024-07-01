from typing import Union
import z3

from mytypes import GlobalVarType

class GlobalVarFactory:
    @staticmethod
    def create_global_var(var_name: str, type: GlobalVarType) -> Union[z3.ArithRef, z3.SeqRef]:
        if type == "Real":
            return z3.Real(var_name)
        elif type == "String":
            return z3.String(var_name)
        else:
            raise ValueError("Unsupported attribute type")

