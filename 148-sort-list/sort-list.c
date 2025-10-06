/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* getMid(struct ListNode* head);
struct ListNode* merge(struct ListNode* left, struct ListNode* right);

struct ListNode* sortList(struct ListNode* head) {
    if (head == NULL || head->next == NULL) {
        return head;
    }

    struct ListNode* mid = getMid(head);
    struct ListNode* left = sortList(head);
    struct ListNode* right = sortList(mid);

    return merge(left, right);
}

struct ListNode* getMid(struct ListNode* head) {
    struct ListNode* slow = head;
    struct ListNode* fast = head;
    struct ListNode* prev = NULL;

    while (fast && fast->next) {
        prev = slow;
        slow = slow->next;
        fast = fast->next->next;
    }

    if (prev) {
        prev->next = NULL;
    }

    return slow;
}

struct ListNode* merge(struct ListNode* left, struct ListNode* right) {
    struct ListNode dummy;
    dummy.next = NULL;
    struct ListNode* tail = &dummy;

    while (left && right) {
        if (left->val < right->val) {
            tail->next = left;
            left = left->next;
        } else {
            tail->next = right;
            right = right->next;
        }
        tail = tail->next;
    }

    tail->next = (left != NULL) ? left : right;
    return dummy.next;
}