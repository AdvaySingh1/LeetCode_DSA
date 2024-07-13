#include <vector>
using namespace std;

// Definition for singly-linked list.
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
    int pairSum(ListNode *head)
    {

        ListNode *fast = head, *slow = head, *prev = nullptr;
        while (fast && fast->next)
        {
            fast = fast->next->next;
            ListNode *tmp = slow;
            slow = slow->next;
            tmp->next = prev;
            prev = tmp;
        }

        int max_sum = 0; // unsigned ints
        while (slow)
        {
            int curr_sum = slow->val + prev->val;
            max_sum = max(max_sum, curr_sum);
            slow = slow->next;
            prev = prev->next;
        }

        return max_sum;
    }

    /* The following is the O(n) space and time solution */
    // add all of the values
    //     ListNode * slow = head, *fast = head;

    //     while (fast && fast->next) {
    //         fast = fast->next->next;
    //         slow = slow->next;
    //     }

    //     vector<int> arr;

    //     while (slow) {
    //         arr.push_back(slow->val);
    //         slow = slow->next;
    //     }

    //     int max_sum = 0;
    //     for (int i = arr.size() - 1; i >= 0; i--){
    //         int curr_sum = arr[i] + head->val;
    //         max_sum = max(max_sum, curr_sum);
    //         head = head->next;
    //     }

    //     return max_sum;
    // }
};