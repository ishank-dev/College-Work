#include<iostream>
#include<fstream>
using namespace std;

int main(){
    string data,text;

    ofstream outfile("afile.dat",ios::app);

    cout<<"Enter your name"<<endl;
    cin>>data;

    outfile<<data;

    outfile.close();

    cout<<"Reading file"<<endl;

    ifstream infile("afile.dat");

  while(getline(infile,text))
    cout<<text<<" ";

    infile.close();

    return 0;
}