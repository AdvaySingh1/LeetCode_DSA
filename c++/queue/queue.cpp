#include "queue.hpp"
#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    Queue q;
    string op = "";
    int num = 0;
    while (op != "exit")
    {
        cin >> op;
        if (op == "enqueue")
        {
            cin >> num;
            q.enqueue(num);
        }
        else if (op == "dequeue")
        {
            q.dequeue();
        }
    }
    // TODO: add a delete all function to delete the remining entries upon exiting.
}

// ctor
Queue::Queue() : size(0), first(nullptr), last(nullptr) {}
// get size
int Queue::getSize()
{
    return this->size;
}

// is empty
bool Queue::is_empty()
{
    return this->size == 0;
}

// peek
int Queue::peek()
{
    if (this->is_empty()) // TODO check if exception for dereferencing a nullptr;
    {
        return -1;
    }
    return this->first->num;
}

// enqueue
void Queue::enqueue(int num)
{
    Node *newNode = new Node;
    newNode->num = num;
    newNode->next = nullptr;
    if (this->is_empty())
    {
        first = last = newNode; // check
    }
    else
    {
        last->next = newNode;
        last = newNode;
    }

    size++;

    cout << "Added " << num << ". Size: " << this->getSize() << endl;
}

// dequeue
void Queue::dequeue()
{
    if (this->is_empty())
    {
        cout << "You can't dequeue and empty queue" << endl;
    }
    else
    {
        Node *toDel = first;
        int num = toDel->num;
        if (first == last)
        {
            first = nullptr;
            last = nullptr;
        }
        else
        {
            first = first->next;
        }
        delete toDel;
        size--;

        cout << "Deleted " << num << ". Size: " << this->getSize() << endl;
        ;
    }
}
