#include <iostream>
#include <string>
#include <vector>

using namespace std;

// s.resize(), s.find(), s.length()

vector<int> findAllOccurances(string big, string small){
    int index = 0;
    vector<int> results;
    while(index != -1){
        index = big.find(small,index);
        if(index == -1){
            continue;
        }
        results.push_back(index);
        index += 1;
    }
    return results;
}

void space20(string &s){
    vector<int> all_spaces = findAllOccurances(s," ");
    int num_spaces = all_spaces.size();
    int extra_space = num_spaces*2;
    int length_original = s.length();

    s.resize(length_original+extra_space,' ');
    int last_index = s.length()-1;
    for(int i=length_original-1;i>=0;i--){
        if(s[i]!=' '){
            s[last_index] = s[i];
            last_index -= 1;
        }
        if(s[i] == ' '){
            s[last_index--] = '0';
            s[last_index--] = '2';
            s[last_index] = ' ';
            last_index -=1;
        }
    }
}


int main(){

    string s = "Hello World!! How is it?";
    space20(s);
    cout << s << endl;
    return 0;
}