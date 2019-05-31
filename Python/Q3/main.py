# a dictionary (keys are the first tuple and values are the second one)
A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), ('1', '2', '3', '4', '5')))
# a list containing 0, 1, ..., 9
A1 = range(10)
# a list containing common elements of A1 and A0's keys
A2 = [i for i in A1 if i in A0]
# a sorted list containing A0's values
A3 = sorted(A0[i] for i in A0)
# a list containing sublists in form of [i, i*i] and i is 0, 1, ..., 9
A4 = [[i, i*i] for i in A1]


def printContainer(container):
    if(type(container) is type(range(0))):
        [print(i, end=' ') for i in container]
    else:
        print(container)
    print('\n')


if __name__ == '__main__':
    [printContainer(container) for container in [A0, A1, A2, A3, A4]]
