#ifndef MIN_HEAP_HPP
#define MIN_HEAP_HPP

#include <string>
using namespace std;

class Heap
{
public:
    // ctor
    Heap();

    // size
    int getSize();

    // return min element
    int extract_min();

    // remove min element
    void del_min();

    // insert element
    void insert(int num);

    // heapify down
    void heapifyDown();

    // heapify up
    void heapifyUp();

    // helper array for swapping
    void swap(int a, int b);

    ~Heap();

private:
    int size;
    int capacity;
    int *arr;
};

#endif