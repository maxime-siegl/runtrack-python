number = 1

while number <= 100:
    reste1 = number % 3
    reste2 = number % 5
    if reste1 == 0 and reste2 == 0:
        print('FizzBuzz')
    elif reste1 == 0:
        print('Fizz')
    elif reste2 == 0:
        print('Buzz')
    elif reste1 != 0 and reste2 != 0:
        print(number)

    number += 1