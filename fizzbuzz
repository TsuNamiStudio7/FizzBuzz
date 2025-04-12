from typing import List, Callable

class Rule:
    def __init__(self, condition: Callable[[int], bool], output: str):
        self.condition = condition
        self.output = output

    def applies_to(self, number: int) -> bool:
        return self.condition(number)

    def get_output(self) -> str:
        return self.output

class FizzBuzzEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules

    def evaluate(self, number: int) -> str:
        result = ''.join(rule.get_output() for rule in self.rules if rule.applies_to(number))
        return result or str(number)

    def run(self, start: int = 1, end: int = 100) -> List[str]:
        return [self.evaluate(i) for i in range(start, end + 1)]

# Define reusable rule generators
def divisible_by(n: int) -> Callable[[int], bool]:
    return lambda x: x % n == 0

# Instantiate rules
rules = [
    Rule(divisible_by(3), "Fizz"),
    Rule(divisible_by(5), "Buzz"),
    Rule(divisible_by(7), "Bazz"),
    Rule(lambda x: x % 11 == 0, "Eleven!")  # Custom lambda condition
]

# Run the engine
engine = FizzBuzzEngine(rules)
result = engine.run(1, 150)

# Output
for line in result:
    print(line)
