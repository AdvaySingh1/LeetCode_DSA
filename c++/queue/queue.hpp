#ifndef QUEUE_HPP
#define QUEUE_HPP


// implement a queue with a singally linked list (on heap)
struct Node {
    int num;
    Node * next;

};

class Queue {
    public:
        // ctor
        Queue();

        // getSize
        int getSize();

        // is empty
        bool is_empty();

        // enqueue
        void enqueue(int num);

        // dequeue
        void dequeue();

        //peek
        int peek();


    private:
        int size;
        Node * first;
        Node * last;



};

#endif