/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {
        if(head->next == nullptr) return NULL;
        ListNode *prev = nullptr, *slow = head, *fast = head;
        while (fast) {
            fast = fast->next;
            if (fast == nullptr)
                break;
            fast = fast->next;
            prev = slow;
            // cout << prev->val << endl;
            slow = slow->next;
            // cout << slow->val << endl;
        }
        prev->next = slow->next;
        slow->next = nullptr;
        delete slow;
        return head;
    }
};