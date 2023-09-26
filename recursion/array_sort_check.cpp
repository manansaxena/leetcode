#include <iostream>
#include <vector>

using namespace std; 

bool check_sorted(int arr[], int n){
    if(n == 1){
        return true;
    }

    bool rest_array = check_sorted(arr+1,n-1);
    if(rest_array == true && arr[0] <= arr[1]){
        return true;
    }
    else{
        return false;
    }
}


int main(){
    int abc[] = {1,2,3,4};

    cout << check_sorted(abc, sizeof(abc)/sizeof(int)) << endl;
    return 0;
}