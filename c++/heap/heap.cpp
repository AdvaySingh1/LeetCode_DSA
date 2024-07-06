#include <vector>

using namespace std;

class MinHeap
{
public:
    MinHeap()
    {
        heap.push_back(0); // dummy val for math later
    }

    void push(int val)
    {
        heap.push_back(val);
        _bubbleUp(heap.size() - 1);
    }

    int pop()
    {
        if (heap.size() <= 1)
        {
            return -1; // would usually throw an error
        }
        int res = heap[1];
        if (heap.size() == 2)
        {
            heap.pop_back();
            return res;
        }

        heap[1] = heap.back();
        heap.pop_back();
        _bubbleDown(1);
        return res;
    }

    int top()
    {
        return (heap.size() > 1 ? heap[1] : -1); // would throw error
    }

    void heapify(const vector<int> &arr)
    {
        // maybe set empty before this
        heap.insert(heap.end(), arr.begin(), arr.end());

        for (int i = heap.size() / 2; i >= 1; i--)
        {
            _bubbleDown(i);
        }
    }

private:
    vector<int> heap;

    // requirement: i is a valid index
    void _bubbleUp(int i)
    {
        while (i > 1 && heap[i / 2] > heap[i])
        {
            swap(heap[i], heap[i / 2]);
            i /= 2;
        }
    }
    // requirement: i is a valid index
    void _bubbleDown(int i)
    {
        int child = i * 2;
        while (child < heap.size())
        {
            if (child + 1 < heap.size() && heap[child + 1] < heap[i] && heap[child + 1] < heap[child])
            {
                child++;
            }
            if (heap[child] < heap[i])
            {
                swap(heap[child], heap[i]);
                i = child;
                child = i * 2;
            }
            else
            {
                break;
            }
        }
    }
};
