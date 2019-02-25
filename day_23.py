#-----Day 22: Binary Search Trees-------#




    def getHeight(self,root):
        if root:
            leftDepth = self.getHeight(root.left)
            rightDepth = self.getHeight(root.right)

            if leftDepth > rightDepth:
                return leftDepth + 1
            else:
                return rightDepth + 1
        else:
            return -1






