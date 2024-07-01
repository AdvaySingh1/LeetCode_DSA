#include <vector>
#include <string>

using namespace std;

/**
 * Promprt: Merge N sorted linked lists
 * Time complexity is O(nLogn) because the list is diveded in half and merging two sorted lists/arrays is O(n)
 */

//   Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *mergeKLists(vector<ListNode *> &lists)
    {
        if (lists.empty())
            return nullptr;
        while (lists.size() > 1)
        {
            vector<ListNode *> mergedList;

            for (size_t i = 0; i < lists.size(); i += 2)
            {
                ListNode *l1 = lists[i];
                ListNode *l2;
                if (i + 1 < lists.size())
                {
                    l2 = lists[i + 1];
                }
                else
                {
                    l2 = nullptr;
                }
                mergedList.push_back(mergeTwoLists(l1, l2));
            }
            lists = move(mergedList); // copies the mergedList without
            // the copy ctor (shallow copy since merged list not needed)
        }
        return lists.front(); // lists [0]
    }
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2)
    {
        ListNode dummy; // unlike python, create a listNode in the heap
        ListNode *tail = &dummy;

        // uslaly implemented with dynamic arrays
        while (l1 && l2)
        {
            if (l1->val <= l2->val)
            {
                tail->next = l1;
                l1 = l1->next;
            }
            else
            {
                tail->next = l2;
                l2 = l2->next;
            }
            tail = tail->next;
        }

        tail->next = l1 ? l1 : l2;
        // clear up the memory leaks here

        return dummy.next;
    }
};
