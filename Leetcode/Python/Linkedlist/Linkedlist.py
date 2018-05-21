class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkList:
    def __init__(self):
        self.list = None
    def InitFromList(self,l):
        self.list = ListNode(l[0])
        cur = self.list
        for x in l[1:]:
            cur.next = ListNode(x)
            cur = cur.next
    def Print(self):
        cur = self.list
        while cur != None :
            print("%d->"  % cur.val,end = "")
            cur = cur.next
    def lenth(self):
        cur = self.list
        count = 0
        while cur != None :
            count += 1
            cur = cur.next
        return count
    def InitFromPt(self,x):
        self.list = x
    
    def ToList(self):
        ans = list()
        cur = self.list
        while cur != None:
            ans.append(cur.val)
        return ans