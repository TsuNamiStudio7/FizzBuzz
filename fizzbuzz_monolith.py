import logging
from typing import Callable, Dict, List

# --- Global Registry for Rules ---
RULES: Dict[str, Callable[[int], str]] = {}

def fizzbuzz_rule(name: str):
    """Decorator to register a new FizzBuzz rule."""
    def decorator(func: Callable[[int], str]):
        RULES[name] = func
        return func
    return decorator

# --- Define Rules (Plugin-like but inline) ---

@fizzbuzz_rule("Fizz")
def fizz(n: int) -> str:
    return "Fizz" if n % 3 == 0 else ""

@fizzbuzz_rule("Buzz")
def buzz(n: int) -> str:
    return "Buzz" if n % 5 == 0 else ""

@fizzbuzz_rule("Bazz")
def bazz(n: int) -> str:
    return "Bazz" if n % 7 == 0 else ""

@fizzbuzz_rule("DoubleEleven")
def double_eleven(n: int) -> str:
    return "DoubleEleven" if n % 11 == 0 and n % 2 == 0 else ""

@fizzbuzz_rule("Prime")
def prime(n: int) -> str:
    if n < 2: return ""
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return ""
    return "Prime"

# --- FizzBuzz Engine ---

class FizzBuzzEngine:
    def __init__(self, active_rules: List[str]):
        self.active_rules = active_rules
        self.logger = logging.getLogger("FizzBuzzEngine")
        self.logger.setLevel(logging.INFO)

    def evaluate(self, number: int) -> str:
        result = ''.join(RULES[name](number) for name in self.active_rules if name in RULES)
        self.logger.debug(f"{number}: {result or str(number)}")
        return result or str(number)

    def run(self, start: int, end: int) -> None:
        for number in range(start, end + 1):
            print(f"{number}: {self.evaluate(number)}")

# --- Main Program Config ---

if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING)

    # You can add or remove rule names here freely
    CONFIG = {
        "enabled_rules": ["Fizz", "Buzz", "Bazz", "DoubleEleven", "Prime"]
    }

    engine = FizzBuzzEngine(CONFIG["enabled_rules"])
    engine.run(1, 100)
