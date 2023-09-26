#include <iostream>
#include <string>

using namespace std;

int main(){
    // string s;
    // getline(cin,s,'.');
    // for(char c:s){
    //     cout << c << " ,";
    // }
    // cout << endl << s << endl;

    string paragraph = "Hello World you young fella!";
    string word;
    getline(cin, word);

    int index = paragraph.find(word); // converting an unsigned long to integer. So it would be -1 if the string is not found
    if(index != -1){
        cout << index << endl;
    }
    else if(index == -1){
        cout << "String not found" << endl;
    }

    return 0;
}