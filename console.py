from typing import Literal
from colorama import Fore, Style, Back

Variant = Literal["Fore", "Back"]

class Console:    
    @staticmethod
    def red(text: str, back: bool = False) -> str:
        variant = Back if back else Fore
        return f"{variant.RED}{text}{Style.RESET_ALL}"
    
    @staticmethod
    def green(text: str, back: bool = False) -> str:
        variant = Back if back else Fore
        return f"{variant.GREEN}{text}{Style.RESET_ALL}"
    
    @staticmethod
    def blue(text: str, back: bool = False) -> str:
        variant = Back if back else Fore
        return f"{variant.BLUE}{text}{Style.RESET_ALL}"
