/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

typedef struct ListNode* node;

node ReverseList(node head){
    node prev = NULL;
    node curr = head;
    while(curr){
        node next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}

node removeNthFromEnd(node head, int n) {

    if (!head) return NULL;
    
    node revHead = ReverseList(head);    
    node curr = revHead;
    node prev = NULL;

    for (int i = 1; i < n && curr != NULL; i++) {
        prev = curr;
        curr = curr->next;
    }
    if (!curr) return ReverseList(revHead);

    if (!prev) {
        revHead = curr->next;
    } else {
        prev->next = curr->next;
    }

    free(curr);

    return ReverseList(revHead);

}