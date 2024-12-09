#include "cd.h"
#include <sstream>
#include <iostream>
#include <cctype>
#include <algorithm> // Voor std::remove
Cd::Cd( const std::string& diskMap) {
    int id = 0; // Huidige bestand-ID
    for (size_t i = 0; i < diskMap.size(); i += 2) {
        int fileSize = diskMap[i] - '0'; // Grootte van het bestand
        int freeSpace = (i + 1 < diskMap.size()) ? diskMap[i + 1] - '0' : 0; // Vrije ruimte
        
        // Voeg bestand-ID toe voor elke blok van het bestand
        for (int j = 0; j < fileSize; ++j) {
            blocks.push_back(id); // Bestand-ID als integer
        }
        // Voeg vrije ruimte toe
        for (int j = 0; j < freeSpace; ++j) {
            blocks.push_back(-1); // Gebruik bijvoorbeeld -1 om vrije ruimte aan te geven
        }
        id++; // Volgende bestand-ID
    }


    std::cout << std::endl;
}

void Cd::compactDisk() {
    for (size_t i = blocks.size(); i-- > 0;) { // Itereer van rechts naar links
        if (blocks[i] == -1) continue; // Sla vrije ruimte over
        // Zoek de dichtstbijzijnde vrije ruimte links
        for (size_t j = 0; j < i; ++j) {
            if (blocks[j] == -1) {
                blocks[j] = blocks[i]; // Verplaats bestand naar vrije ruimte
                blocks[i] = -1;      // Maak de oude positie vrij
                break;
            }
        }
    }
}

void Cd::compactDisk2() {
    // Begin met de bestanden met het hoogste ID
    for (size_t i = blocks.size(); i-- > 0;) { // Itereer van rechts naar links
        if (blocks[i] == -1) continue; // Sla vrije ruimte over
        
        // Bepaal de bestandsgrootte door te kijken naar opeenvolgende blokken van hetzelfde bestand
        int bestandsgrootte = 0;
        int huidige = blocks[i];
        size_t beginIndex = i;  // Onthoud het begin van het bestand
        while (i > 0 && blocks[i - 1] == huidige) {
            bestandsgrootte++;
            i--;
        }
        bestandsgrootte++; // Vergeet niet het laatste blok mee te nemen

        // Zoek naar vrije ruimte die groot genoeg is om het bestand te verplaatsen
        for (size_t j = 0; j < beginIndex; ++j) {
            if (blocks[j] == -1) {
                int legegrootte = 0;
                size_t huidigepos = j;
                
                // Zoek het einde van de vrije ruimte
                while (huidigepos < blocks.size() && blocks[huidigepos] == -1) {
                    legegrootte++;
                    huidigepos++;
                }

                // Als er voldoende vrije ruimte is, verplaats het bestand
                if (bestandsgrootte <= legegrootte) {
                    for (int h = 0; h < bestandsgrootte; h++) {
                        blocks[j + h] = huidige; // Verplaats bestand naar vrije ruimte
                        blocks[beginIndex - h] = -1; // Maak de oude positie vrij
                    }
                    break; // Breek de loop zodra het bestand is verplaatst
                }
            }
        }
    }
}



long long int Cd::calculateChecksum(int choose) {
    if (choose == 1){
        compactDisk2();
    }
    if(choose == 0) compactDisk();
    long long int checksum = 0;

    for (size_t i = 0; i < blocks.size(); ++i) {
        if (blocks[i]!=-1){
        
        checksum += i * blocks[i];      // Positie * bestand-ID
        }
    }
    return checksum;
}


