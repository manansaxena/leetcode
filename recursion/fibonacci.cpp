#include <iostream>

using namespace std; 

int fibonacci(int n){
    if(n == 0){
        return 0;
    }
    if(n == 1){
        return 1;
    }
    int curr_fib = fibonacci(n-1)+fibonacci(n-2);
    return curr_fib;
}

int main(){
    cout << fibonacci(6) << endl;
    return 0;
}