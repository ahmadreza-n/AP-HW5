import random
import math


# part 1
def isInCircle(x, y):  # returns true if (x, y) is in Circle
    return (x*x + y*y) < 0.25


# part 2
def calculatePi(totalPoints):  # calculates pi with given number of points
    inCirclePoints = 0
    for _ in range(totalPoints):
        randX = random.random() - 0.5
        randY = random.random() - 0.5
        inCirclePoints += int(isInCircle(randX, randY))

    return inCirclePoints*4/totalPoints


# part 3
def find(error):  # calculates pi and number of points needed
    calculatedPi = 0
    totalPoints = 0
    inCirclePoints = 0
    while math.fabs(math.pi - calculatedPi) > error:
        totalPoints += 1
        randX = random.random() - 0.5
        randY = random.random() - 0.5
        inCirclePoints += int(isInCircle(randX, randY))
        calculatedPi = inCirclePoints*4/totalPoints

    return [totalPoints, calculatedPi]


# part 4
if __name__ == '__main__':
    iterations = int(input('enter a number: '))
    totalPoints = 0
    pi = 0
    for _ in range(iterations):
        data = find(0.01)
        totalPoints += data[0] / iterations
        pi += data[1] / iterations

    print(f'average of total points needed is: {int(totalPoints)}')
    print(f'average of calculated pi is: {pi:.5f}')
