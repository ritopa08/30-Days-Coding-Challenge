#-----Day 24: More Linked Lists-------#


    def removeDuplicates(self,head):
        #Write your code here
        if head==None:
            return head
        elif head.next==None:
            return head
        elif head.data==head.next.data:
            head.next=head.next.next
            self.removeDuplicates(head)
        else:
            self.removeDuplicates(head.next)
        return head





