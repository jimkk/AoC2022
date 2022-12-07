with open('Day7/input.txt', 'r') as fp: s_input = fp.read()

lines = s_input.split('\n')

class System:
    location = ['/']
    filetree = {}
    def up_dir(self):
        self.location = self.location[:-1]
    def down_dir(self, s):
        self.location.append(s)
    def root_dir(self):
        self.location = self.location[1:1]
    def get_location(self):
        return self.location
    def add_dir(self, s):
        loc = self.filetree
        for step in self.location:
            loc = loc[step]
        if s not in loc.keys():
            loc[s] = {}
    def add_file(self, s, size):
        loc = self.filetree
        for step in self.location:
            loc = loc[step]
        if s not in loc.keys(): 
            loc[s] = int(size)
    def get_filetree(self):
        return self.filetree

system = System()



for line in lines:
    if line.startswith('$ cd'):
        if line.endswith('..'):
            system.up_dir()
        elif line.endswith(' /'):
            system.root_dir()
        else:
            system.down_dir(line.split(' ')[2])
    elif line.startswith('$ ls'):
        continue
    elif line.startswith('dir'):
        system.add_dir(line.split(' ')[1])
    else:
        l = line.split(' ')
        system.add_file(l[1], l[0])

sizes = []
def get_file_size(filetree):
    size = 0
    for key in filetree.keys():
        if type(filetree[key]) is dict:
            size += get_file_size(filetree[key])
        else:
            size += filetree[key]
    sizes.append(size)
    return size

size = get_file_size(system.get_filetree())
print(sum([x for x in sizes if x <= 100000]))


required_deletion_amount = 30000000 - (70000000 - size)
print(min([x for x in sizes if x >= required_deletion_amount]))