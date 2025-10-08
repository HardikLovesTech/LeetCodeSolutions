/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    struct ListNode* pA = headA;
    struct ListNode* pB = headB;
    
    while(pA != pB){
        pA = (pA == NULL) ? headA : pA->next;
        pB = (pB == NULL) ? headB : pB->next;
    }
    
    return pA;
}