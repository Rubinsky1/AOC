#include "walk.h"



void Walk::readInputTo2DArray(const std::string& filename) {
    
    std::ifstream file(filename);  // Open het bestand voor lezen
    std::string line;
    ROWS = 0;

    // Lees het bestand regel voor regel
    while (std::getline(file, line)) {
        COLS = line.size();
        for (size_t col = 0; col < line.size() ; ++col) {
            Field[ROWS][col] = line[col]; // Vul de array met karakters uit de input
            Copy[ROWS][col] = line [col];
        }
        ++ROWS;
    }
    // Sluit het bestand
    file.close();


}

void Walk::printField(){
    // Print de 2D array
    for (int i = 0; i < ROWS; ++i) {
        for (int j = 0; j < COLS; ++j) {
            std::cout << Field[i][j];
        }
        std::cout << std::endl;
    }
}

int Walk::aantalRoutes(){
    int starty = 0;
    int startx = 1;
    int totaal = aantalRoutesREC(startx, starty)-3;
    std::cout<<totaal<<std::endl;
    return totaal;
}

int Walk::aantalRoutesREC(int x, int y) {
    int maxstep = 0;
    char temp;
    bool stapgezet = false;

    // Controleer of de huidige positie ongeldig is
    if (x < 0 || x > COLS || y < 0 || y > ROWS || Field[y][x] == 'O') return 0;
    if (Field[y][x] == '#') return 0;

    // Controleer of het doel is bereikt
    if (y == ROWS && x == COLS - 1) return 1;
    //std::cout<<x<<" "<<y<<"\n";
    // Markeer het huidige veld als bezocht
    temp = Field[y][x];
    Field[y][x] = 'O';

    // Verken de vier richtingen
    if (Field[y][x + 1] != '<') maxstep = std::max(maxstep, aantalRoutesREC(x + 1, y));
    if (Field[y][x - 1] != '>') maxstep = std::max(maxstep, aantalRoutesREC(x - 1, y));
    if (Field[y + 1][x] != '^') maxstep = std::max(maxstep, aantalRoutesREC(x, y + 1));
    if (Field[y - 1][x] != 'v') maxstep = std::max(maxstep, aantalRoutesREC(x, y - 1));

    // Herstel de oorspronkelijke waarde van het veld
    Field[y][x] = temp;

    // Als een stap is gezet, verhoog `maxstep`
    if (maxstep > 0) stapgezet = true;
    return maxstep + (stapgezet ? 1 : 0);
}

void Walk::printTree() {
    for (const auto& [key, node] : nodes) {
        std::cout << "Node (" << node->x << ", " << node->y << ") is connected to:\n";
        for (const auto& [neighbor, cost] : node->neighbors) {
            std::cout << "  -> Node (" << neighbor->x << ", " << neighbor->y << ") with cost " << cost << "\n";
        }
        std::cout << std::endl;
    }
}


Node* Walk::getNode(int x, int y) {
    auto key = std::make_pair(x, y);
    if (nodes.find(key) == nodes.end()) {
        nodes[key] = new Node(x, y);
    }
    return nodes[key];
}
// Struct voor een punt


// Functie om de afstand tussen twee punten te berekenen
int Walk::calculateDistance(Point start, Point end) {
    int distance = 0;
    std::queue<Point> toVisit;
    std::map<std::pair<int, int>, bool> visited;
    
    toVisit.push(start);
    visited[{start.x, start.y}] = true;
    
    while (!toVisit.empty()) {
        Point current = toVisit.front();
        toVisit.pop();
        
        if (current.x == end.x && current.y == end.y) {
            return distance;
        }
        
        // Probeer alle vier de richtingen
        for (auto [dx, dy] : {std::make_pair(1, 0), std::make_pair(-1, 0),
                              std::make_pair(0, 1), std::make_pair(0, -1)}) {
            int nx = current.x + dx, ny = current.y + dy;
            
            // Controleer of we binnen de grenzen zijn en niet bezocht
            if (nx >= 0 && nx < COLS && ny >= 0 && ny < ROWS && !visited[{nx, ny}] &&
                (Field[ny][nx] == '.' || Field[ny][nx] == 'S' || Field[ny][nx] == 'E')) {
                toVisit.push({nx, ny});
                visited[{nx, ny}] = true;
            }
        }
        ++distance;
    }
    return -1;  // Als er geen pad is
}
void Walk::buildTree() {
    std::vector<Point> crossings;
    
    // Identificeer de start en eindpunt, en kruisingen
    for (int y = 0; y < ROWS; ++y) {
        for (int x = 0; x < COLS; ++x) {
            if (Field[y][x] == 'S' || Field[y][x] == 'E' || 
                (Field[y][x] == '.' && (
                    (y > 0 && Field[y-1][x] == '.') || 
                    (y < ROWS-1 && Field[y+1][x] == '.') || 
                    (x > 0 && Field[y][x-1] == '.') || 
                    (x < COLS-1 && Field[y][x+1] == '.')
                ))) {
                crossings.push_back({x, y});
            }
        }
    }

    // Maak verbindingen tussen de kruisingen
    for (size_t i = 0; i < crossings.size(); ++i) {
        for (size_t j = i + 1; j < crossings.size(); ++j) {
            Point start = crossings[i];
            Point end = crossings[j];

            // Bereken de afstand tussen deze twee punten
            int distance = calculateDistance(start, end);
            if (distance != -1) {  // Als er een pad is
                Node* startNode = getNode(start.x, start.y);
                Node* endNode = getNode(end.x, end.y);
                startNode->neighbors.push_back({endNode, distance});
                endNode->neighbors.push_back({startNode, distance});
            }
        }
    }
}