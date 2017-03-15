/**
fast compile/run command:
  g++ RandPicker.cpp -o pickRandom; cp ./pickRandom ./lastTest; ./pickRandom pickRandom.table 6; rm ./pickRandom
cross-compile command:
  x86_64-w64-mingw32-g++ -Wall -g -std=c++0x -static-libgcc -static -lpthread -o pickRandom.exe RandPicker.cpp
**/

#include <iostream>
#include <fstream>
#include <stdlib.h>     /* srand, rand, strtol */
#include <string.h>		/* strcmp */
#include <time.h>       /* time */
#include <sys/time.h>

using namespace std;

/**
 * From http://stackoverflow.com/questions/322938/recommended-way-to-initialize-srand
 */
// unsigned long mix(unsigned long a, unsigned long b, unsigned long c)
// {
//     a=a-b;  a=a-c;  a=a^(c >> 13);
//     b=b-c;  b=b-a;  b=b^(a << 8);
//     c=c-a;  c=c-b;  c=c^(b >> 13);
//     a=a-b;  a=a-c;  a=a^(c >> 12);
//     b=b-c;  b=b-a;  b=b^(a << 16);
//     c=c-a;  c=c-b;  c=c^(b >> 5);
//     a=a-b;  a=a-c;  a=a^(c >> 3);
//     b=b-c;  b=b-a;  b=b^(a << 10);
//     c=c-a;  c=c-b;  c=c^(b >> 15);
//     return c;
// }

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
    struct timeval t1;
    gettimeofday(&t1, NULL);
    srand(t1.tv_usec);
    //    Code used in finding a suitable method of seeding rand(), 
    //    given that the program could be called multiple times a second.
    // int init = rand();
    // unsigned long seed = mix(clock(), time(NULL), rand());
    // long count[lineCount];
    // for (int i = 0; i < lineCount; i++) {
    //   count[i] = 0;
    // }
    // for (int i = 0; i < 100000; i++) {
    //   // srand (mix(clock(), time(NULL), init));
    //   // cout << t1.tv_usec << "\n";
    //   gettimeofday(&t1, NULL);
    //   srand(t1.tv_usec);
    //   count[rand() % lineCount]++;
    // }
    // for (int i = 0; i < lineCount; i++) {
    //   cout << count[i] << ",";
    // }
    // cout << (int)argv[1][0] << " " << entries[rand() % lineCount] << endl;
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
