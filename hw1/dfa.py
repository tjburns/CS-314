class dfa:

    current_state = None

    def __init__(self, states, symbols, transition_rules, start_state, final_states):
        self.states = states
        self.symbols = symbols
        self.transition_rules = transition_rules
        self.start_state = start_state
        self.final_states = final_states
        self.current_state = start_state
        return

    def transition_to_state(self, input_value):
        if (self.current_state, input_value) not in self.transition_rules.keys():
            self.current_state = None
            return
        self.current_state = self.transition_rules[(self.current_state, input_value)]
        return

    def in_final_state(self):
        return self.current_state in self.final_states

    def go_to_initial_state(self):
        self.current_state = self.start_state
        return

    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        for i in input_list:
            self.transition_to_state(i)
            continue
        return self.in_final_state()


"""
states = ['q0', 'q1', 'q2', 'q3']
symbols = ['a', 'b', 'c']
tr = dict()
tr[('q0', 'a')] = 'q1'
tr[('q1', 'b')] = 'q2'
tr[('q0', 'c')] = 'q2'
tr[('q1', 'a')] = 'q1'
tr[('q0', 'b')] = 'q3'
# {('q0', 'a'): 'q1', ('q1', 'b'): 'q2', ('q0', 'c'): 'q2', ('q1', 'a'): 'q1', ('q0', 'b'): 'q3'}
start = 'q0'
final = ['q2', 'q3']
"""

line = input().split()
states = []
for i in range(len(line)-1):
    states.append(line[i+1])
# print(states)

line = input().split()
symbols = []
for i in range(len(line) - 1):
    symbols.append(line[i + 1])
# print(symbols)

line = input().split()
# print(line)
tr = dict()
while line[0] != 'end_rules':
    if line[0] == 'begin_rules':
        line = input().split()
        continue
    # print(line)
    tr[(line[0], line[4])] = line[2]
    # print("value added to dictionary")

    line = input().split()
# print(tr)

line = input().split()
start = line[1]
# print(start)

final = []
line = input().split()
for i in range(len(line)-1):
    final.append(line[i+1])
# print(final)

testAutomaton = dfa(states, symbols, tr, start, final)

while(True):
    try:
        line = input()
    except EOFError:
        exit(0)
    if testAutomaton.run_with_input_list(line):
        print("accepted")
    else:
        print("rejected")