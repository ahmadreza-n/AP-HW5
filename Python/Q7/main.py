import sys

l = []
[l.append(int(sys.argv[i])) for i in range(1, len(sys.argv)) if int(sys.argv[i]) % 6 == 0 and (i) % 6 == 0 and int(sys.argv[i]) not in l]
l.sort()
print(l)