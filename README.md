# RollTables
Basic DnD roll table program. Includes GUI and collection of tables, written loosely for DnD 5e.

Compilation:
Windows:
	RandPicker.exe compiled via mingw:
	g++ RandPicker.cpp -o pickRandom.exe -static-libgcc -static-libstdc++
linux:
	g++ RandPicker.cpp -o pickRandom 

Run the main program via:
linux:
	python3 RollTableGUI.py
windows:
	python RollTableGUI.py