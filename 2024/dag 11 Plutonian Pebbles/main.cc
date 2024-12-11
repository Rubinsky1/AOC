#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <utility>

#include <unordered_map>

using namespace std;

void remove_duplicates_and_count(std::vector<pair< long long, long long>>& array) {
    // Maak een unordered_map om de frequentie van elk getal te tellen, rekening houdend met alle 'second' waardes
    std::unordered_map<long long, long long> frequency_map;

    for (const auto& p : array) {
        frequency_map[p.first] += p.second;  
    }

    array.clear();
    for (const auto& entry : frequency_map) {
        array.push_back(make_pair(entry.first, entry.second));  
    }
}

int main(int argc, char* argv[]) {
    // Controleer of er een argument is meegegeven
    if (argc != 2) {
        cerr << "Gebruik: " << argv[0] << " <aantal_loops>" << endl;
        return 1;  // Foutcode als het aantal argumenten niet klopt
    }

    // Verkrijg het aantal loops van het argument
    int aantal_loops = atoi(argv[1]); // atoi converteert de string naar een int
    std::ifstream file("dag11.txt");
    std::vector<pair<long long, long long>> array;

    if (file.is_open()) {
        std::string line;
        std::getline(file, line); 
        std::istringstream iss(line);
        int num;
        while (iss >> num) {

            array.push_back(make_pair(num, 1)); 
        }
        file.close();
    } else {
        std::cerr << "Kan bestand niet openen." << std::endl;
        return 1;
    }
    std::vector<pair<long long, long long>> new_array; // Nieuwe array

    for (int iteration = 0; iteration < aantal_loops; ++iteration) {
        new_array.clear();

        for (size_t i = 0; i < array.size(); ++i) {
            long long stone = array[i].first; // Eerste waarde van het paar (getal)
            long long amount = array[i].second;
            if (stone == 0) {
                new_array.push_back(make_pair(1, amount)); // Als de steen 0 is, vervang het door 1
            } else if (std::to_string(stone).length() % 2 == 0) {
                // Als de lengte van het getal even is, splitsen we het
                std::string num_str = std::to_string(stone);
                int mid = num_str.length() / 2;
                new_array.push_back(make_pair(std::stoi(num_str.substr(0, mid)), amount)); // Eerste deel
                new_array.push_back(make_pair(std::stoi(num_str.substr(mid)), amount));   // Tweede deel
            } else {
                new_array.push_back(make_pair(stone * 2024, amount)); // Anders vermenigvuldigen we het getal met 2024
            }
        }
        remove_duplicates_and_count(new_array);

        array = new_array; // Werk de originele array bij
    }

    long long totaal = 0;
    for(size_t i = 0; i < array.size(); i++){
        totaal += array[i].second;
    }
    std::cout << "Lengte van new_array: " << totaal << std::endl;

    return 0;
}
