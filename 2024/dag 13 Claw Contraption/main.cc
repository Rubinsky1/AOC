#include "claw.h"



int main() {
    Claw C;
    C.loadData(std::cin);
    std::cout<<"Opdracht1: "<<C.cheapestit(false)<<std::endl;
    std::cout<<"Opdracht2: "<<C.cheapestit(true)<<std::endl;
    return 0;
}