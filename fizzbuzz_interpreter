import re
from typing import Callable, List, Dict

# Define operations the DSL understands
OPERATIONS: Dict[str, Callable[[int], str]] = {
    "if_divisible": lambda n, arg: arg["text"] if n % arg["mod"] == 0 else "",
    "if_endswith":  lambda n, arg: arg["text"] if str(n).endswith(arg["digit"]) else "",
    "else_number":  lambda n, arg: str(n) if not arg["accum"] else "",
}

# Mini DSL parser: converts text lines into rule functions
def parse_dsl(lines: List[str]) -> List[Callable[[int], str]]:
    rules = []
    for line in lines:
        if line.startswith("#") or not line.strip():
            continue
        tokens = re.split(r'\s+', line.strip())
        op = tokens[0]
        if op == "if_divisible":
            mod = int(tokens[1])
            text = tokens[2]
            rules.append(lambda n, m=mod, t=text: OPERATIONS[op](n, {"mod": m, "text": t}))
        elif op == "if_endswith":
            digit = tokens[1]
            text = tokens[2]
            rules.append(lambda n, d=digit, t=text: OPERATIONS[op](n, {"digit": d, "text": t}))
        elif op == "else_number":
            rules.append(lambda n: OPERATIONS[op](n, {"accum": apply_all_rules(n, rules[:-1])}))
    return rules

# Apply all rules in order and accumulate result
def apply_all_rules(n: int, rules: List[Callable[[int], str]]) -> str:
    accum = ""
    for rule in rules:
        result = rule(n)
        accum += result
    return accum or str(n)

# Main run logic
def run_fizzbuzz_dsl(start: int, end: int, dsl_code: str):
    lines = dsl_code.strip().split("\n")
    rules = parse_dsl(lines)
    for i in range(start, end + 1):
        print(apply_all_rules(i, rules))

# Sample DSL config
DSL_PROGRAM = """
# FizzBuzz DSL Sample
if_divisible 3 Fizz
if_divisible 5 Buzz
if_endswith 7 Lucky
else_number
"""

if __name__ == "__main__":
    run_fizzbuzz_dsl(1, 50, DSL_PROGRAM)
