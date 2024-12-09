#include "antenna.h"

Antenna::Antenna(){
    for (int i = 0; i < ROWS; ++i) {
        for (int j = 0; j < COLS; ++j) {
            signals[i][j] = '.';
        }
        
    }
}

void Antenna::readInputTo2DArray(const std::string& filename) {
    
    std::ifstream file(filename);  // Open het bestand voor lezen
    std::string line;
    int row = 0;

    // Lees het bestand regel voor regel
    while (std::getline(file, line) && row < ROWS) {
        for (size_t col = 0; col < line.size() && col < COLS; ++col) {
            Field[row][col] = line[col]; // Vul de array met karakters uit de input
        }
        ++row;
    }

    // Sluit het bestand
    file.close();


}

void Antenna::printField(){
    // Print de 2D array
    for (int i = 0; i < ROWS; ++i) {
        for (int j = 0; j < COLS; ++j) {
            std::cout << Field[i][j];
        }
        std::cout << std::endl;
    }
}
void Antenna::printSignals(){
        // Print de 2D array
    for (int i = 0; i < ROWS; ++i) {
        for (int j = 0; j < COLS; ++j) {
            std::cout << signals[i][j];
        }
        std::cout << std::endl;
    }
}

// Functie om de signalen te creëren
void Antenna::createSignals(int choice) {
    // We doorlopen het veld om alle antennes te vinden
    for (int i = 0; i < ROWS; ++i) {
        for (int j = 0; j < COLS; ++j) {
            if (Field[i][j] != '.') {  // Er is een antenne op deze positie
                char antenna = Field[i][j];

                // We doorzoeken het veld opnieuw om dezelfde antennes te vinden
                for (int x = 0; x < ROWS; ++x) {
                    for (int y = 0; y < COLS; ++y) {
                        if (Field[x][y] == antenna && (x != i || y != j)) { // Zelfde antenne, niet dezelfde positie

                            
                            // Antinodes worden op de juiste plekken geplaatst
                            for(int k = 0; k<ROWS;k++){
                                if(choice == 0)k = 2;
                                int antinodeX = i + (x - i)*k ;
                                int antinodeY = j + (y - j)*k ;

                                // Controleer of de antinode binnen de grenzen valt
                                if (antinodeX >= 0 && antinodeX < ROWS && antinodeY >= 0 && antinodeY < COLS) {
                                    signals[antinodeX][antinodeY] = '#'; // Zet een antinode
                                }
                                if(choice == 0)break;
                            }
                        }
                    }
                }
            }
        }
    }
}

int Antenna::countSignals(){
    int count = 0;
    for (int i = 0; i < ROWS; ++i) {
        for (int j = 0; j < COLS; ++j) {
            if (signals[i][j] == '#')count++;
        }
    }
    return count;
}