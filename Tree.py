# Zoe Harris
# CSCE311 Assignment #3
# March 20, 2019

import argparse
from BST import BST
from AVL import AVL

# make parser using argParse()
parser = argparse.ArgumentParser()
parser.add_argument("expr", help="Enter file name")
parser.add_argument("second_expr", nargs="?", help="Enter second file name")
args = parser.parse_args()

# open file and read contents into trees
bst = BST()
avl = AVL()

file = open(args.expr)
for line in file:
    bst.insert(line)
    avl.insert(line)
file.close()

# print height and number of elements in each tree
print("BST Tree")
print("Inserted: " + str(bst.inserted) + "  Height: " + str(bst.height) + "\n")
print("AVL Tree")
print("Inserted: " + str(avl.inserted) + "  Height: " + str(avl.tree_height))

# if second file name given, use file contents to remove
# elements from existing trees
if args.second_expr:

    file = open(args.second_expr)
    for line in file:
        bst.remove(line)
        avl.remove(line)
    file.close()

    print("\nAfter Removal")
    print("BST Tree")
    print("Deleted: " + str(bst.deleted) + "  Height: " + str(bst.height) + "\n")
    print("AVL Tree")
    print("Deleted: " + str(avl.deleted) + "  Height: " + str(avl.tree_height))
