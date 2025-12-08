#ifndef TABLE_H
#define TABLE_H

#include <iostream>
#include <vector>
#include <tuple>

class Table {
private:
    std::vector<char> values;                               // Vector voor de karakters
    std::vector<std::tuple<int, int, int, int, int>> links;         // Vector voor paren van links (begin, eind, eind)
    std::vector<bool> endstates;
public:
    // Voeg een cel toe aan de tabel
    void addCell(char value, int link1, int link2, int link3, int link4, int link5, bool isendstate);
    // Print de volledige tabel
    void printTable() const;
    //print een dot file uit de tabel
    void printDot(std::ostream& out) const;
    char getValue(size_t i) const;
    std::tuple<int, int, int, int, int> getLinks(size_t i) const;
    size_t size() const;
    void add_endstates();
    bool getendstate(size_t i) const;
};

#endif