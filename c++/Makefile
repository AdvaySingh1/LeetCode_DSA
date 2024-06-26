# set verbosity
VB ?= 0

ifeq ($(VB),1)
  V =
else
  V = @
endif

# Compiler
CXX = g++

# Compiler flags
CXXFLAGS = -Wall -std=c++17 -pedantic

# set the sources
SOURCES = main.cpp heap/min_heap.cpp stack/stack.cpp

# compile into object files
OBJECTS = $(SOURCES:.cpp=.o)

# det the dependencies
DEPS = $(OBJECTS:.o=.d)

# set default target
all: main.exe

# Link files
main.exe: $(OBJECTS)
	$(V)$(CXX) $(CXXFLAGS) -o $@ $(OBJECTS)


# stack
stack.exe: stack/stack.cpp stack/stack.hpp
	$(V)$(CXX) $(CXXFLAGS) $< -o $@ -include stack/stack.hpp

# queue
queue.exe: queue/queue.cpp queue/queue.hpp
	$(V)$(CXX) $(CXXFLAGS) $< -o $@ -include queue/queue.hpp

# heap
heap.exe: heap/min_heap.cpp heap/min_heap.hpp
	$(V)$(CXX) $(CXXFLAGS) $< -o $@ -include heap/min_heap.hpp

# tree


# graph



# rule for compilation
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@


# include all deps
-include $(DEPS)


# clear the .exe executable, object, and output text files
clean: 
	$(V)rm -vrf *.o *.exe *.out.txt

# targets not creating any files
.PHONY: clean all


