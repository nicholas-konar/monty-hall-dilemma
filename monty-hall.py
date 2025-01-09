import random

# number of game simulations to run
k = 1000

# whether the contestant should change their guess or not
changeGuess = True


def rand(): return random.randint(0, 2)


# random but not equal to x
def randx(x):
    y = rand()
    return y if x != y else randx(x)


# 3 doors, one of which contains the car.
def createDoors():
    doors = [False] * 3
    doors[rand()] = True
    return doors


def simulateGame(changeGuess):
    # randomly generate the doors and make a guess
    doors = createDoors()
    guess1 = rand()

    # never reveal the car or guess1
    n = randx(guess1)
    reveal = n if not doors[n] else 3 - n - guess1

    # guess2 can only be the last remaining door
    guess2 = 3 - reveal - guess1
    return doors[guess2] if changeGuess else doors[guess1]


results = [simulateGame(changeGuess) for i in range(k)]

print(f'won {sum(results)} out of {len(results)}')
