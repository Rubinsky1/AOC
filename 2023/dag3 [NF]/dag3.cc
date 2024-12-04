#include <fstream>
#include <iostream>
#include <string>
#include <climits>

using namespace std;
const int Max = 140;


class uitlezen{
    private:
    char bestand[Max][Max];
    ifstream invoer;

    public:
    uitlezen();
    void krijg();
    void file();
    void check_buren();
};

void uitlezen::file(){
    string filenaam;
    cout<<"vul hier in welke file u wilt coderen of decoderen"<<endl;
    cin>>filenaam;
    invoer.open(filenaam.c_str());

}//file

void uitlezen::krijg(){
    char ingevoerd;
    for(int j = 140; j<140; j++){
        for(int i = 0; i < 140; i++){
            invoer.get(ingevoerd);
            bestand[i][j] = ingevoerd;
            //cout<<ingevoerd;
        }
    }
}

void uitlezen::check_buren(){
    for(int j = 140; j<140; j++){
        for(int i = 0; i < 140; i++){
            
        }
    }
}

uitlezen::uitlezen(){
    file();
}

int main(){
    uitlezen bestand;
    bestand.krijg();
}