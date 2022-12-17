from functools import reduce
import operator
with open('Day8/input.txt') as f: s_input = f.read()

rows = s_input.split('\n')

tall_trees = (2 * len(rows[0])) + (2 * (len(rows)-2))

for i in range(1, len(rows)-1):
    for j in range(1, len(rows[0])-1):
        column = [x[j] for x in rows]
        if max(rows[i][0:j]) < rows[i][j]:
            tall_trees += 1
        elif max(rows[i][j+1:]) < rows[i][j]:
            tall_trees += 1
        elif max(column[:i]) < rows[i][j]:
            tall_trees += 1
        elif max(column[i+1:]) < rows[i][j]:
            tall_trees += 1

# Part 1
print(tall_trees)

highest_score = 0
for i, row in enumerate(rows):
    for j in range(len(rows[0])):
        visible_trees = [0 for _ in range(4)]
        column = [x[j] for x in rows]
        # left
        for k in range(j-1,-1, -1):
            visible_trees[0] += 1
            if row[k] >= row[j]:
                break
        # right
        for k in range(j+1, len(row)):
            visible_trees[1] += 1
            if row[k] >= row[j]:
                break
        # up
        for k in range(i-1, -1, -1):
            visible_trees[2] += 1
            if column[k] >= column[i]:
                break
        # down
        for k in range(i+1, len(column)):
            visible_trees[3] += 1
            if column[k] >= column[i]:
                break
        score = reduce(operator.mul, visible_trees)
        if score > highest_score: 
            highest_score = score
print(highest_score)
