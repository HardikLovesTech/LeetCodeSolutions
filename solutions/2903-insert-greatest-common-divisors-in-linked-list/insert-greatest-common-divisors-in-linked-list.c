/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// Helper function to compute GCD
int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

struct ListNode* insertGreatestCommonDivisors(struct ListNode* head) {
    struct ListNode* curr = head;

    while (curr != NULL && curr->next != NULL) {
        int g = gcd(curr->val, curr->next->val);

        // Allocate and initialize the new node
        struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
        newNode->val = g;
        newNode->next = curr->next;

        // Insert the new node
        curr->next = newNode;

        // Move to the next original node
        curr = newNode->next;
    }

    return head;
}
