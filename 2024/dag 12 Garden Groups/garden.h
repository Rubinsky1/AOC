#ifndef GARDEN_H
#define GARDEN_H

#include <ostream>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include<set>
class Garden {
private:
    std::vector<std::vector<char>> Field;
    int Width = 0;
    int Height = 0;
    int zoekgroep1(int row, int col, std::vector<std::vector<bool>>& bezocht, int& grootte, char k);
    int zoekgroep2(int row, int col, std::vector<std::vector<bool>>& bezocht, int& grootte, char k);
public:
    int groepGrote(bool opdracht);
    void readInputTo2DArray(const std::string& filename);
    void printField();


};

#endif