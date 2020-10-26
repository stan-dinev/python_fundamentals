a = []

class Name:
    def __init__(self,name, games):
        self.name = name
        self.games = games


name1 = None

while True:
    command = input()
    if command == 'report':
        break
    string = command.split(' -> ')
    string1 = list(map(int, string[1].split(',')))
    name1 = Name(string[0], string1)
    a.append(name1)

while True:
    c = input()
    if c == 'end':
        break
    if c == 'score descending':
        d = sorted(a, key=lambda x: (-sum(x.games), x.name))
        for y in d:
            print(f'{y.name}: {sum(y.games)}')
    if c == 'score ascending':
        d = sorted(a, key=lambda x: (sum(x.games), x.name))
        for y in d:
            print(f'{y.name}: {sum(y.games)}')
    if c == 'numberOfGames descending':
        d = sorted(a, key=lambda x: (-len(x.games), x.name))
        for y in d:
            print(f'{y.name}: {len(y.games)}')
    if c == 'numberOfGames ascending':
        d = sorted(a, key=lambda x: (len(x.games), x.name))
        for y in d:
            print(f'{y.name}: {len(y.games)}')












