#ifndef STACK_HPP
#define STACK_HPP

struct Node {
            int num;
            Node * next;
        };

// implementing a Stack in the heap memery (RAII: resourse aqusition is initialization)
// underlaying struct: singally linked list
// Note a common implementation of a stack is using a dynamic array such as a vector
class Stack {
    public:
        // ctor
        Stack();

        // add item
        void push(int num);

        // delete item
        void pop();

        // get first item

        int peek();

        // get size
        int getSize();

        // is empty
        bool isEmpty();

    private:
        int size;
        Node * first;
};

#endif