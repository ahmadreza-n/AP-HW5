CXX = g++
CXXFLAGS = -std=c++17 -Wall -c
LXXFLAGS = -std=c++17
OBJECTS = main.o gaussSolver.o
TARGET = main


$(TARGET): $(OBJECTS)
	$(CXX) $(LXXFLAGS) $(OBJECTS) -o $(TARGET)
main.o: main.cpp
	$(CXX) $(CXXFLAGS) main.cpp
gaussSolver.o: gaussSolver.h gaussSolver.cpp
	$(CXX) $(CXXFLAGS) gaussSolver.cpp
clean:
	rm -f $(TARGET) $(OBJECTS)
