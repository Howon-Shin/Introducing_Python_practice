# 4.1
secret = 4
guess = 8

if guess < secret:
    print("too low")
elif guess == secret:
    print("just right")
else:
    print("too high")

# 4.2
small = True
green = False

if small and green:
    print("pea")
elif small and not green:
    print("cherry")
elif not small and green:
    print("watermelon")
elif not small and not green:
    print("pumpkin")