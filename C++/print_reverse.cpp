#include <iostream>
using namespace std;

void printReverse(const char *str) {
  if (!*str)
    return;
  printReverse(str + 1);
  cout << *str << " "; // print the first char in str
}

int main(){
    printReverse("helloworld");
//    const char *str = "helloworld";
//    cout << *str << endl;
}
