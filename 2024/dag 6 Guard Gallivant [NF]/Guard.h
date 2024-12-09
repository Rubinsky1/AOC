#ifndef GUARD_H
#define GUARD_H

#include "standaard.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <set>
#include <tuple>
class Guard {
private:
    char Field[ROWS][COLS];
    char Copy[ROWS][COLS];
    bool moveForward(int& x, int& y, char& dir);
    char turnRight(char dir);
    bool findStartPosition(int& x, int& y, char& dir);
    std::set<std::tuple<int, int, char>> visited_positions;  // Set voor bezochte posities met richting
    bool isInLoop(int x, int y, char dir);
    void reset();
public:
    Guard();
    int visited_count = 0;
    void readInputTo2DArray(const std::string& filename);
    void printField();
    bool startPatrol();
    int testloops();
};

#endif