# 14.1
import os

print(os.listdir('.'))

# 14.2
print(os.listdir('..'))

# 14.3
test1 = 'This is a test of the emergency text system'

fout = open('test.txt', 'wt')
print(test1, file= fout)

fout.close()

# 14.4
fin = open('test.txt', 'rt')

test2 = fin.read()

fin.close()

print(test2)