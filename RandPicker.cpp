
// fast compile/run command: g++ RandPicker.cpp -o test; cp ./test ./lastTest; ./test test.table 6; rm ./test

#include <iostream>
#include <fstream>
#include <stdlib.h>     /* srand, rand, strtol */
#include <string.h>		/* strcmp */
#include <time.h>       /* time */

using namespace std;

int main(int argc, char* argv[]) {

	if (argc < 3) {
        std::cerr << "Usage: " << argv[0] << " TableAddress DiceRoll" << std::endl;
        std::cerr << "   OR: " << argv[0] << " TableAddress -r   #(prints a random entry)" << std::endl;
        std::cerr << "   OR: " << argv[0] << " TableAddress -s   #(prints size of table)" << std::endl;
        return 1;
    }


	ifstream file(argv[1]);
	string line;

  if (!file) {
      cout << "Invalid file." << endl;
      return 1;
  }

	int lineCount = 0;

    while (getline(file, line))
        lineCount++;
   	file.close();

   	if (strcmp(argv[2], "-s") == 0 || strcmp(argv[2], "s") == 0) {
	    cout << "Table contains " << lineCount << " option(s)" << endl;
	    return 0;
   	}
   	if (strcmp(argv[2], "-r") && ! isdigit(argv[2][0])) {
	    cout << "Invalid usage." << endl;
	    return 1;
   	}
   	//
	ifstream myReadFile;
	myReadFile.open(argv[1]);

	string entries[lineCount];
   	line = "";
	int i = 0;	
	while (getline(myReadFile, line))
	{
		entries[i] = line;
		i++;
	}
	myReadFile.close();

  if (! strcmp(argv[2], "-r")) {
    // srand (time(NULL));
    srand (clock());
    cout << entries[rand() % lineCount] << endl;
    return 0;
  }

  char * _;
  int diceRoll = strtol(argv[2], &_, 10);

  if (diceRoll < 1 || diceRoll > lineCount) {
  	cout << "Die value out of bounds, must be > 0 and <= " << lineCount << "." << endl;
  	return lineCount;
  }

  // for ( int i = 0; i < 500; i++) {
  // 	int i1 = rand() % lineCount;
  // 	int i2 = rand() % lineCount;
  // 	string temp = entries[i1];
  // 	entries[i1] = entries[i2];
  // 	entries[i2] = temp;
  // }

	cout << entries[diceRoll - 1] << endl;

	return 0;
}