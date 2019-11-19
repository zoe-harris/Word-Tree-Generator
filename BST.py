# Zoe Harris
# CSCE311 Assignment #3
# March 20, 2019

from BinaryNode import BinaryNode


class BST:

    def __init__(self):
        self.root = None
        self.height = 0
        self.inserted = 0
        self.deleted = 0

    def __insert__(self, new_val, t):

        # if tree is empty, make root
        if self.root is None:
            t = BinaryNode(new_val, None, None)
            self.root = t
            self.inserted += 1
            return t

        # if tree is not empty, insert node as a leaf
        if t is None:
            t = BinaryNode(new_val, None, None)
            self.inserted += 1

        # check for duplicate value, increment duplicate counter
        if t.val == new_val:
            t.duplicates += 1
            return t

        # recurse down left or right branch to find correct
        # place for new value
        elif new_val.lower() < t.val.lower():
            t.left = self.__insert__(new_val, t.left)
        elif new_val.lower() > t.val.lower():
            t.right = self.__insert__(new_val, t.right)

        return t

    def insert(self, new_val):
        self.__insert__(new_val, self.root)
        self.set_height()

    def find_min(self, x):
        while x.left is not None:
            x = x.left
        return x

    def __remove__(self, val, t):

        # node containing val does not exist
        if t is None:
            return t

        # recursive call on left branch
        if val.lower() < t.val.lower():
            t.left = self.__remove__(val, t.left)

        # recursive call on right branch
        elif val.lower() > t.val.lower():
            t.right = self.__remove__(val, t.right)

        # node to be removed has two children
        # copy right subtree's min val into node to be removed
        # recursively remove node to be removed
        elif t.left is not None and t.right is not None:
            t.val = self.find_min(t.right).val
            t.right = self.__remove__(t.val, t.right)

        # node to be removed has none or one child(ren)
        # return pointer to either "None" or one child
        else:
            if t.left is not None:
                t = t.left
            else:
                t = t.right

        return t

    def remove(self, val):
        if self.search(val) is not None:
            self.__remove__(val, self.root)
            self.deleted += 1
            self.set_height()

    # print tree using inorder traversal
    def __print_tree__(self, x):

        if x is not None:
            self.__print_tree__(x.left)
            print(x.val)
            self.__print_tree__(x.right)

    def search(self, target):

        temp = self.root
        found = None

        while temp is not None:
            if temp.val == target:
                found = temp
                return found
            elif target.lower() < temp.val.lower():
                temp = temp.left
            elif target.lower() > temp.val.lower():
                temp = temp.right

        return found

    def print_tree(self):
        self.__print_tree__(self.root)

    def get_height(self, x):

        if x is None:
            return 0
        else:
            # recurse down each branch
            lh = self.get_height(x.left)
            rh = self.get_height(x.right)

            # for each call, return the greater height plus one
            if lh > rh:
                return lh + 1
            else:
                return rh + 1

    def set_height(self):
        self.height = self.get_height(self.root)
