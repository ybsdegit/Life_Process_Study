#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/1/22 9:07
# @author: Paulson●Wier
# @file: depth_level_tree.py
# @desc:

'''
tree
          D
    B           C
F       G             A
      E             H
'''

class Tree:
    root = ''
    right = None
    left = None
    # 初始化类
    def __init__(self,node):
        self.root = node

    def set_root(self,node):
        self.root = node

    def get_root(self):
        return self.root

    #初始化树
    #设置所有节点
a = Tree('A')
b = Tree('B')
c = Tree('C')
d = Tree('D')
e = Tree('E')
f = Tree('F')
g = Tree('G')
h = Tree('H')

#设置节点之间的联系，生成树
a.left = h
b.left = f
b.right = g
c.right = a
d.left = b
d.right = c
g.left = e


# 深度优先 ： 根左右 遍历 （递归实现）
def depth_tree(tree_node):
    if tree_node is not None:
        print(tree_node.root)
        #访问左子树
        if tree_node.left is not None:
            depth_tree(tree_node.left) #递归遍历
        if tree_node.right is not None:
            depth_tree(tree_node.right) #递归遍历

# depth_tree(d)    #传入根节点
# results : D B F G E C A H

# 广度优先 ： 层次遍历 （队列实现）
def level_queue(root):
    if root is None:
        return
    my_queue = []
    node = root
    my_queue.append(node)       #根节点入队列
    i= 0
    while my_queue:
        i = i+1
        node = my_queue.pop(0)  #出队列
        print("广度遍历结果{}".format(i),node.root)        #访问节点
        if node.left is not None:
            my_queue.append(node.left)  #入队列
        if node.right is not None:
            my_queue.append(node.right)

level_queue(d)
# results :D B C F G A E H