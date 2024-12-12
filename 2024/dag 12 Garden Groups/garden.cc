#include "garden.h"
#include <vector>
#include <string>
#include <fstream>
#include <iostream>

void Garden::readInputTo2DArray(const std::string& filename) {
    std::ifstream file(filename); // Open het bestand
    if (!file.is_open()) {
        std::cerr << "Kan bestand niet openen: " << filename << std::endl;
        return;
    }

    std::string line;
    Width = 0;
    Height = 0;
    while (std::getline(file, line)) {
        if (Width == 0) {
            Width = line.size();
        }
        std::vector<char> row(line.begin()-1, line.end()); 
        //row.erase(row.begin());
        Field.push_back(row); 
        Height++;
    }
    file.close(); // Sluit het bestand
}

void Garden::printField() {
    for (size_t i = 0; i<Field.size(); i++) { 
        for (size_t j = 0; j<Field[i].size(); j++) { 
          
          if(Field[i][j]) std::cout << Field[i][j] << " "; 
        }
        std::cout << std::endl; 
    }
}

int Garden::zoekgroep1(int row, int col, std::vector<std::vector<bool>>& bezocht, int& grootte, char k) {
    int totaal = 0;
    if (row < 0 || row >= Height || col < 0 || col >= Width || Field[row][col] != k) {//checkt of de huidige positie toegevoegd moet worden of niet
        //zo niet dan wordt de functie afgekapt
        return 1;//tel 1 rij ernaast dus hekje
    }
    if(bezocht[row][col])return  0;
    grootte++;//zet de grootte 1 omhoog omdat de groep uit  meer bestaat
    bezocht[row][col] = true;//zet de positie naar bezocht
    totaal += zoekgroep1(row + 1, col,  bezocht, grootte, k);//checkt 1 kolom naar rechts recursief
    totaal += zoekgroep1(row - 1, col,  bezocht, grootte, k);//checkt 1 kolom naar links recursief
    totaal += zoekgroep1(row, col + 1,  bezocht, grootte, k);//checkt 1 kolom naar boven recursief
    totaal += zoekgroep1(row, col - 1,  bezocht, grootte, k);//checkt 1 kolom naar onder recursief
    return totaal;
}//zoekNullen
int Garden::zoekgroep2(int row, int col, std::vector<std::vector<bool>>& bezocht, int& grootte, char k) {
    int totaal = 0;
    if (row < 0 || row >= Height || col < 0 || col >= Width || Field[row][col] != k) {//checkt of de huidige positie toegevoegd moet worden of niet
        //zo niet dan wordt de functie afgekapt
        return 0;
    }
    if(bezocht[row][col])return  0;
    grootte++;//zet de grootte 1 omhoog omdat de groep uit  meer bestaat
    bezocht[row][col] = true;//zet de positie naar bezocht

        int hoeken = 0;
    // Controleer de vier mogelijke hoeken
    // Controleer voor een binnenhoek (beide cellen zijn 'b')
    if (row + 1 < Height && col + 1 < Width && Field[row+1][col] == k && Field[row][col+1] == k && Field[row+1][col+1] != k) hoeken++; // Onder + Rechts
    if (row + 1 < Height && col - 1 >= 0 && Field[row+1][col] == k && Field[row][col-1] == k && Field[row+1][col-1] != k) hoeken++; // Onder + Links
    if (row - 1 >= 0 && col + 1 < Width && Field[row-1][col] == k && Field[row][col+1] == k&& Field[row-1][col+1] != k) hoeken++; // Boven + Rechts
    if (row - 1 >= 0 && col - 1 >= 0 && Field[row-1][col] == k && Field[row][col-1] == k&& Field[row-1][col-1] != k) hoeken++; // Boven + Links

    // Controleer voor een buitenhoek (een van de cellen is rand of ander karakter)
    if ( (row+1 == Height||Field[row+1][col] != k ) && (col+1 == Width||Field[row][col+1] != k  )) hoeken++; // Onder + Rechts
    if ((row+1 == Height||Field[row+1][col] != k) && ( col-1 < 0||Field[row][col-1] != k )) hoeken++; // Onder + Links
    if ( (row-1 <0||Field[row-1][col] != k) && (col+1 == Width||Field[row][col+1] != k )) hoeken++; // Boven + Rechts
    if ( (row-1 <0||Field[row-1][col] != k) && ( col-1 < 0||Field[row][col-1] != k )) hoeken++; // Boven + Links



    totaal += hoeken; // Voeg de hoeken toe aan het totaal
    totaal += zoekgroep2(row + 1, col,  bezocht, grootte, k);//checkt 1 kolom naar rechts recursief
    totaal += zoekgroep2(row - 1, col,  bezocht, grootte, k);//checkt 1 kolom naar links recursief
    totaal += zoekgroep2(row, col + 1,  bezocht, grootte, k);//checkt 1 kolom naar boven recursief
    totaal += zoekgroep2(row, col - 1,  bezocht, grootte, k);//checkt 1 kolom naar onder recursief
    return totaal;
}//zoekNullen

int Garden::groepGrote(bool opdracht) {
  std::vector<std::vector<bool>> kopie(Height, std::vector<bool>(Width, false));
  int grote = 0;
  int som = 0;
  for(int i = 0; i<Height; i++){
    for(int j = 0; j<Width ; j++){
      if(!kopie[i][j]){//als er een 0 op de huidige positie staat en de positie nog niet bezocht is
        grote = 0;
        char k = Field[i][j];
        int hekjes = 0;
        if(opdracht){if(k != '\0')hekjes = zoekgroep2(i, j, kopie, grote, k);}//roep de functie aan om de grote van de huidige groep te bepalen
        else if(k != '\0')hekjes = zoekgroep1(i, j, kopie, grote, k);
        if(k != '\0')som+= hekjes*grote;

        grote = 0;//terugzetten
      }//if
    }//for j
  }//for i
  return som;//stuurt de kleinste terug
}//groepGrote
