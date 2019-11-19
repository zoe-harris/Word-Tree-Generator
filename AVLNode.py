# Zoe Harris
# CSCE311 Assignment #3
# March 20, 2019


class AVLNode:

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.duplicates = 0
        self.height = 0
