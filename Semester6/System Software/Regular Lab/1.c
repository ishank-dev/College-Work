//Program to create,write and delete a file

#include <iostream>
#include <fstream>
using namespace std;

int main() {
  // Create and open a text file
  ofstream MyFile("file1.txt");

  // Write to the file
  MyFile << "This is my file. Welcome to OOADP lab";

  // Close the file
  MyFile.close();
}




