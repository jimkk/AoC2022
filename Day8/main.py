with open('input.txt') as f: s_input = f.read()

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
print(tall_trees)
