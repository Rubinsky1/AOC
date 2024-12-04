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
    char eerste;
    char laatste;
    char hulp;
    bool run = true;
    invoer.get(ingevoerd);
    while(run){

        if(ingevoerd <= '9' && ingevoerd >= '0'){

            nummer(ingevoerd, eerste, laatste);
            invoer.get(ingevoerd);
        }
        else if(ingevoerd == '\n'){
            run = false;
            hulp = eerste;
            eerste = 'x';
            cout<<hulp<<laatste<<endl;
            if(hulp == 'x')return 0;
            else return(hulp - '0')*10 + (laatste - '0');
            
            
        }
        
        else{

            switch (ingevoerd) { 
            case 'o':
                invoer.get(ingevoerd);
                if(ingevoerd == 'n'){
                    invoer.get(ingevoerd);
                    if(ingevoerd == 'e'){
                        nummer('1', eerste, laatste);   
                    }
                    
                    if(ingevoerd == 'i'){
                        invoer.get(ingevoerd);
                        if(ingevoerd == 'n'){
                            invoer.get(ingevoerd);
                            if(ingevoerd == 'e'){
                                nummer('1', eerste, laatste);
                            }
                        }
                    }
                }
                break;
            case 't':
                invoer.get(ingevoerd);
                if(ingevoerd == 'w' || ingevoerd == 'h'){
                    invoer.get(ingevoerd);
                    if(ingevoerd == 'o'){
                        nummer('2', eerste, laatste);
                    }
                    if(ingevoerd == 'r'){
                        invoer.get(ingevoerd);
                        if(ingevoerd == 'e'){
                            invoer.get(ingevoerd);
                            if(ingevoerd == 'e'){
                                nummer('3', eerste, laatste);
                            }
                        }
                    }
                }
                break;
            case 'f':
                invoer.get(ingevoerd);
                if(ingevoerd == 'o' || ingevoerd == 'i'){
                    invoer.get(ingevoerd);
                    if(ingevoerd == 'u' || ingevoerd == 'v'){
                        invoer.get(ingevoerd);
                        if(ingevoerd == 'r'){
                            nummer('4', eerste, laatste);
                        }
                        else if(ingevoerd == 'e'){
                            nummer('5', eerste, laatste);
                        }
                    }
                }
                break;
            case 's':
                invoer.get(ingevoerd);
                if(ingevoerd == 'i' || ingevoerd == 'e'){
                        invoer.get(ingevoerd);
                        if(ingevoerd == 'x'){
                            nummer('6', eerste, laatste);
                        }
                        else if(ingevoerd == 'v'){
                            invoer.get(ingevoerd);
                            if(ingevoerd == 'e'){
                                invoer.get(ingevoerd);
                                if(ingevoerd == 'n'){
                                    nummer('7', eerste, laatste);
                                }
                            }
                        }
                }
                break;
            case 'e':
                invoer.get(ingevoerd);
                if(ingevoerd == 'i'){
                    invoer.get(ingevoerd);
                    if(ingevoerd == 'g'){
                        invoer.get(ingevoerd);
                        if(ingevoerd == 'h'){
                            invoer.get(ingevoerd);
                            if(ingevoerd == 't'){
                                nummer('8', eerste, laatste);
                            }
                        }
                    }
                }
                break;
            case 'n': 
                invoer.get(ingevoerd);
                if(ingevoerd == 'i'){
                    invoer.get(ingevoerd);
                    if(ingevoerd == 'n'){
                        invoer.get(ingevoerd);
                        if(ingevoerd == 'e'){
                            nummer('9', eerste, laatste);
                        }
                    }
                }
                break;
            default:
                invoer.get(ingevoerd);
            } 
        }
    }
}

int main(){
    int som = 0;
    ifstream invoer;
    file(invoer);
    while(!invoer.eof()){
        // cout<<som<<endl;
        som = som + krijg(invoer);
        cout<<som<<endl;
    }
    cout<<som ;
}