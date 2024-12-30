#include "walk.h"







int main() {
    Walk W;
    std::string filename = "dag23.txt"; // Bestand waar je input vandaan komt
    W.readInputTo2DArray(filename); // Roep de functie aan om in te lezen en af te drukken
    
    //W.printField();
    W.aantalRoutes();
    W.buildTree();
    W.printTree();
    // std::cout << "Aantal bezochte posities: " << G.visited_count << std::endl;
    // //G.printField();
    // std::cout << "Aantal gevonden loops: " << G.testloops() << std::endl;
    return 0;
}