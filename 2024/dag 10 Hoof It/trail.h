#ifndef trail_H
#define trail_H


#include <iostream>
#include <fstream>
#include <vector>
#include<set>
class Trail {
private:
    std::vector<std::vector<int>> Field;
    
    const std::vector<std::pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // Richtingen (boven, onder, links, rechts)

    bool isValidMove(int x, int y, int currentValue); // Controleer geldigheid van de beweging
    int dfs(int x, int y); // Depth-First Search
    int calculateTrailheadScore(int x, int y); // Bereken de score voor een specifieke trailhead
    
public:

    int findRoutes(); // Zoek routes van 0 naar 9
    void readInputTo2DArray(const std::string& filename);
    void printField();

    int findTrailheads(); // Zoek trailheads en bereken scores

};

#endif