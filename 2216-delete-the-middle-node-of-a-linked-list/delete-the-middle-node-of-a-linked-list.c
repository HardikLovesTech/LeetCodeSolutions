/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteMiddle(struct ListNode* head) {
    struct ListNode* prev = (struct ListNode*)malloc(sizeof(struct ListNode));
    prev->val = 0;
    prev->next = head;
    struct ListNode* fast = head;
    struct ListNode* slow = prev;
    while(fast != NULL && fast->next != NULL){
        slow = slow->next;
        fast = fast->next->next;
    }
    struct ListNode* temp = slow->next;
    slow->next = slow->next->next;
    free(temp);
    struct ListNode* NewHead = prev->next;
    free(prev);
    return NewHead;
}