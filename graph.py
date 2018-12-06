#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""图"""


class Graph:

    def __init__(self, v):
        self.v = v
        self.adj = [[] for _ in range(v)]

    def add_edge(self, s, t):
        self.adj[s].append(t)
        self.adj[t].append(s)

    # 广度优先搜索
    def bfs(self, s, t):
        if s == t:
            return
        visted = [False] * self.v
        visted[s] = True
        queue = [s]
        prev = [-1] * self.v
        while len(queue):
            w = queue.pop(0)
            for i in self.adj[w]:
                if not visted[i]:
                    prev[i] = w
                    if i == t:
                        self.print_path(prev, s, t)
                        return
                    visted[i] = True
                    queue.append(i)

    # 深度优先搜索
    def dfs(self, s, t):

        found = False
        visted = [False] * self.v
        prev = [-1] * self.v

        def recur_dfs(start):
            nonlocal found
            if found:
                return
            visted[start] = True
            if start == t:
                found = True
                return
            for i in self.adj[start]:
                if not visted[i]:
                    prev[i] = start
                    recur_dfs(i)
        recur_dfs(s)
        self.print_path(prev, s, t)

    def print_path(self, prev, s, t):
        if prev[t] != -1 and t != s:
            self.print_path(prev, s, prev[t])
        print('{}'.format(t), end=' ')

    def __str__(self):
        return str(self.adj)


if __name__ == '__main__':
    a = Graph(8)
    a.add_edge(0, 1)
    a.add_edge(0, 3)
    a.add_edge(1, 2)
    a.add_edge(1, 4)
    a.add_edge(2, 5)
    a.add_edge(3, 4)
    a.add_edge(4, 5)
    a.add_edge(4, 6)
    a.add_edge(5, 7)
    a.add_edge(6, 7)
    print(a)
    a.dfs(0, 6)
