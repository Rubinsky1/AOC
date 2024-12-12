#include "garden.h"



int main() {
    Garden G;
    std::string filename = "dag12.txt"; // Bestand waar je input vandaan komt
    G.readInputTo2DArray(filename); // Roep de functie aan om in te lezen en af te drukken
    std::cout<<"deel1:"<<G.groepGrote(false)<<"\n";
    std::cout<<"deel2:"<<G.groepGrote(true)<<"\n";
}