# factorial of a number: 
# 5! factorial is 120: 
# 5 * 4 * 3 * 2 * 1 

# A recursive function calls itself with modified data 

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(f'5!={factorial(5):,}, 3!={factorial(3):,}, 11!={factorial(11)}')


# fibonacci numbers:
# 1, 1, 2, 3, 5, 8, 13, 21, ....

def fibonacci(limit):
    nums = []

    current = 0
    next_num = 1

    while current < limit:
        current, next_num = next_num, next_num + current
        nums.append(current)

    return nums 


print('with list')
for n in fibonacci(100):
    print(f'{n}', end=', ')

print()
print()

def fibonacci_co():
    current = 0
    next_num = 1

    # while current < limit:
    while True:
        current, next_num = next_num, next_num + current
        yield current

print('with yield')
for n in fibonacci_co():
    if n > 1000:
        break
    
    print(f'{n}', end=', ')
