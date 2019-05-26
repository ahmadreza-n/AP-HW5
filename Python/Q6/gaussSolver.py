import math


class CGaussSolver:
    def __init__(self, pf, a, b, n):
        self.pf = pf
        self.a = a
        self.b = b
        self.n = n

    def legendre(self, n, x):
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            return ((2.0 * n - 1) / n) * x * self.legendre(n - 1, x) - ((1.0 * n - 1) / n) * self.legendre(n - 2, x)

    def dLegendre(self, n, x):
        return (1.0 * n / (x * x - 1)) * ((x * self.legendre(n, x)) - self.legendre(n - 1, x))

    def legendreZeroes(self, n, i):
        xOld = math.cos(math.pi * (i - 1 / 4.0) / (n + 1 / 2.0))
        xNew = xOld + 1
        iteration = 1
        while (1 + math.fabs(xNew - xOld)) > 1.:
            if iteration != 1:
                xOld = xNew
            xNew = xOld - self.legendre(n, xOld) / self.dLegendre(n, xOld)
            iteration += 1
        return xNew

    def exec(self):
        integral = 0
        for i in range(self.n):
            integral += self.pf(self.legendreZeroes(self.n, i + 1)) * \
                self.weight(self.n, self.legendreZeroes(self.n, i + 1))
        self.result = ((self.b - self.a) / 2.0) * integral

    def getResult(self):
        return self.result

    def weight(self, n, x):
        return 2 / ((1 - math.pow(x, 2)) * math.pow(self.dLegendre(n, x), 2))


def func(x):
    return x*x


if __name__ == "__main__":
    obj = CGaussSolver(func, 0, 1, 2)
    obj.exec()
    print(obj.getResult())
