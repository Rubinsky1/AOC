#include "Guard.h"

Guard::Guard(){

}

void Guard::readInputTo2DArray(const std::string& filename) {
    
    std::ifstream file(filename);  // Open het bestand voor lezen
    std::string line;
    int row = 0;

    // Lees het bestand regel voor regel
    while (std::getline(file, line) && row < ROWS) {
        for (size_t col = 0; col < line.size() && col < COLS; ++col) {
            Field[row][col] = line[col]; // Vul de array met karakters uit de input
            Copy[row][col] = line [col];
        }
        ++row;
    }

    // Sluit het bestand
    file.close();


}

void Guard::printField(){
    // Print de 2D array
    for (int i = 0; i < ROWS; ++i) {
        for (int j = 0; j < COLS; ++j) {
            std::cout << Field[i][j];
        }
        std::cout << std::endl;
    }
}

    // Beweeg de bewaker vooruit in de gegeven richting
    bool Guard::moveForward(int& x, int& y, char& dir) {
        int new_x = x, new_y = y;

        if (dir == '^') new_x--;
        else if (dir == '>') new_y++;
        else if (dir == 'v') new_x++;
        else if (dir == '<') new_y--;

        // Controleer of de nieuwe positie binnen de grenzen ligt
        if (new_x < 0 || new_y < 0 || new_x >= ROWS || new_y >= COLS) {
            if (Field[x][y] != 'X') {
                Field[x][y] = 'X';  // Markeer als bezocht
                visited_count++;
            }
            return false;  // Bewaker is buiten het bord
        }

        // Verplaats de bewaker
    
        return true;
    }

    char Guard::turnRight(char dir) {
        if (dir == '^') return '>';
        if (dir == '>') return 'v';
        if (dir == 'v') return '<';
        if (dir == '<') return '^';
        return dir;  // Fout, maar voorkomt een crash bij foutieve input
    }

    bool Guard::findStartPosition(int& x, int& y, char& dir) {
        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                if (Field[i][j] == '^' || Field[i][j] == '>' || Field[i][j] == 'v' || Field[i][j] == '<') {
                    x = i;
                    y = j;
                    dir = Field[i][j];  // Zet de richting
                    Field[i][j] = '.';  // Zet de startpositie op een leeg veld
                    return true;
                }
            }
        }
        return false;
    }

bool Guard::startPatrol() {
    visited_positions.clear();

    int x, y; // Huidige positie van de bewaker
    char dir; // Huidige richting van de bewaker

    // Vind de startpositie van de bewaker (gemarkeerd met ^)
    findStartPosition(x, y, dir);
    
    bool is_out_of_bounds = false;
    while (!is_out_of_bounds) {
        //std::cout<<dir<<"\n";
        if (isInLoop(x, y, dir)) {
        
            return false;  // Stop de patrouille bij een loop
        }
        // Markeer de huidige positie als bezocht
        if (Field[x][y] != 'X') {
            Field[x][y] = 'X';  // Markeer als bezocht
            visited_count++;
        }

        // Maak tijdelijke variabelen voor de nieuwe x en y posities
        int new_x = x, new_y = y;

        // Controleer de richting en voer de regels uit
        if (dir == '^') {
            if(Field[x-1][y]=='#'){
                dir = turnRight(dir);
            }
            else new_x = x - 1;
            
        } else if (dir == '>') {
            if(Field[x][y+1]=='#'){
                dir = turnRight(dir);
            }
            else new_y = y + 1;
            
        } else if (dir == 'v') {
            if(Field[x+1][y]=='#'){
                dir = turnRight(dir);
            }
            else new_x = x + 1;
            
        } else if (dir == '<') {
            if(Field[x][y-1]=='#'){
                dir = turnRight(dir);
            }
            else new_y = y - 1;
            
        }
        // Verplaats de bewaker
        if (!moveForward(new_x, new_y, dir)) {
            break;
        }
        // Werk de huidige x en y bij
        x = new_x;
        y = new_y;

    }
    return true;
}

    bool Guard::isInLoop(int x, int y, char dir) {
        std::tuple<int, int, char> current_state = {x, y, dir};
        
        // Controleer of deze positie en richting al bezocht zijn
        if (visited_positions.find(current_state) != visited_positions.end()) {
            return true;  // Loop gedetecteerd
        }
        
        // Voeg de huidige positie en richting toe aan de set van bezochte posities
        visited_positions.insert(current_state);
       
        return false;  // Geen loop
    }

int Guard::testloops(){
    int loop_count = 0;
    for (int i = 0; i < ROWS; ++i) {
        for (int j = 0; j < COLS; ++j) {
            reset();
            if(Field[i][j] != '#' && Field[i][j] != '^'&& Field[i][j] != 'v'&& Field[i][j] != '<'&& Field[i][j] != '>' ){
                char original = Field[i][j];
                Field[i][j] = '#';
                if (!startPatrol()) loop_count++;
                Field[i][j] = original;  // Herstel het veld
            }
            
        }
     
    }
    return loop_count;
}

void Guard::reset(){
    for (int i = 0; i < ROWS; ++i) {
        for (int j = 0; j < COLS; ++j) {
            Field[i][j] = Copy[i][j];
        }
    }
}