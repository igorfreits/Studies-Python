# Write your code below this row 👇

for i in range(0, 101):
    if i % 3 == 0:
        print(f'{i} - Fizz')
    elif i % 5 == 0:
        print(f'{i} - Buzz')
    elif i % 3 == 0 and i % 5 == 0:
        print(f'{i} - FizzBuzz')
    else:
        print(i)
