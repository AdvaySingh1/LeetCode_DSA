#include <iostream>
#include "min_heap.hpp"
using namespace std;

int main(int argc, char **argv)
{
    Heap h;
    string op = "";
    int num = 0;
    while (op != "exit")
    {
        cin >> op;
        // insert
        if (op == "insert")
        {
            cin >> num;
            h.insert(num);
        }

        else if (op == "del_min")
        {
            h.del_min();
        }
    }
}

// heap functions
Heap::Heap()
    : size(0), capacity(1)
{
    this->arr = new int[capacity];
}

Heap::~Heap()
{
    delete[] this->arr;
}

int Heap::extract_min()
{
    if (this->size == 0)
    {
        return -1; // TODO add exception
    }
    return this->arr[0];
}

int Heap::getSize()
{
    return this->size;
}

void Heap::insert(int num)
{
    // covered width
    if (capacity == this->getSize())
    {
        capacity *= 2;
        int *arr2 = new int[capacity];

        // copy the values
        for (int i = 0; i < this->getSize(); i++)
        {
            arr2[i] = this->arr[i];
        }
        delete[] this->arr;
        this->arr = arr2;
    }

    // add val and increment size
    this->arr[this->getSize()] = num;

    this->size++;

    // heapify up
    this->heapifyUp();

    cout << "Inserted " << num << ". Min element: " << this->extract_min()
         << ". Size: " << this->getSize() << endl;
}

void Heap::del_min()
{
    if (this->getSize() == 0)
    {
        cout << "Can't delete min from an empty heap" << endl;
        return;
    }
    cout << "Deleted " << this->extract_min(); // TODO replace with function call

    // swap first and last and decrement size
    this->swap(0, this->getSize() - 1);
    this->size--;

    // heapify down
    this->heapifyDown();

    cout << ". Min element: " << this->extract_min() << ". Size: " << this->getSize() << endl;
}

void Heap::heapifyDown()
{
    int index = 0;

    while (index * 2 + 2 < size) // check if right amount here
    {
        // while smaller childnode
        while (this->arr[index] > this->arr[index * 2 + 1] ||
               this->arr[index] > this->arr[index * 2 + 2])
        {

            // if left child node is smaller
            if (this->arr[index * 2 + 1] <= this->arr[index * 2 + 2])
            {
                this->swap(index, index * 2 + 1);
                index = index * 2 + 1;
            }

            // if right child node is smaller
            else
            {
                this->swap(index, index * 2 + 2);
                index = index * 2 + 2;
            }
        }
        index++;
    }

    if (index * 2 + 1 < size && this->arr[index] > this->arr[index * 2 + 1])
    {
        cout << "swapping " << this->arr[index * 2 + 1] << " and " << this->arr[index];
        this->swap(index * 2 + 1, index);
    }
}

void Heap::heapifyUp()
{
    int index = this->getSize() - 1;

    // while a the parent node is larger
    while ((index >= 2) &&
           ((this->arr[index] < this->arr[index / 2 - 1] && index % 2 == 0) ||
            (this->arr[index] < this->arr[index / 2] && index % 2 == 1)))
    {
        if (index % 2 == 0)
        {
            this->swap(index, index / 2 - 1);
            index = index / 2 - 1;
        }
        else
        {
            this->swap(index, index / 2);
            index = index / 2;
        }
    }

    // TODO incorperate into if else chain
    if (index == 1 && this->arr[index] < this->arr[0])
    {
        this->swap(1, 0);
    }
}

// swap
void Heap::swap(int a, int b)
{
    int num = this->arr[a];
    this->arr[a] = this->arr[b];
    this->arr[b] = num;
}
