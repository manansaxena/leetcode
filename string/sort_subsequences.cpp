#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

void getSubsequence(string s, vector<string> &result){
    if(s == ""){
        result.push_back(s);
        return;
    }
    getSubsequence(s.substr(1),result);
    int size = result.size();
    for(int i=0;i<size;i++){
        result.push_back(s[0]+result[i]);
    }
}

bool sortByLength(string s1, string s2){
    if(s1.length() != s2.length()){
        return s1.length()<s2.length();
    }
    else{
        return s1 < s2;
    }
}

vector<string> sortSubsequence(string s){
    vector<string> result;
    getSubsequence(s, result);
    sort(result.begin(),result.end(),sortByLength);
    return result;
}


int main(){

    vector<string> result = sortSubsequence("abcd");
    for(auto s:result){
        cout << s << endl;
    }

    return 0;
}