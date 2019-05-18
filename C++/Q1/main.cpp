#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <execution>

template <typename T>
void printContainer(const T &, const char *);

int main()
{
    // part a
    std::vector<int> vec1(100), vec2(10);
    int i{1};
    std::generate(vec1.begin(), vec1.end(), [&i]() { return i++; });
    printContainer(vec1, "vec1 is:");
    i = 1;
    std::generate(vec2.begin(), vec2.end(), [&i]() { return i++; });
    printContainer(vec2, "vec2 is:");
    // part b
    vec2.resize(110);
    std::copy(vec1.begin(), vec1.end(), vec2.begin() + 10);
    printContainer(vec2, "vec2 is:");
    // part c
    std::vector<int> odd_vec(50);
    std::copy_if(vec1.begin(), vec1.end(), odd_vec.begin(), [](const int &num) { return num % 2; });
    printContainer(odd_vec, "odd_vec is:");
    // part d
    std::vector<int> reverse_vec(100);
    std::copy(vec1.rbegin(), vec1.rend(), reverse_vec.begin());
    printContainer(reverse_vec, "reverse_vec is:");
    // part f
    std::sort(std::execution::par_unseq, vec2.begin(), vec2.end());
    printContainer(vec2, "vec2 is:");

    return 0;
}

template <typename T>
void printContainer(const T &arr, const char *message)
{
    std::cout << message << std::endl;
    std::for_each(arr.begin(), arr.end(), [](const auto &var) { std::cout << var << ", "; });
    std::cout << std::endl;
}