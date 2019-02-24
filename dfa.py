
print("run starts")
line = input().split()
states = []
for i in range(len(line)-1):
    print(line[i+1])
    states.append(line[i+1])
print(states)

line = input().split()
symbols = []
for i in range(len(line) - 1):
    symbols.append(line[i + 1])

print("dfa initialized. enters loop")
dfa = {}
for i in states:
    dfa[states[i]] = {}

line = input().split()
while line[0] != 'end_rules':
    if line[0] == 'begin_rules':
        continue

    dfa[line[0]] = {line[4], line[2]}

    line = input().split()

    print("loop")

print("exits loop")
print(dfa)

start = []
line = input().split()
for i in range(len(line)-1):
    start.append(line[i+1])

final = []
line = input().split()
for i in range(len(line)-1):
    final.append(line[i+1])

# check for end of file
# do tests



"""
dfa =  {0:{'a':1, 'b':3, 'c':2},
        1:{'a':1, 'b':2},
        2:{},
        3:{}}
"""