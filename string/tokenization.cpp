#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <cstring>

using namespace std;

vector<string> tokenize(string s){
    stringstream ss(s);
    string token;
    vector<string> tokens;
    while(getline(ss,token,' ')){
        tokens.push_back(token);
    }
    return tokens;
}

vector<string> tokenize_2(string str){
    vector<string> tokens;
    char *s = strtok((char*)str.c_str()," ");
    while(s!=NULL){
        tokens.push_back(string(s));
        s = strtok(NULL, " ");
    }
    return tokens;
}

int main(){
    string s = "Hello world !!";
    vector<string> tokens = tokenize_2(s);
    for(auto token:tokens){
        cout << token << endl;;
    }
    return 0;
}