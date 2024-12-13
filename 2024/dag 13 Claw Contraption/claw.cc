#include "claw.h"


void Claw::loadData(std::istream& input) {
    std::string line;
    long long extrafun = 10000000000000;
    while (std::getline(input, line)) {
        Pair pair1, pair2, pair3, pair4;

        // Eerste regel inlezen
        std::istringstream iss1(line);
        iss1 >> pair1.first >> pair1.second;

        // Tweede regel inlezen
        if (!std::getline(input, line)) break;
        std::istringstream iss2(line);
        iss2 >> pair2.first >> pair2.second;

        // Derde regel inlezen
        if (!std::getline(input, line)) break;
        std::istringstream iss3(line);
        iss3 >> pair3.first >> pair3.second;
        pair4.first = pair3.first + extrafun;
        pair4.second = pair3.second + extrafun;
        data.emplace_back(pair1, pair2, pair3);
        data2.emplace_back(pair1, pair2, pair4);
        if (!std::getline(input, line)) break;
        // Tuple maken en toevoegen aan de vector
        
    }
}

void Claw::printData() const {
    for (const auto& t : data) {
        const auto& [p1, p2, p3] = t;
        std::cout << "Pair 1: (" << p1.first << ", " << p1.second << "), ";
        std::cout << "Pair 2: (" << p2.first << ", " << p2.second << "), ";
        std::cout << "Pair 3: (" << p3.first << ", " << p3.second << ")\n";
    }
}


long long Claw::cheapestit(bool opdracht){
    long long totaal = 0;
    
    const auto& datahulp = data;
    if(opdracht)    data=data2;
    
    for (const auto& t : data) {

        const auto& [p1, p2, p3] = t;
        std::pair<long long, long long> pair = cramersRule(p1.first, p2.first, p1.second, p2.second, p3.first, p3.second);
        long long laagste = pair.first*3+pair.second*1;
        totaal+=laagste;
    }
    data = datahulp;
    return totaal;
}

std::pair<long long, long long> Claw::cramersRule(long long a, long long b, long long c, long long d, long long e, long long f) {
    std::pair<long long, long long> pair;

    long long detA = a * d - b * c;
    long long detA1 = e * d - b * f;
    long long detA2 = a * f - e * c;
    //std::cout<<"\n"<<detA<<","<<detA1<<","<<detA2<<"\n";
    // Als de determinant van de coefficientmatrix 0 is, is er geen oplossing
    if (detA == 0) {
        pair.first = 0;
        pair.second = 0;
        return pair;
    }

    // Check of de uitkomst van de delingen een geheel getal is
    if (detA1 % detA != 0 || detA2 % detA != 0) {
        pair.first = 0;
        pair.second = 0;
    } else {
        pair.first = detA1 / detA;
        pair.second = detA2 / detA;
    }
    //std::cout<<"\n"<<pair.first<<","<<pair.second<<"\n";
    return pair;
}
