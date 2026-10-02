class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* t1 = l1;
        ListNode* t2 = l2;
        ListNode* dummy = new ListNode(-1);
        ListNode* curr = dummy;
       dummy->next = NULL;
        int c = 0;
        while(t1!=NULL || t2!=NULL){
            int sum = c;
            if(t1) sum+=t1->val;
            if(t2) sum+=t2->val;
            ListNode* newnode = new ListNode(sum%10);
            c = sum/10;
            curr->next = newnode;
            curr = curr->next;
            if(t1) t1 = t1->next;
            if(t2) t2 = t2->next;
        }
        if(c){
            ListNode* newnode = new ListNode(c);
            curr->next = newnode;
            curr = curr->next;
        }
        return dummy->next;
    }
};