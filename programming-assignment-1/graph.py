#!/usr/bin/env python3

import collections
import math

class Graph:

    def __init__(self):
        self._adj_list = {}

    def add_node(self, V):
        if V not in self._adj_list:
            self._adj_list[V] = []

    def add_edge(self, V, W, weight):
        self.add_node(V)
        self.add_node(W)
        self._adj_list[V].append((W, weight))
        self._adj_list[W].append((V, weight)) # graph is undirected

    def mst_prim(self):
        mst = Graph()
        unexplored_nodes = {vertex: (math.inf, None) for vertex in self._adj_list.keys()}
        while len(unexplored_nodes) != 0:
            node = min(unexplored_nodes, key = unexplored_nodes.get)
            weight, parent = unexplored_nodes.pop(node)
            if parent is not None:
                mst.add_edge(parent, node, weight)
            for neighbor, weight in self._adj_list[node]:
                if neighbor in unexplored_nodes and weight < unexplored_nodes[neighbor][0]:
                    unexplored_nodes[neighbor] = (weight, node)
        return mst
