#include "Guard.h"







int main() {
    Guard G;
    std::string filename = "dag6.txt"; // Bestand waar je input vandaan komt
    G.readInputTo2DArray(filename); // Roep de functie aan om in te lezen en af te drukken
    
    G.startPatrol();
    std::cout << "Aantal bezochte posities: " << G.visited_count << std::endl;
    //G.printField();
    std::cout << "Aantal gevonden loops: " << G.testloops() << std::endl;
    return 0;
}