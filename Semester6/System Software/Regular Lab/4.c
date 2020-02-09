#include <iostream>
#include <fstream>
using namespace std;

int main() {
  string fname;

  cout<<"Enter the fname";
  cin>>fname;
  
  ifstream MyReadFile(fname.c_str());

  if(MyReadFile== NULL)
  cout<<"Not present";
  else
  cout<<"Present";

  // Close the file
  MyReadFile.close();
}
