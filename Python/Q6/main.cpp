#include "gaussSolver.h"
#include <iostream>
#include <math.h>
#include <iomanip>

long double aFunction(long const double &x)
{
    long double xPrime{0.5*x + 0.5} ;
    return (pow(xPrime, 3) / (xPrime + 1)) * cos(pow(xPrime, 2));
}

int main(int argc, char *argv[])
{
    long double (*pf)(const long double &);
    pf = &aFunction;
    
    int n = atoi(argv[1]);
    CGaussSolver aSolver(pf, 0, 1, n);
    aSolver.exec();
    std::cout.precision(20);
    std::cout << "Result of C++ code (n = "<< std::setw(2) << n << "): "<< aSolver.getResult() << std::endl;
    return 0;
}
