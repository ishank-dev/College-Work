#include<iostream>
#include<fstream>
using namespace std;

int main(){
    string data,text;
    string fname;

    cout<<"Enter the fname";
    cin>>fname;
    ofstream outfile(fname.c_str());

    cout<<"Enter your name"<<endl;
    cin>>data;

    outfile<<data;

    outfile.close();

    cout<<"Reading file"<<endl;

    ifstream infile(fname.c_str());

  while(getline(infile,text))
    cout<<text<<" ";

    infile.close();

    return 0;
}