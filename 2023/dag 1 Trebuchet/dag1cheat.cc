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
void nummer(char ingevoerd, char &eerste, char &laatste){
    if(!(eerste <= '9' && eerste >= '0')){
        eerste = ingevoerd;
    }
    laatste = ingevoerd;
}




int krijg(ifstream&invoer){
    char ingevoerd;
    char eerste = 'x';
    char laatste = 'x';
    char hulp;

    while(invoer.get(ingevoerd)){
        if (ingevoerd <= '9' && ingevoerd >= '0'){
            if (eerste == 'x'){
                eerste = ingevoerd;
            }
            laatste = ingevoerd;
        } else {
            switch (ingevoerd) { 
                case 'o':
                    invoer.get(ingevoerd);
                    if(ingevoerd == 'n'){
                        ingevoerd = '1';
                    }
                    break;
                case 't':
                    invoer.get(ingevoerd);
                    if(ingevoerd == 'w' || ingevoerd == 'h'){
                        invoer.get(ingevoerd);
                        if(ingevoerd == 'o'){
                            ingevoerd = '2';
                        }
                        if(ingevoerd == 'r'){
                            invoer.get(ingevoerd);
                            if(ingevoerd == 'e'){
                                invoer.get(ingevoerd);
                                if(ingevoerd == 'e'){
                                    ingevoerd = '3';
                                }
                            }
                        }
                    }
                    break;
                // ... cases for 'f', 's', 'e', 'n'
                default:
                    break;
            }
            if (ingevoerd <= '9' && ingevoerd >= '0'){
                if (eerste == 'x'){
                    eerste = ingevoerd;
                }
                laatste = ingevoerd;
            }
        }
        if(ingevoerd == '\n'){
            if (eerste != 'x' && laatste != 'x'){
                cout << eerste << laatste << endl;
                return (eerste - '0') * 10 + (laatste - '0');
            } else if (eerste != 'x') {
                cout << eerste << endl;
                return eerste - '0';
            }
            return 0;
        }
    }
    return 0;
}


int main(){
    int som = 0;
    ifstream invoer;
    file(invoer);
    while(!invoer.eof()){
        // cout<<som<<endl;
        som = som + krijg(invoer);
    }
    cout<<som ;
}