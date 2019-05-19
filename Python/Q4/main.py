import random
import math

# part 1


def isInCircle(x, y):
    return (x*x + y*y) < 1

# part 3


def find(error):
    calculatedPi = 0
    totalPoints = 0
    inCirclePoints = 0
    while math.fabs(math.pi - calculatedPi) > error:
        totalPoints += 1
        randX = (random.random() * 2) - 1
        randY = (random.random() * 2) - 1
        inCirclePoints += int(isInCircle(randX, randY))
        calculatedPi = inCirclePoints*4/totalPoints
    return [totalPoints, calculatedPi]

# part 2
def calculatePi(totalPoints):
    inCirclePoints = 0
    for _ in range(totalPoints):
        randX = (random.random() * 2) - 1
        randY = (random.random() * 2) - 1
        inCirclePoints += int(isInCircle(randX, randY))

    return inCirclePoints*4/totalPoints

# part 4
iterations = int(input('enter a number: '))
totalPoints = 0
pi = 0
for _ in range(iterations):
    data = find(0.01)
    totalPoints += data[0] / iterations
    pi += data[1] / iterations
print('average of total points neede is:', int(totalPoints))
print(f'average of calculated pi is: {pi:.5f}')
