#include <iostream>
class LinkedList
{
public:
    LinkedList()
        : size(0)
    {
        first = new Node;
        first->next = nullptr;
        last = first;
    }

    int get(int index)
    {
        if (index >= size)
        {
            return -1;
        }
        Node *n = first;
        for (int i = 0; i < index; i++, n = n->next)
        {
        }
        return n->val;
    }

    void insertHead(int val)
    {
        if (size == 0)
        {
            first->val = val;
        }
        else
        {
            Node *newNode = new Node;
            newNode->val = val;
            newNode->next = first;
            first = newNode;
        }
        size++;
    }

    void insertTail(int val)
    {
        if (size == 0)
        {
            first->val = val;
        }
        else
        {
            Node *newNode = new Node;
            newNode->val = val;
            last->next = newNode;
            last = newNode;
            last->next = nullptr;
        }
        size++;
    }

    bool remove(int index)
    {
        if (size == 0 || index >= size)
        {
            return false;
        }
        Node *n = first;

        if (index == 0)
        {
            first = first->next;
            size--;
            return true;
        }

        int i = 0;
        for (; i < index - 1; i++, n = n->next)
        {
        }
        if (i + 2 >= size)
        {
            last = n;
            last->next = nullptr;
        }
        else
        {
            n->next = n->next->next;
        }
        size--;
        return true;
    }

    vector<int> getValues()
    {
        vector<int> vals;
        Node *n = first;
        for (int i = 0; i < size; i++, n = n->next)
        {
            vals.push_back(n->val);
        }
        return vals;
    }

private:
    struct Node
    {
        Node *next;
        int val;
    };
    Node *first;
    Node *last;
    int size = 0;
};
