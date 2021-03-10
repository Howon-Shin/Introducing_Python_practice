# 7.1
year_lists = [1997 + year for year in range(6)]

print(year_lists)

# 7.2
print(year_lists[3])

# 7.3
print(year_lists[-1])

# 7.4 
things = ["mozzarella", "cinderella", "salmonella"]

# 7.5
print(things[1].capitalize())
print(things)

# 7.6
print(things[0].upper())
print(things)

# 7.7
del things[2]
print(things)

# 7.8
surprise = ["Groucho", "Chico", "Harpo"]

# 7.9
print(surprise[-1].lower()[::-1].capitalize())
print(surprise)

# 7.10
even = [num for num in range(10) if num%2 == 0]
print(even)

# 7.11
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done")
]
start2 = "Someone better"

for rhyme in rhymes:
    print(('! '.join(start1) + '! ' + rhyme[0] + '!').title())
    print(start2 + ' ' + rhyme[1] + '.')