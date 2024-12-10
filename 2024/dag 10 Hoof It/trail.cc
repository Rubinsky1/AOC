#include "trail.h"


void Trail::readInputTo2DArray(const std::string& filename) {
    std::ifstream file(filename);  // Open het bestand voor lezen
    std::string line;

    Field.clear(); // Zorg ervoor dat het veld leeg is voordat je begint

    // Lees het bestand regel voor regel
    while (std::getline(file, line)) {
        std::vector<int> row;

        // Converteer elk karakter in de regel naar een integer en voeg toe aan de rij
        for (char ch : line) {
            if (std::isdigit(ch)) { // Controleer of het karakter een cijfer is
                row.push_back(ch - '0'); // Converteer van 'char' naar 'int'
            }
        }

        Field.push_back(row); // Voeg de rij toe aan het veld
    }

    // Sluit het bestand
    file.close();
}

void Trail::printField() {
    for (const auto& row : Field) {
        for (const auto& cell : row) {
            std::cout << cell<<" ";
        }
        std::cout << std::endl;
    }
}

int Trail::findRoutes() {
    int allRoutes = 0;

    // Start DFS vanaf elk vakje met waarde 0
    for (size_t i = 0; i < Field.size(); ++i) {
        for (size_t j = 0; j < Field[i].size(); ++j) {
            if (Field[i][j] == 0) {
                allRoutes += dfs(i, j);
            }
        }
    }

    // Print gevonden routes
    return allRoutes ;
}

int Trail::dfs(int x, int y) {
    int score = 0;
    // Controleer of we een eindpunt hebben bereikt (waarde 9)
    if (Field[x][y] == 9) {
        return 1;
    }

    // Verken alle mogelijke richtingen
    for (const auto& dir : directions) {
        int newX = x + dir.first;
        int newY = y + dir.second;

        if (isValidMove(newX, newY, Field[x][y])) {
            score += dfs(newX, newY);
        }
    }

    return score;
}

bool Trail::isValidMove(int x, int y, int currentValue) {
    size_t copyx = x;
    size_t copyy = y;
    // Controleer of de nieuwe positie binnen de grenzen ligt
    if (x < 0 || y < 0 || copyx >= Field.size() || copyy >= Field[0].size()) {
        return false;
    }

    // Controleer of het vakje exact 1 hoger is en niet eerder bezocht
    return (Field[x][y] == currentValue + 1 );
}

int Trail::findTrailheads() {
    int trailscore = 0;

    for (size_t i = 0; i < Field.size(); ++i) {
        for (size_t j = 0; j < Field[i].size(); ++j) {
            if (Field[i][j] == 0) { // Trailhead gevonden
                int score = calculateTrailheadScore(i, j); // Bereken de score van deze trailhead
                trailscore += score;
            }
        }
    }

    return trailscore;
}

int Trail::calculateTrailheadScore(int x, int y) {
    std::set<std::pair<int, int>> visitedNodes; // Unieke vakjes met waarde 9 die we bereiken
    std::vector<std::pair<int, int>> stack = {{x, y}}; // DFS-stack
    

    while (!stack.empty()) {
        auto [currX, currY] = stack.back();
        stack.pop_back();

        for (const auto& dir : directions) {
            int newX = currX + dir.first;
            int newY = currY + dir.second;

            if (isValidMove(newX, newY, Field[currX][currY])) {
                if (Field[newX][newY] == 9) {
                    visitedNodes.insert({newX, newY}); // Voeg unieke 9 toe
                } else {
                    stack.emplace_back(newX, newY); // Voeg nieuwe positie toe aan stack
                }          
            }
        }
    }

    return visitedNodes.size(); // Retourneer het aantal unieke 9's
}