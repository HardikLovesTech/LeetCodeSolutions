/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

typedef struct ListNode Behenchod;

bool hasCycle(Behenchod *head) {
    if(head == NULL || head->next == NULL) return false;


    Behenchod *slow = head;
    Behenchod *fast = head;
    
    while(fast != NULL && fast->next != NULL){
        slow = slow->next;
        fast = fast->next->next;

        if(slow == fast){
            return true;
        }
    }
    return false;
}