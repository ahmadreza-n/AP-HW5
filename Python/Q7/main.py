import sys

[print(item, end=' ') for item in sorted(set([int(sys.argv[i]) for i in range(1, len(sys.argv)) if int(sys.argv[i]) % 6 == 0 and i % 6 == 0]))]
