from typing import List, Callable, Protocol
import logging

# -- Protocols (Interfaces) for extensibility --

class Rule(Protocol):
    def applies(self, number: int) -> bool: ...
    def output(self) -> str: ...

class OutputHandler(Protocol):
    def handle(self, number: int, result: str) -> None: ...

# -- Core Implementation --

class DivisibleRule:
    def __init__(self, divisor: int, word: str):
        self.divisor = divisor
        self.word = word

    def applies(self, number: int) -> bool:
        return number % self.divisor == 0

    def output(self) -> str:
        return self.word

class LambdaRule:
    def __init__(self, condition: Callable[[int], bool], word: str):
        self.condition = condition
        self.word = word

    def applies(self, number: int) -> bool:
        return self.condition(number)

    def output(self) -> str:
        return self.word

class ConsoleOutputHandler:
    def handle(self, number: int, result: str) -> None:
        print(f"{number}: {result}")

class FizzBuzzEngine:
    def __init__(self, rules: List[Rule], handler: OutputHandler = ConsoleOutputHandler()):
        self.rules = rules
        self.handler = handler
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    def evaluate(self, number: int) -> str:
        result = ''.join(rule.output() for rule in self.rules if rule.applies(number))
        return result or str(number)

    def run(self, start: int, end: int) -> None:
        for number in range(start, end + 1):
            result = self.evaluate(number)
            self.logger.debug(f"Evaluating {number}: {result}")
            self.handler.handle(number, result)

# -- Sample usage --

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    rules = [
        DivisibleRule(3, "Fizz"),
        DivisibleRule(5, "Buzz"),
        DivisibleRule(7, "Bazz"),
        LambdaRule(lambda x: x % 11 == 0 and x % 2 == 0, "DoubleEleven")
    ]

    engine = FizzBuzzEngine(rules)
    engine.run(1, 150)
