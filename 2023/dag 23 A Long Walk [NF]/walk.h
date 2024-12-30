#ifndef GUARD_H
#define GUARD_H

#include "standaard.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <set>
#include <tuple>
#include <map>
#include <queue>
struct Point {
    int x, y;
};
struct Node {
    int x, y; // Coördinaten van de knoop
    std::vector<std::pair<Node*, int>> neighbors; // Verbindingen (pointer naar buur, kost)

    Node(int x, int y) : x(x), y(y) {}
};

class Walk {
private:
    int ROWS ;
    int COLS ;
    char Field[MAXROWS][MAXCOLS];
    char Copy[MAXROWS][MAXCOLS];
    int aantalRoutesREC(int x, int y);

    Node* getNode(int x, int y);
    int calculateDistance(Point start, Point end);

public:

    int aantalRoutes();
    void readInputTo2DArray(const std::string& filename);
    void printField();
    std::map<std::pair<int, int>, Node*> nodes; // Knopen geïndexeerd op coördinaten

    void buildTree();
    int findLongestPath(Node* start);
    void printTree();
};
#endif