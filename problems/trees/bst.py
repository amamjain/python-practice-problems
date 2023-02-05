class Empty:

    def __init__(self):
        # nothing to do!
        pass

    def is_empty(self):
        return True

    def is_leaf(self):
        return False

    def num_nodes(self):
        return 0

    def height(self):
        return 0

    def contains(self, n):
        return False

    def insert(self, n):
        return Node(n, Empty(), Empty())
    
    def inorder(self):
        return []
    
    def min_item(self):
        return None
    
    def max_item(self):
        return None
    
    def balance_factor(self):
        return None
    
    def balanced_everywhere(self):
        return True
    
    def add_to_all_help(self, integer):
        return
    
    def path_to(self, integer):
        return None


class Node:

    def __init__(self, n, left, right):
        self.value = n
        self.left = left
        self.right = right

    def is_empty(self):
        return False

    def is_leaf(self):
        return self.left.is_empty() and self.right.is_empty()

    def num_nodes(self):
        return 1 + self.left.num_nodes() + self.right.num_nodes()

    def height(self):
        return 1 + max(self.left.height(), self.right.height())

    def contains(self, n):
        if n < self.value:
            return self.left.contains(n)
        elif n > self.value:
            return self.right.contains(n)
        else:
            return True

    def insert(self, n):
        if n < self.value:
            return Node(self.value, self.left.insert(n), self.right)
        elif n > self.value:
            return Node(self.value, self.left, self.right.insert(n))
        else:
            return self
    
    def inorder(self):
        if self.is_empty():
            return []
        else:
            return self.left.inorder() + [self.value] + self.right.inorder()
        
    def min_item(self):
        if self.is_empty():
            return None
        elif self.left.is_leaf:
            return self.left.value
        else:
            return self.left.min_item()
    
    def max_item(self):
        if self.is_empty():
            return None
        elif self.right.is_leaf:
            return self.right.value
        else:
            return self.right.max_item()
        
    def balance_factor(self):
        if self.is_empty():
            return None
        else:
            return self.right.height() - self.left.height()
        
    def balance_everywhere(self):
        if self.balance_factor and self.left.balance_everywhere() and self.left.balance_everywhere() != 0 or 1 or -1:
            return False
        return True
    
    def add_to_all(self, integer):
        self.add_to_all_help(integer)
        return self
    
    #HELPER    
    def add_to_all_help(self, n):     
        self.value += n
        self.left.add_to_all_help(n)
        self.right.add_to_all_help(n)
        
    def path_to(self, n):
        if self.contains(n):
            if n < self.value:
                return [self.value] + self.left.path_to(n)
            if n > self.value:
                return [self.value] + self.right.path_to(n)
            else:
                return [self.value]
        else:
            return None

if __name__ == "__main__":
    bst = Empty().insert(42).insert(10).insert(15).insert(63)

    print(f"The number of nodes is {bst.num_nodes()}")
    print(f"The height is {bst.height()}")
