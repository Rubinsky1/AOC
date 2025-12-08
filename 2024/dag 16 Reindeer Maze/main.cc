#include "maze.h"
#include <fstream>



int main() {
    Maze M;
    M.loaddata("test.txt");
    std::ofstream outFile("test.dot");
    M.printDot(outFile);
    M.simplify();
    std::ofstream outFile2("test1.dot");
    M.printDot(outFile2);
    outFile.close();
    std::cout<<"Opdracht1: "<<""<<std::endl;
    std::cout<<"Opdracht2: "<<""<<std::endl;
    return 0;
}