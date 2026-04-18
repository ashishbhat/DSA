class BST:
    class Node:
        def __init__(self, data):
            self.data  = data
            self.left  = None
            self.right = None

    @staticmethod
    def _traverse(head: Node) -> None:
        if head is None:
            return
        print(head.data)
        BST._traverse(head.left)
        BST._traverse(head.right)

    def __init__(self,arr):
        self.__head = BST.Node(arr[0]) if arr else None
        for i in range(1,len(arr)):
            self.insert(arr[i])

    def insert(self, n) -> None:
        if self.__head is None:
            self.__head = BST.Node(n)
            return
        temp = self.__head
        while temp:
            if n > temp.data:
                if temp.right is None:
                    temp.right = BST.Node(n)
                    break
                else:
                    temp = temp.right
            else:
                if temp.left is None:
                    temp.left = BST.Node(n)
                    break
                else:
                    temp = temp.left
    
    def pre_order(self):
        BST._traverse(self.__head)


    def predecessot(self, target: Node) -> int :
        temp = self.__head
        predecessor = -1
        while(temp.data != target):
            if temp.data > predecessor and temp.data < target:
                predecessor = temp.data;
            if target <= temp.data:
                temp= temp.left
            else:
                temp = temp.right


        if temp.left != None:
            temp = temp.left
            while temp.right:
                temp = temp.right
            predecessor = temp.data

        return predecessor

if __name__ == "__main__":
    arr = [10,20,5,6,75,11,9,101,2]
    tree = BST(arr)
    tree.pre_order()
    print(tree.predecessot(9))