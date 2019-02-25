#-----Day 23: BST Level-Order Traversal-------#




    def depth(self,node):
        #node=root
        if node==None:
            return 0;
        else:
            l_h=self.depth(node.left)
            r_h=self.depth(node.right)

            if(l_h>r_h):
                return l_h+1
            else:
                return r_h+1





