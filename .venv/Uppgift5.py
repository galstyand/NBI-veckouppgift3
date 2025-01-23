import random

print("Välkommen till gissa-numret-spelet!")
print("Jag har valt ett hemligt tal mellan 1 och 100. Kan du gissa vad det är?")

secret = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Gissa ett tal: "))
    attempts += 1

    if guess < secret:
        print("För lågt! Försök igen.")
    elif guess > secret:
        print("För högt! Försök igen.")
    else:
        print("Grattis! Du gissade rätt på " + str(attempts) + " försök.")
        break

    if abs(guess - secret) < 5:
        print("Nu börjar det brännas!")