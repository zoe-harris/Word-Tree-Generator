# Zoe Harris
# CSCE311 Assignment #3
# March 20, 2019

from AVLNode import AVLNode


class AVL:

    def __init__(self):

        self.root = None
        self.tree_height = 0
        self.inserted = 0
        self.deleted = 0

    def height(self, x):

        if x is None:
            return 0
        else:
            # recurse down each branch until x is None
            # this sets lh and rh initially to 0
            lh = self.height(x.left)
            rh = self.height(x.right)
            # for each call, return the greater height plus one
            if lh > rh:
                return lh + 1
            else:
                return rh + 1

    def rotate_with_left_child(self, k2):

        # rotate tree
        k1 = k2.left
        k2.left = k1.right
        k1.right = k2

        # update k1 and k2 heights
        k1.height = self.height(k1)
        k2.height = self.height(k2)

        # update root if needed
        if self.root is k2:
            self.root = k1

        return k1

    def rotate_with_right_child(self, k1):

        # rotate tree
        k2 = k1.right
        k1.right = k2.left
        k2.left = k1

        # update k1 and k2 heights
        k1.height = self.height(k1)
        k2.height = self.height(k2)

        # update root if needed
        if self.root is k1:
            self.root = k2

        return k2

    def double_with_left_child(self, k1):

        # rotate tree twice and return new root
        k1.left = self.rotate_with_right_child(k1.left)
        return self.rotate_with_left_child(k1)

    def double_with_right_child(self, k1):

        # rotate tree twice and return new root
        k1.right = self.rotate_with_left_child(k1.right)
        return self.rotate_with_right_child(k1)

    def __insert__(self, new_val, t):

        # if tree is not empty, insert node as a leaf
        if t is None:
            t = AVLNode(new_val, None, None)
            if self.root is None:
                self.root = t
            self.inserted += 1

        # check for duplicate value, increment duplicate counter
        elif t.val == new_val:
            t.duplicates += 1
            return t

        # recurse down left or right branch to find
        # correct place for new value
        elif new_val.lower() < t.val.lower():

            t.left = self.__insert__(new_val, t.left)

            # check for imbalance in left child
            if self.height(t.left) - self.height(t.right) > 1:
                # imbalance in left subtree of left child
                if new_val.lower() < t.left.val.lower():
                    t = self.rotate_with_left_child(t)
                # imbalance in right subtree of right child
                else:
                    t = self.double_with_left_child(t)

        elif new_val.lower() > t.val.lower():

            t.right = self.__insert__(new_val, t.right)

            # check for imbalance in right child
            if self.height(t.right) - self.height(t.left) > 1:
                # imbalance in left subtree of right child
                if new_val.lower() > t.right.val.lower():
                    t = self.rotate_with_right_child(t)
                else:
                    t = self.double_with_right_child(t)

        # update height of t and return it
        t.height = self.height(t)
        return t

    def insert(self, new_val):
        self.__insert__(new_val, self.root)
        self.tree_height = self.height(self.root)

    # print tree using inorder traversal
    def __print_tree__(self, x):
        if x is not None:
            self.__print_tree__(x.left)
            print(x.val)
            self.__print_tree__(x.right)

    def print_tree(self):
        self.__print_tree__(self.root)

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

    def find_parent(self, target):

        temp = self.root
        parent = None

        while temp is not None:
            if temp.right is not None:
                if temp.right.val == target.val:
                    parent = temp
                    return parent
            if temp.left is not None:
                if temp.left.val == target.val:
                    parent = temp
                    return parent
            if target.val.lower() > temp.val.lower():
                temp = temp.right
            elif target.val.lower() < temp.val.lower():
                temp = temp.left

        return parent

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

        else:

            if t.val == self.root.val:
                parent = self.root
            else:
                parent = self.find_parent(t)

            # node to be deleted has two children
            # copy right subtree's min val into node to be removed
            if t.left is not None and t.right is not None:
                t.val = self.find_min(t.right).val
                t.right = self.__remove__(t.val, t.right)

            # node to be removed has none or one child(ren)
            # return pointer to either "None" or one child
            else:
                if t.left is not None:
                    t = t.left
                else:
                    t = t.right

            # check for imbalance in left child
            if self.height(parent.right) - self.height(parent.left) == 2:
                # imbalance in right subtree of left child
                if self.height(parent.right.left) > self.height(parent.right.right):
                    parent = self.double_with_right_child(parent)
                # imbalance in left subtree of left child
                else:
                    parent = self.rotate_with_right_child(parent)

            # check for imbalance in right child
            if self.height(parent.left) - self.height(parent.right) == 2:
                # imbalance in left subtree of right child
                if self.height(parent.left.right) > self.height(parent.left.left):
                    parent = self.double_with_left_child(parent)
                # imbalance in right subtree of right child
                else:
                    parent = self.rotate_with_left_child(parent)

        return t

    def remove(self, val):

        if self.search(val) is not None:
            self.__remove__(val, self.root)
            self.deleted += 1
            self.tree_height = self.height(self.root)



