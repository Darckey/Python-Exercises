import random
x = 0
throw_counts = 0

while x != 1:
    x = random.randint(1, 6)
    print(x)
    throw_counts += 1
else:
    print(f'You got number 1 after {throw_counts} tries.')
"""
i = 0

while i < 10:
    print(random.randint(1, 6))
    i += 1
else:
    print("end")

    """