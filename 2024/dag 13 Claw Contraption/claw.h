#ifndef CLAW_H
#define ClAW_H
#include <vector>
#include <tuple>
#include <utility>
#include <iostream>
#include <sstream>

class Claw {
public:
    using Pair = std::pair<long long, long long>;
    using Triple = std::tuple<Pair, Pair, Pair>;

    void loadData(std::istream& input);
    void printData() const;
    long long cheapestit(bool opdracht);
    std::pair<long long, long long> cramersRule(long long a, long long b, long long c, long long d, long long e, long long f);
private:

    std::vector<Triple> data;
    std::vector<Triple> data2;
};

#endif