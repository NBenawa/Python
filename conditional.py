from datetime import datetime

# FIZZBUZZ Problem
for n in range(1, 101):
    # if n % 15 == 0:
    #     print('FizzBuzz')
    # elif n % 3 == 0:
    #     print('Fizz')
    # elif n % 5 == 0:
    #     print('Buzz')
    # else:
    #     print(n)
    print('FizzBuzz' if n % 15 == 0 else 'Fizz' if n % 3 == 0 else 'Buzz' if n % 5 ==0 else n)


# WaitUntil Problem
wait_until = datetime.now().second + 5

while datetime.now().second != wait_until:
    pass
print(f'We are at {wait_until} seconds!')