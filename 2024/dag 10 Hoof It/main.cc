#include "trail.h"







int main() {
    Trail T;
    std::string filename = "dag10.txt"; // Bestand waar je input vandaan komt
    T.readInputTo2DArray(filename); // Roep de functie aan om in te lezen en af te drukken
    std::cout<<"totaal aantal trailheads: "<< T.findTrailheads()<<"\n";
    std::cout<<"totaal aantal routes:"<<T.findRoutes()<<"\n";
    
}