#include "antenna.h"







int main() {
    Antenna A;
    std::string filename = "dag8.txt"; // Bestand waar je input vandaan komt
    A.readInputTo2DArray(filename); // Roep de functie aan om in te lezen en af te drukken
    A.createSignals(0);
    std::cout<<"aantal signalen:"<<A.countSignals()<<"\n";
    Antenna B;
    B.readInputTo2DArray(filename); // Roep de functie aan om in te lezen en af te drukken
    B.createSignals(1);
    std::cout<<"aantal signalen:"<<B.countSignals()<<"\n";
    return 0;
}