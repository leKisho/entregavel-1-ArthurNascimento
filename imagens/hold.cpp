// so para segurar a pasta

#include <iostream>
#include <vector>

using namespace std;

int main(){

    vector<double*> numeres;

    while (true){
        // do nothing(?)
        numeres.push_back (new double[500000000]);
    }

    return 0;

}