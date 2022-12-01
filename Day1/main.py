with open('Day1/input.txt', 'r', encoding='utf-8') as f: s_input = f.read()

elf_calories = [sum(x) for x in [[int(x) for x in elf.split('\n')] for elf in s_input.split('\n\n')]]

#Part1
print(max(elf_calories))

#Part2
print(sum(sorted(elf_calories, reverse=True)[:3]))
