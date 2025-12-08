#ifndef MAZE_H
#define MAZE_H
#include <vector>
#include <tuple>
#include <utility>
#include <iostream>
#include <sstream>
#include "table.h"

class Maze {
public:
    void loaddata(std::string filename);
    Maze() : table() {}
    void printDot(std::ostream& out) const {
        table.printDot(out);
    }
    int cheapestpath();
    void simplify();
private:
    Table table;
    int starty;
    int startx;
};

#endif