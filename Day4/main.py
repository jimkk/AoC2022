with open('Day4/input.txt', 'r') as fp: s_input = fp.read()
def expand(x):
    parts = x.split('-')
    return [*range(int(parts[0]), int(parts[1])+1)]
pairs = [[expand(y), expand(z)] for y,z in [x.split(',') for x in s_input.split('\n')]]
pair_intersections = [len(set(p[0]) & set(p[1])) for p in pairs]
# Part 1
full_intersection = [1 if (len(pairs[i][0]) == pair_intersections[i] or len(pairs[i][1]) == pair_intersections[i] ) else 0 for i in range(len(pairs))]
print(sum(full_intersection))
# Part 2
partial_intersection = [1 for p in pair_intersections if p > 0]
print(sum(partial_intersection))