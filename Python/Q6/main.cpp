#include "gaussSolver.h"
#include <iostream>
#include <math.h>
#include <chrono>

long double func(long const double &x)
{
    return (pow(x, 3) / (x + 1)) * cos(pow(x, 2));
}

int main()
{
    long double (*pf)(const long double &);
    pf = &func;
    auto start{std::chrono::high_resolution_clock::now()};
    CGaussSolver obj(pf, 0, 1, 20);
    obj.exec();
    std::cout << "result: " << obj.getResult() << std::endl;
    auto end{std::chrono::high_resolution_clock::now()};
    std::cout << "took: " << std::chrono::duration_cast<std::chrono::duration<double>>(end - start).count() << "ms" << std::endl;
    return 0;
}
