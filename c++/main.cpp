#include <iostream>
#include "./heap/min_heap.hpp"
#include "./stack/stack.hpp"

using namespace std;

class UsageError  { // : public exception
    public:
    virtual const char * what() const { // allow inheritance
        return("Usage error");
    }
};

const void readUsage(int argc, char** argv) {
    if(argc != 4){
        throw UsageError();
    }
    string dsas[5] = {"stack", "queue", "min_heap"};
    string commands[5] = {"add", "remove"};

    bool isValidDsa = false;
    bool isValidCommand = false;
    

    for (auto elt: dsas){
        if(elt == argv[1]){
            isValidDsa = true;
        }
    }
    if (!isValidDsa){ throw UsageError();}

    for (auto elt: commands){
        if(elt == argv[2]){
            isValidCommand = true;
        }
    }
    if (!isValidCommand){ throw UsageError();}
}

int main(int argc, char** argv){
    cout.precision(3);
    try{
        // assure right arguments
        readUsage(argc, argv);

        // stack
        if (argv[1] == "stack"){
            Stack s;
            
        }



    } catch (const UsageError &e) {
        cout << e.what();
    }

    
    return 1;
}