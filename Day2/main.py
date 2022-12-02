with open('Day2/input.txt', 'r') as fp: s_input = fp.read()


rounds = [z.split(' ') for z in s_input.split('\n')]

rounds_nums = [(ord(z[0]) - ord('A'), ord(z[1]) - ord('X')) for z in rounds]


#Part 1
points = 0
for r in rounds_nums:
    result = (r[0] - r[1]) % 3
    match result:
        case 0:
            points = points + r[1] + 3
        case 1:
            points = points + r[1]
        case 2:
            points = points + r[1] + 6
    points = points + 1

print(points)


#Part 2
points = 0
for r in rounds_nums:
    match r[1]:
        case 0:
            points = points + ((r[0] - 1) % 3)
        case 1:
            points = points + r[0] + 3
        case 2:
            points = points + ((r[0] + 1) % 3) + 6
    points = points + 1

print(points)
