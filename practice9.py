# 9.1
def good():
    return ['Harry', 'Ron', 'Hermione']

print(good())

# 9.2
def get_odds(first = 0, last = 10, step = 1):
    num = first
    while num < last:
        if num%2 == 1:
            yield num
        
        num += step

i = 0
for odd in get_odds():
    i += 1
    if i == 3:
        print(odd)
        break

# 9.3
def test(func):
    def new_function(*args, **kwargs):
        print("start")
        func(*args, **kwargs)
        print("end")
    return new_function

@test
def add(a, b):
    print(a + b)

add(2, 42)

# 9.4
class OopsException(Exception):
    pass

try:
    raise OopsException("Caught an oops")
except OopsException as exc:
    print(exc)
