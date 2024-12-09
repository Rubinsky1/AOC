#include "cd.h"
#include <iostream>
#include <fstream>
std::string readFromFile(std::string& filename) {
    std::ifstream file(filename);

    std::string content;
    std::getline(file, content); // Lees de eerste regel (verwacht dat de disk-map in één regel staat)
    file.close();
    return content;
}

int main() {
    // Voorbeeldinput
    
    std::string filename = "dag9.txt"; // Bestand met de disk-map
    std::string diskMap = readFromFile(filename);

    // Maak een Cd-object en bereken de checksum
    Cd cd(diskMap);

    std::cout << "Checksum exercise 1: " << cd.calculateChecksum(0) << std::endl;
    Cd cd2(diskMap);
    std::cout << "Checksum exercise 2: " << cd2.calculateChecksum(1) << std::endl;
    return 0;
}
