

    def insert(self,head,data): 
    #Complete this method
        if head==None:
            head=Node(data)
        
        #current=head
        elif head.next==None:
            head.next=Node(data)
        else:
            self.insert(head.next,data)
        return head
              
     
    


