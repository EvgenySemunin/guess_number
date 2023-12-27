from random import randint
number = randint(1, 100)
print(number)
print('Guess number')
while True:
    guess = int(input('Введите число - 3'))
    if guess < number:
        print('Ваше число меньше того, что загадано.')
    elif guess > number:
        print('Ваше число больше того, что загадано. ')
    elif guess == number:
        break
print('Отличная интуиция! Вы угадали число :)')
