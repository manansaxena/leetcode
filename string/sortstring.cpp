#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <utility>

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

bool sortbysecNum(pair<string,int> &a, pair<string,int> &b){
    return (a.second < b.second);
}

bool sortbysecLex(pair<string,string> &a, pair<string,string> &b){
    return (a.second < b.second);
}

vector<string> sortString(vector<string> &strings, int key, bool reversed, string comparison_type){
    vector<vector<string>> tokenizedString;
    for(int i=0;i<strings.size();i++){
        tokenizedString.push_back(tokenize(strings[i]));
    }
    vector<string> sorted;
    if(comparison_type == "numerical"){
        vector<pair<string,int>> paired_strings;
        for(int i=0;i<tokenizedString.size();i++){
            pair<string, int> p1(strings[i],stoi(tokenizedString[i][key]));
            paired_strings.push_back(p1);
        }
        sort(paired_strings.begin(),paired_strings.end(),sortbysecNum);
        for(int i=0;i<paired_strings.size();i++){
            sorted.push_back(paired_strings[i].first);
        }
    }
    else if(comparison_type == "lexi"){
        vector<pair<string,string>> paired_strings;
        for(int i=0;i<tokenizedString.size();i++){
            pair<string, string> p1(strings[i],tokenizedString[i][key]);
            paired_strings.push_back(p1);
        }
        sort(paired_strings.begin(),paired_strings.end(),sortbysecLex);
        for(int i=0;i<paired_strings.size();i++){
            sorted.push_back(paired_strings[i].first);
        }
    }

    if(reversed){
        reverse(sorted.begin(),sorted.end());
    }
    
    return sorted;
}


int main(){
    
    vector<string> strings = {
        "22 111 121",
        "22 41 2",
        "12 21 11"
    };

    vector<string> sorted_strings = sortString(strings,2, true,"numerical");
    for(auto s:sorted_strings){
        cout << s << endl;
    }
    return 0;
}