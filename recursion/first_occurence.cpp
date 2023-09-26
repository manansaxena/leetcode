#include <iostream>
#include <vector>

using namespace std; 

int first_occurence(int arr[], int n, int find){
    if(n == 0){
        return -1;
    }
    if(arr[0] == find){
        return 0;
    }
    int subIndex = first_occurence(arr+1,n-1,find);
    if(subIndex == -1){
        return -1;
    }
    else {
        return subIndex+1;
    }
}


int main(){
    int abc[] = {1,2,3,2,4};

    cout << first_occurence(abc, sizeof(abc)/sizeof(int), 3) << endl;
    return 0;
}