import copy

with open('Day5/input.txt', 'r') as fp: s_input = fp.read()

inputs = s_input.split('\n\n')

initial_stacks = inputs[0].split('\n')[:-1]
instructions = inputs[1].split('\n')
instructions = [list(map(int, [x[1],x[3],x[5]])) for x in [y.split(' ') for y in instructions]]

stack_rows = []
for r in initial_stacks:
    i = 0
    row = []
    while i < len(r):
        row.append(r[i:i+3].strip('[] '))
        i = i + 4
    stack_rows.append(row)

stacks = [[] for i in range(len(stack_rows[0]))]
for row in stack_rows:
    for i, v in enumerate(row):
        if row[i] != '':
            stacks[i].insert(0, v)


def execute_instructions(s, instructions, is9000 = True):
    for instruction in instructions:
        amount = instruction[0]
        from_stack = instruction[1] - 1
        to_stack = instruction[2] - 1
        crates_to_move = s[from_stack][-amount:]
        if is9000: crates_to_move.reverse()
        s[to_stack] = s[to_stack] + crates_to_move
        del s[from_stack][-amount:]
    return s

# Part 1
stacks_p1 = copy.deepcopy(stacks)
execute_instructions(stacks_p1, instructions)
top_of_stack = ''
for stack in stacks_p1:
    top_of_stack += stack[-1]
print(top_of_stack)

# Part 2
stacks_p2 = copy.deepcopy(stacks)
execute_instructions(stacks_p2, instructions, is9000=False)
top_of_stack = ''
for stack in stacks_p2:
    top_of_stack += stack[-1]
print(top_of_stack)