with open('Day3/input.txt', 'r') as f: s_input = f.read()

sacks = [sack for sack in s_input.split('\n')]

sacks = [list(set(s[:int(len(s)/2)]).intersection(s[int(len(s)/2):]))[0] for s in sacks]

#Part 1
priority = sum([y - (96 if y >= 97 else 38) for y in [ord(x) for x in sacks]])
print(priority)

#Part 2
#print(sum([y - (96 if y >= 97 else 38) for y in [ord(x) for x in [list(set(x).intersection(y).intersection(z))[0] for x,y,z in [[s for s in s_input.split('\n')][x*3:x*3+3] for x in range(int(len([s for s in s_input.split('\n')])/3))]]]]))
sets = [s for s in s_input.split('\n')]
subsets = [sets[x*3:x*3+3] for x in range(int(len(sets)/3))]
badges = [list(set(x) & set(y) & set(z))[0] for x,y,z in subsets]
priority = sum([y - (96 if y >= 97 else 38) for y in [ord(x) for x in badges]])
print(priority)