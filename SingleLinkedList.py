#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 单链表实现


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class SingleLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self

    def __next__(self):
        item = self.head
        if item is not None:
            self.head = self.head.next
            return item
        else:
            raise StopIteration

    def append(self, data):
        if not isinstance(data, Node):
            item = Node(data)
        else:
            item = data

        if self.head is None:
            self.head = item
            self.size += 1
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = item
            self.size += 1

    def delete(self, data):
        if self.is_empty():
            print('linked list is empty')
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        prev_node = self.head
        curr_node = self.head.next
        while curr_node.next is not None:
            if curr_node.data == data:
                prev_node.next = curr_node.next
            else:
                prev_node = curr_node
                curr_node = curr_node.next


if __name__ == '__main__':
    node1 = Node('a')
    node2 = Node('b')
    linked_list_1 = SingleLinkedList()
    linked_list_1.append(node1)
    linked_list_1.append(node2)
    for i in linked_list_1:
        print(i)
