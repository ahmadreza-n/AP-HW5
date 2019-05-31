import gaussSolver as gs
import math
from time import time as epochTime
import sys
import subprocess
import matplotlib.pyplot as plt


def func(x):
    x = 0.5*x + 0.5
    return math.pow(x, 3) * math.cos(math.pow(x, 2)) / (x + 1)


n = int(sys.argv[1])

# part 1
print("############# first part #############")
start = epochTime()
aSolver = gs.CGaussSolver(func, 0, 1, n)
aSolver.exec()
print(f"Result of Python code (n = {n}) : {aSolver.getResult():.20f}")
print(f"took {(epochTime() - start) * 1000:.4f} ms\n")

start = epochTime()
subprocess.call(['./main', f'{n}'])
print(f"took {(epochTime() - start) * 1000:.4f} ms\n")

# part 2
print("############# second part #############")
pythonTime = []
cTime = []
inputList = range(1, n + 1)
for i in inputList:
    start = epochTime()
    aSolver = gs.CGaussSolver(func, 0, 1, i)
    aSolver.exec()
    pythonTime.append((epochTime() - start) * 1000)
    print(f"\nResult of Python code (n = {i}) : {aSolver.getResult():.20f}")
    start = epochTime()
    subprocess.call(['./main', f'{i}'])
    cTime.append((epochTime() - start) * 1000)


print("\n\nDegree \t Python \t C++")
for i in inputList:
    print(f"{i} \t {pythonTime[i - 1]:.5f}ms \t {cTime[i - 1]:.5f}ms")

f = plt.figure()
plt.plot(inputList, pythonTime, label="Python")
plt.plot(inputList, cTime, label="C++")
plt.xlabel('Degree')
plt.ylabel('Time in ms')
plt.legend()
plt.show()
f.savefig("result.pdf")
