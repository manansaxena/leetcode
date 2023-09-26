#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool isSubsequence(string bigger, string smaller){
    for(int i=0;i<smaller.length();i++){
        int index = bigger.find(smaller[i]);
        if(index == -1){
            return false;
        }
        bigger = bigger.substr(index+1);
    }
    return true;
}


int main(){
    string bigger = "codingminutes";
    string smaller = "cdines";
    bool result = isSubsequence(bigger,smaller);
    cout << result << endl;

    return 0;
}