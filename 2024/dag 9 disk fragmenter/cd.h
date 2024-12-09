#ifndef CD_H
#define CD_H

#include <string>
#include <vector>

class Cd {
private:
    std::vector<int> blocks; // Diskmap als een vector van bestand-IDs en '.'
    void compactDisk();
    void compactDisk2();
public:
    Cd(const std::string& diskMap); // Constructor die de disk-map parset
    long long int calculateChecksum(int choose);        // Berekent de checksum

};

#endif