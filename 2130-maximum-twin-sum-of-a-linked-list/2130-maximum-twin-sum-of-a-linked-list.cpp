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
    int pairSum(ListNode* head) {
        ListNode* slow,* fast, *prev, *next;
        slow = fast = head;
        prev = nullptr;
        next = slow->next;
        while(fast != nullptr){
            fast = fast->next->next;
            slow->next = prev;
            prev = slow;
            slow = next;
            next = next->next;
        }
        int maxi = 0;
        while(prev && slow){
            maxi = max(maxi, prev->val + slow->val);
            slow = slow->next;
            prev = prev->next;
        }
        return maxi;
    }
};