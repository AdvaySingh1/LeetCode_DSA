#include <vector>
using namespace std;

class MinStack
{
public:
    MinStack()
    {
    }

    void push(int val)
    {
        stack.push_back(val);
        if (minStack.size() == 0)
        {
            minStack.push_back(val);
        }
        else
        {
            minStack.push_back(min(val, minStack[minStack.size() - 1]));
        }
    }

    void pop()
    {
        stack.pop_back();
        minStack.pop_back();
    }

    int top()
    {
        return stack[stack.size() - 1];
    }

    int getMin()
    {
        return minStack[minStack.size() - 1];
    }

private:
    vector<int> stack;
    vector<int> minStack;
};