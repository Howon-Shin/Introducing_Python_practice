# 6.1
for num in [3, 2, 1, 0]:
    print(num)

# 6.2
guess_me = 7
number = 1
while number <= guess_me:
    if number == guess_me:
        print('found it!')
        break
    
    print("too low")

    number += 1
else:
    print('oops')

# 6.3
guess_me = 5
for number in range(10):
    if number == guess_me:
        print('found it!')
        break
    
    print("too low")
else:
    print('oops')