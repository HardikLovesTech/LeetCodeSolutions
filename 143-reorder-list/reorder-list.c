/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

typedef struct ListNode node;

node *ReverseList(node *head){
    node *curr = head;
    node *prev = NULL;
    while(curr){
        node *next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}

void reorderList(node *head) {
    if (!head || !head->next) return;
    node *slow = head;
    node *fast = head;
    while(fast->next && fast->next->next){
        slow = slow->next;
        fast = fast->next->next;
    }

    node *second = ReverseList(slow->next);
    slow->next = NULL;

    node *first = head;
    while(second){
        node *temp1 = first->next;
        node *temp2 = second->next;
        first->next = second;
        second->next = temp1;
        first = temp1;
        second = temp2;
    }
}