from ./Linkedlist.py import Linkedlist
from ./Linkedlist.py import ListNode

class Solution:
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


def main


if __name__ == 'main':
    main()