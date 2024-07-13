#include <cstddef>
using namespace std;
// Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution
// O(P + C) solution where C is the size of the cucle
{
public:
    ListNode *detectCycle(ListNode *head)
    {
        ListNode *fast = head, *slow = head;

        while (fast && fast->next)
        {
            fast = fast->next->next;
            slow = slow->next;
            if (fast == slow)
            {
                break;
            }
        }
        if (fast == NULL || fast->next == nullptr)
        {
            return NULL;
        }

        ListNode *slow2 = head;

        while (slow != slow2)
        {
            slow = slow->next;
            slow2 = slow2->next;
        }
        return slow;
    }
};