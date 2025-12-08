#include "table.h"

    //functie om kolommen toe te voegen aan de tabel
    void Table::addCell(char value, int link1, int link2, int link3, int link4, int link5, bool isendstates) {
        values.push_back(value);                      // Voeg karakter toe
        links.emplace_back(link1, link2, link3, link4, link5);      // Voeg een tuple van drie integers toe
        endstates.push_back(isendstates);
    }
//debug functie om te kijken of alle knopen gelinkt zijn 
    void Table::printTable() const {
        std::cout << "\tValue\tLink1\tLink2\tLink3\tlink4\n";
        for (size_t i = 0; i < values.size(); ++i) {
            std::cout <<  "\t" << values[i] << "\t";
            std::cout << std::get<0>(links[i]) << "\t"; // vertrek punt
            std::cout << std::get<1>(links[i]) << "\t"; // eind punt 1
            std::cout << std::get<2>(links[i]) << "\n"; // eind punt 2
            std::cout << std::get<3>(links[i]) << "\n"; // eind punt 3
            std::cout << std::get<4>(links[i]) << "\n"; // eind punt 4
        }
    }

void Table::printDot(std::ostream& out) const {
    out << "digraph Table {rankdir=\"LR\"" << std::endl; // Begin van de DOT-definitie
    out << "  node [shape=circle];" << std::endl;

    // Itereer over de cellen in de tabel
    for (size_t i = 0; i < values.size(); ++i) {
        char value = values[i]; // Het karakter
        int link1 = std::get<0>(links[i]); // Haal het vertrekpunt op
        int link2 = std::get<1>(links[i]); // Haal de eindpunten op
        int link3 = std::get<2>(links[i]);
        int link4 = std::get<3>(links[i]);
        int link5 = std::get<4>(links[i]);
        // Controleer of de pijl van 0 naar iets gaat met een '#'
        if (link2 != 0 && link2 != -1) {
            
                out << link1 << " -> " << link2;
                if (value != ' ' ) {
                    out << " [label=\"" << value << "\"]" << std::endl;
                } else {
                    out << std::endl;
                }
            
        }
        if (link4 != 0) {
                out << link1 << " -> " << link4;
                if (value != ' ') {
                    out << " [label=\"" << value << "\"]" << std::endl;
                } else {
                    out << std::endl;
                }
            
        }
        if (link5 != 0) {
                out << link1 << " -> " << link5;
                if (value != ' ') {
                    out << " [label=\"" << value << "\"]" << std::endl;
                } else {
                    out << std::endl;
                }
            
        }
        if (link3 != 0) {
                out << link1 << " -> " << link3;
                if (value != ' ') {
                    out << " [label=\"" << value << "\"]" << std::endl;
                } else {
                    out << std::endl;
                }
            
        }
    }

    // Maak knooppunt 0 onzichtbaar als er een pijl is die naar iets anders wijst en het label is '#'
    for (size_t i = 0; i < values.size(); ++i) {
        if (std::get<0>(links[i]) == 0 ) {
            out << "  0 [style=invis];" << std::endl; // Maak knooppunt 0 onzichtbaar
        }
        if ( std::get<1>(links[i]) == -1)  {
            out << std::get<0>(links[i]) << "   [shape=doublecircle];" << std::endl; // Maak knooppunt -1 een dubbele cirkel
            
        }
    }

    out << "}" << std::endl; // Sluit de DOT-definitie
}


    // Getter voor een value op index i
char Table::getValue(size_t i) const {
    if (i < values.size()) {
        return values[i];
    }
    throw std::out_of_range("Index out of range for getValue.");
}

bool Table::getendstate(size_t i) const {
    if (i < endstates.size()) {
        return endstates[i];
    }
    throw std::out_of_range("Index out of range for getValue.");
}

    // Getter voor een link (link1, link2, link3) op index i
std::tuple<int, int, int, int, int> Table::getLinks(size_t i) const {
    if (i < links.size()) {
        return links[i];
    }
    throw std::out_of_range("Index out of range for getLinks.");
}

size_t Table::size() const {
    return values.size();
}

void Table::add_endstates(){
    bool gelukt = true;  // Start met 'true', omdat we gaan proberen cellen toe te voegen

    // Blijf door de loop gaan totdat er geen nieuwe cellen meer worden toegevoegd
    while (gelukt) {
        gelukt = false;  // Stel gelukt in op false, zodat we weten of er een verandering is

        for (size_t i = 0; i < values.size(); ++i) {
            for (size_t j = 0; j < values.size(); ++j){
                // Controleer of een overgang naar -1 mogelijk is, en de overgang het juiste karakter heeft (' ')
                if (endstates[j] && (std::get<0>(links[j]) == std::get<1>(links[i]) || std::get<0>(links[j]) == std::get<2>(links[i])) && values[i] == ' '&& !endstates[i])  {
                    endstates[i] = true;
                    // Geef aan dat er een wijziging is geweest
                    gelukt = true;
                }
            }
        }
    }
}

