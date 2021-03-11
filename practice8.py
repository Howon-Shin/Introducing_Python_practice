# 8.1
e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}

# 8.2
print(e2f['walrus'])

# 8.3
f2e = dict(item[::-1] for item in e2f.items())
print(f2e)

# 8.4
print(dict(item[::-1] for item in e2f.items())['chien'])

# 8.5
print(e2f.keys())

# 8.6
life = {'animal': {'cats': 'Henri', 'octopi': 'Grumpy', 'emus': 'Lucy'},\
     'plants': {}, 'other': {}}

# 8.7
print(life.keys())

# 8.8
print(life['animal'].keys())

# 8.9
print(life['animal']['cats'])

# 8.10
squares = {num: num**2 for num in range(10)}
print(squares)

# 8.11
odd = {num for num in range(10) if num%2 == 1}
print(odd)

# 8.12
iter = (thing for thing in (list('Got') + list(range(10))))

for i in iter:
    print(i)

# 8.13
print(dict(zip(('optimist', 'pessimist', 'troll'), ('The glass is half full',\
     'The glass is half empty', 'How did you get a glass?'))))

# 8.14
print(dict(zip(['Creature of Habit', 'Crewel Fate'], ['A nun turns into a mon ster',\
     'A haunted yarn shop'])))