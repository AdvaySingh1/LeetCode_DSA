#include "stack.hpp"
#include "iostream"

using namespace std;


int main(int argc, char** argv){
    Stack s;
    string op = "";
    int num = 0;
    while (op != "exit"){
        cin >> op;
        
        // add a number
        if (op == "push"){
            cin >> num;
            s.push(num);
        }
        else if(op == "pop"){
            s.pop();
        }
    }
}

// ctor with initializer list
Stack::Stack() :
    size(0), first(nullptr)
{}

void Stack::push(int num){
    Node * curr = new Node;
    curr->num = num;
    if (this->isEmpty()){
        curr->next = nullptr;
    } else{
        curr->next = this->first;
    }
    this->first = curr;

    size++;

    cout << "Pushed " << this->peek() << ". The size is " << this->getSize() << endl;
}

void Stack::pop(){
    if(this->isEmpty()){return;}
    
    cout << "Popped " << this->first->num;
    if(this->getSize() == 1){
        delete first;
        first = nullptr; // for nullptr
        size--;
        cout << ". The size is " << this->getSize() << endl; // should be 0
        return;
    }

    Node * curr = this->first;
    this->first = this->first->next;
    delete curr;

    size--;

    cout << ". The new peek is: " << this->peek() << ". The size is " << this->getSize() << endl;
}


int Stack::peek(){
    return this->first->num;

}

int Stack::getSize(){
    return Stack::size;
}

bool Stack::isEmpty(){
    return (this->getSize() == 0);
}



class UsageError  { // : public exception
    public:
    virtual const char * what() const { // allow inheritance
        return("Usage error");
    }
};

