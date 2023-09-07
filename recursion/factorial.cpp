#include <iostream>

using namespace std; 

int factorial(int n){
    if(n == 0){
        return 1;
    }
    int prev_fact = factorial(n-1);
    return n * prev_fact;
}

int main(){
    cout << factorial(5) << endl;
    return 0;
}