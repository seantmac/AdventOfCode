import re
from collections import namedtuple, defaultdict
from textwrap import dedent

Action = namedtuple('Action', ['write', 'move', 'state'])

def parse_input(text):
    init_state = re.search('Begin in state (.)\.', text).group(1)
    steps = int(re.search('after (\d+) steps', text).group(1))
    # Pretend that re is sscanf
    rule_matches = re.finditer(dedent("""\
In state (.):
  If the current value is 0:
    - Write the value (.)\.
    - Move one slot to the (\w+)\.
    - Continue with state (.)\.
  If the current value is 1:
    - Write the value (.)\.
    - Move one slot to the (\w+)\.
    - Continue with state (.)\."""), text)
    rules = {}
    dirs = {'right': 1, 'left': -1}
    for rule in rule_matches:
        rules[rule[1]] = (Action(int(rule[2]), dirs[rule[3]], rule[4]),
                          Action(int(rule[5]), dirs[rule[6]], rule[7]))
    return init_state, steps, rules

def run(blueprint):
    state, steps, rules = parse_input(blueprint)
    tape = defaultdict(int)
    cursor = 0
    for _ in range(steps):
        action = rules[state][tape[cursor]]
        tape[cursor] = action.write
        cursor += action.move
        state = action.state
    return len({k for k, v in tape.items() if v == 1})

if __name__ == '__main__':
    with open('25.TXT') as f:
        input_ = f.read()
    print(run(input_))


#4225