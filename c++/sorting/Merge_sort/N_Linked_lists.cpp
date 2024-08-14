#include <vector>
#include <string>

using namespace std;

/**
 * Promprt: Merge N sorted linked lists
 * Time complexity is O(mnLogn) because the list is diveded in half and merging two sorted lists/arrays is O(m)
 *
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
    /**
     * @brief Returns Something
     * @param lists A list of Node points
     * @return ListNode* Another List
     */
    ListNode *mergeKLists(vector<ListNode *> &lists)
    {
        if (lists.size() == 0)
            return {};
        if (lists.size() == 1)
            return lists[0];
        vector<ListNode *> res;
        for (int i = 0; i < lists.size(); i += 2)
        {
            if (i + 1 < lists.size())
                res.push_back(mergeNodes(lists[i], lists[i + 1]));
            else
                res.push_back(lists[i]);
        }
        return mergeKLists(res);
    }

    ListNode *mergeNodes(ListNode *a, ListNode *b)
    {
        ListNode *res = new ListNode;
        ListNode *curr = res;
        while (a != nullptr && b != nullptr)
        {
            if (a->val <= b->val)
            {
                curr->next = a;
                a = a->next;
            }
            else
            {
                curr->next = b;
                b = b->next;
            }
            curr = curr->next;
        }
        curr->next = (a != nullptr) ? a : b;
        return res->next;
    }
};
