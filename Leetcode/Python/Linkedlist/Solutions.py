from Linkedlist import LinkList
from Linkedlist import ListNode

class Solution:
    # 有序链表合并
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur1 = l1
        cur2 = l2
        if (cur1.val <= cur2.val):
            head = cur1
            tmp = cur1
            cur1 = cur1.next
        else:
            head = cur2
            tmp = cur2
            cur2 = cur2.next
        while 1:
            if cur1 == None:
                tmp.next = cur2
                return head
            elif cur2 == None:
                tmp.next = cur1
                return head
            else:
                if cur1.val <= cur2.val:
                    tmp.next = cur1
                    cur1 = cur1.next
                    tmp = tmp.next
                else:
                    tmp.next = cur2
                    cur2 = cur2.next
                    tmp = tmp.next

    def Reverse(self, l):
        """
        Reverse Linked list
        type l: ListNode
        rtype : ListNode
        """
        cur1 = l
        # if l lenth is 1
        if cur1.next != None:
            # set cur2 cur1.next
            cur2 = cur1.next
            cur1.next = None
        else:
            return cur1
        
        while cur2.next != None:
            # set cur3 for cur2
            cur3 = cur2.next

            # reverse cur2.next to cur1    cur1 cur2->cur3->..   ---> cur1<-cur2 cur3->..
            cur2.next = cur1
            # reset cur1 cur2              []<-cur1  cur2(cur3)->..
            cur1 = cur2
            cur2 = cur3
        
        # set final link
        cur2.next = cur1

        return cur2




def mergeTwoLists_test(l1,l2):
    """
    test_main for mergeTwoList
    type l1: list
    type l2: list
    rtype: None
    """
    
    ll1 = LinkList()
    ll2 = LinkList()
    
    ll1.InitFromList(l1)
    ll2.InitFromList(l2)

    sol = Solution()

    ans_pt = sol.mergeTwoLists(ll1.list,ll2.list)

    ans = LinkList()
    ans.InitFromPt(ans_pt)

    return ans.ToList()

def Reverse_test(l):
    """
    Test for Reverse
    type l: List
    rtype: List
    """
    ll = LinkList()
    ll.InitFromList(l)
    sol = Solution()
    ans_pt = sol.Reverse(ll.list)
    ans = LinkList()
    ans.InitFromPt(ans_pt)
    return ans.ToList()



if __name__ == "__main__":
    #ans = mergeTwoLists_test([1,2,3,4],[1,2,3,4,5])
    print(Reverse_test([1,2,3,4,5,6]))

   # print("helloWhorld")
    