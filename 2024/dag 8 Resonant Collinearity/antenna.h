#ifndef antenna_H
#define antenna_H

#include "standaard.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
class Antenna {
private:
    char Field[ROWS][COLS];
    char signals[ROWS][COLS];
public:
    Antenna();
    void readInputTo2DArray(const std::string& filename);
    void printField();
    void printSignals();
    void createSignals(int choice);
    int countSignals();
};

#endif