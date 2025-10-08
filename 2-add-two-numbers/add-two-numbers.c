/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* t1,*t2,*h;
    struct ListNode* t=NULL;
    t1=l1;
    t2=l2;
    int s=0;
    int c=0;
    while(t1!=NULL || t2!=NULL){
        s=0;
        struct ListNode*n=(struct ListNode*)malloc(sizeof(struct ListNode));
        if(t1!=NULL){
            s+=t1->val;
            t1=t1->next;
        }
        if(t2!=NULL){
            s+=t2->val;
            t2=t2->next;
        }
        n->val=(s+c)%10;
        c=(c+s)/10;
        n->next=NULL;
        if(t==NULL){
            t=n;
            h=t;
        }
        else{
            t->next=n;
            t=n;

        }

    }
    if(c>0) {
    struct ListNode* n =(struct ListNode*)malloc(sizeof(struct ListNode));
    n->val=c;
    n->next=NULL;
    t->next=n;
    }

    return h;

}