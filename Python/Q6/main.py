import gaussSolver as gs
import math
from time import time as epochTime

def func(x):
    return math.pow(x, 3) * math.cos(math.pow(x, 2)) / (x + 1)

start = epochTime()

obj = gs.CGaussSolver(func, 0, 1, 20)
obj.exec()
print(f"result: {obj.getResult():.6}",)

print(f"took {(epochTime() - start):.7} ms")


