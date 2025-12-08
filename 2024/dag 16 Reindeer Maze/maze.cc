#include "maze.h"

#include <fstream>
#include <iostream>
#include <string>
#include <unordered_set>
#include <stack>
void Maze::loaddata(std::string filename) {
    std::ifstream infile(filename);
    if (!infile) {
        std::cerr << "Unable to open file";
        return;
    }

    std::string line;
    std::vector<std::vector<char>> maze;
    int width = 0;
    int height = 0;
    while (std::getline(infile, line)) {
        std::vector<char> row;
        for (char c : line) {
            row.push_back(c);
        }
        if (width == 0) {
            width = row.size() -1;
        }
        maze.push_back(row);
        height++;
    }
    std::cout << "Width: " << width << ", Height: " << height << std::endl;
    for (int i = height-2; i > 0; i--) {
        for (int j = 1; j < width-1; j++) {
            if (maze[i][j] != '#') {
                if (maze[i][j] == 'S') {
                    table.addCell(' ', 0, i*100 + j, 0, 0, 0, false);
                    starty = i;
                    startx = j;
                }

                int currentNode = i * 100 + j;
                int link1 = 0;
                int link2 = 0;
                int link3 = 0;
                int link4 = 0;
                if (maze[i-1][j] != '#')link1 = (i - 1) * 100 + j; // Node below
                if (maze[i+1][j] != '#')link3 = (i + 1) * 100 + j; // Node above
                if (maze[i][j+1] != '#')link2 = i * 100 + (j + 1); // Node to the right
                if (maze[i][j-1] != '#')link4 = i * 100 + (j - 1); // Node to the left



                bool isEnd = (maze[i][j] == 'E');
                table.addCell(' ', currentNode, link1, link2, link3, link4, isEnd);
                if (isEnd) {
                    table.addCell(' ', currentNode, -1, 0, 0, 0, false);
                }
            }
        }
    }
    infile.close();
}

void maze::simplify(){
    Table newTable;
    std::unordered_set<int> visited;
    newTable.addCell(' ', 0, starty * 100 + startx, 0, 0, 0, false);
    table = hulpSimplify(starty * 100 + startx, visited, newTable, 0);
}

Table maze::hulpsimplify(int current, std::unordered_set<int> visited, Table newTable, int direction){
    if (current == 0){
        return newTable;
    }
    std::tuple<int, int, int, int, int> cell;
    std::tuple<int, int, int, int, int> cellhulp;
    for (size_t i = 0; i < table.size(); i++) {
        cell = table.getLinks(i);
        int link1 = std::get<0>(cell);
        if (link1 == current) {
            isend = table.getendstate(i);
            if (isend) {
                std::cout << "end" << current << std::endl;
                newTable.addCell(' ', current, -1, 0, 0, 0, false);
            }
            break;
        }
    }
    while(direction ==1 && std::get<2>(cell) == 0 && std::get<4> == 0 && std::get<3> != 0){
        int newcurrent = std::get<3>(cell);
        for (size_t i = 0; i < table.size(); i++) {
            cellhulp = table.getLinks(i);
            int link1 = std::get<0>(cellhulp);
            if (link1 == newcurrent) {
                isend = table.getendstate(i);
                if (isend) {
                    std::cout << "end" << newcurrent << std::endl;
                    newTable.addCell(' ', newcurrent, -1, 0, 0, 0, false);
                }
                break;
            }
        }
  
    }
    newTable.addCell(' ', current, newcurrent, 0, 0, 0, false);
    newTable = hulpSimplify(std::get<1>(cell), visited, newTable, direction);
    newTable = hulpSimplify(std::get<2>(cell), visited, newTable, direction);
    newTable = hulpSimplify(std::get<3>(cell), visited, newTable, direction);
    newTable = hulpSimplify(std::get<4>(cell), visited, newTable, direction);
}
// void Maze::simplify() {
//     Table newTable;
//     std::unordered_set<int> visited;
//     std::stack<int> s;
//     std::tuple<int, int, int, int, int> cell;
//     bool isend = false;
//     s.push(starty * 100 + startx);
//     visited.insert(starty * 100 + startx);
//     newTable.addCell(' ', 0, starty * 100 + startx, 0, 0, 0, false);
//     while (!s.empty()) {
//         isend = false;
//         int current = s.top();
//         s.pop();
//         for (size_t i = 0; i < table.size(); i++) {
//             cell = table.getLinks(i);
//             int link1 = std::get<0>(cell);
//             if (link1 == current) {
//                 isend = table.getendstate(i);
//                 if (isend) {
//                     std::cout << "end" << current << std::endl;
//                     newTable.addCell(' ', current, -1, 0, 0, 0, false);
//                 }
//                 break;
//             }
//         }

//         std::vector<int> links = {std::get<1>(cell), std::get<2>(cell), std::get<3>(cell), std::get<4>(cell)};
//         for (int link : links) {
//             if (link != 0 && visited.find(link) == visited.end()) {
//                 s.push(link);
//                 visited.insert(link);
//             }
//         }

//         newTable.addCell(' ', current, std::get<1>(cell), std::get<2>(cell), std::get<3>(cell), std::get<4>(cell), false);
//     }

//     table = newTable;
// }

int Maze::cheapestpath(){

}