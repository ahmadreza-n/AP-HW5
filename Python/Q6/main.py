import gaussSolver as gs
import math
from time import time as epochTime
import sys
import subprocess
import matplotlib.pyplot as plt

def func(x):
    return math.pow(x, 3) * math.cos(math.pow(x, 2)) / (x + 1)

n = int(sys.argv[1])

print(f"python version with n = {n}")
start = epochTime()
obj = gs.CGaussSolver(func, 0, 1, n)
obj.exec()
# print(f"result: {obj.getResult():.6}",)
print(f"took {(epochTime() - start) * 1000:.7} ms")

print(f"c++ version with n = {n}")
start = epochTime()
subprocess.call(['./main', f'{n}'])
print(f"took {(epochTime() - start) * 1000:.7} ms")

pythonTime = []
cTime = []
print("########## last part ##########")
print("degree \t python \t c++")
inputList = range(20)
for i in inputList:
    start = epochTime()
    obj = gs.CGaussSolver(func, 0, 1, i)
    obj.exec()
    elapsedPython = (epochTime() - start) * 1000
    pythonTime.append(elapsedPython)

    start = epochTime()
    subprocess.call(['./main', f'{i}'])
    elapsedC = (epochTime() - start) * 1000
    cTime.append(elapsedC)
    
    print(f"{i} \t {elapsedPython:.5}ms \t {elapsedC:.3}ms")

f = plt.figure()
plt.plot(inputList, pythonTime, label = "python") 
plt.plot(inputList, cTime, label = "c++") 
plt.xlabel('degree') 
plt.ylabel('time in ms') 
plt.legend() 
plt.show()
f.savefig("result.pdf")