import re

with open('Day6/input.txt', 'r') as fp: s_input = fp.read()

# Part 1
for i in range(0, len(s_input)-4):
    if not re.match(r'^.*(.).*\1.*$', s_input[i:i+4]):
        print(i+4)
        break

# Part 2
for i in range(0, len(s_input)-14):
    if not re.match(r'^.*(.).*\1.*$', s_input[i:i+14]):
        print(i+14)
        break
