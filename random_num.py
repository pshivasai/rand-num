import random

answer = random.randint(1,5)

while True:
    try:
        guess = int(input("Guess the number between 1 to 10 : "))
        if 0 < guess and guess < 11:
            if guess == answer:
                print("you are great!!!")
                break
            if guess != answer:
                print('try again')
        else:
            print('hey!! enter only numbers between 1 to 10.')
            continue
    except ValueError:
        print('enter a number')