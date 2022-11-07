import random
import getpass
import modul1

# getpass.getuser() = jelenlegi fióknév

modul1.greeting(getpass.getuser())
number = random.randint(1, 9)
chances = 0
guess = 0

while True:
    while True:
        try:
            guess = int(input())
        except ValueError:
            print("Nem ertelmetheto szam")
            continue
        else:
            break

    if guess == number:
        print(
            f'GRATULALOK ELTALALTAD A SZAMOT \
            {chances} PROBABOL SIKERULT ELTALALNOD A SZAMOT ({number})')
        break
    elif guess < number:
        print("A szam nagyobb mint ", guess)
    else:
        print("A szam kissebb mint ", guess)
    chances += 1


class Rating:
    def __init__(self, num, text):
        self.num = num
        self.text = text


print('kérlek értékeld a programot:')
while True:
    try:
        print('Ertekeles[1-5]: ')
        rateN = int(input())
        if rateN > 5 or rateN < 1:
            continue
    except ValueError:
        print("Nem ertelmetheto szam")
        continue
    else:
        break

while True:
    try:
        print('Megjegyzés: ')
        rateT = input()

    except ValueError:
        print("Nem ertelmetheto karakter")
        continue
    else:
        break

print('Megjegyzés')
try:
    p1 = Rating(rateN, rateT)
except ValueError:

    print('something vent wrong')

else:
    if p1.num == 5:
        modul1.textArt()
    print('\n////////////////////////\n|')
    modul1.rating(p1.num, p1.text)
    print('|\n|///////////////////////\n')

