#include <fstream>
#include <iostream>
#include <string>
#include <climits>

using namespace std;

void file(ifstream & invoer){
    string filenaam;
    cout<<"vul hier in welke file u wilt coderen of decoderen"<<endl;
    cin>>filenaam;
    invoer.open(filenaam.c_str());

}//file



int krijg(ifstream&invoer){
    char ingevoerd;
    int game = 0;
    int aantal = 0;
    int g = 0;
    int b = 0;
    int r = 0;
    for(int i = 0; i < 5; i++){
        invoer.get(ingevoerd);
        //cout<<ingevoerd;
    }
    while(ingevoerd != ':'){
        invoer.get(ingevoerd);
        //cout<<ingevoerd;
        if(!(ingevoerd<'0' || ingevoerd > '9')){
            game = game * 10 + (ingevoerd - '0');
            
        }
    }
    cout<<game;
    cout<<ingevoerd;
    while(ingevoerd != '\n'&&!invoer.eof()){
        invoer.get(ingevoerd);
        if(!(ingevoerd<'0' || ingevoerd > '9')){
            aantal = aantal * 10 + (ingevoerd - '0');
        }
        if(ingevoerd == 'g'){
            if(aantal>g)g = aantal;
            for(int i = 0; i < 4; i++){
                invoer.get(ingevoerd);
            }
            aantal = 0;
        }
        if(ingevoerd == 'r'){
            if(aantal>r)r = aantal;
            for(int i = 0; i < 2; i++){
                invoer.get(ingevoerd);
            }
            aantal = 0;
        }
        
        if(ingevoerd == 'b'){
            if(aantal>b)b = aantal;
            for(int i = 0; i < 3; i++){
                invoer.get(ingevoerd);
            }
            aantal = 0;
        }
        
    }

    return b*g*r;

}

int main(){
    int aantal = 0;
    ifstream invoer;
    file(invoer);
    while(!invoer.eof()){
        aantal = aantal + krijg(invoer);
        cout<<aantal<<endl;
    }
    invoer.close ( );
}