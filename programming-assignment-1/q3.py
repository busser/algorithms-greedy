#!/usr/bin/env python3 -B

import datetime
import graph

G = graph.Graph()

print(datetime.datetime.now(), "Reading graph...")
with open("edges.txt") as f:
    for line in f.readlines()[1:]:
        G.add_edge(*map(int, line.split()))

print(datetime.datetime.now(), "Computing minimum spanning tree...")
mst = G.mst_prim()

print(datetime.datetime.now(), "Computing overall cost...")
mst_cost = 0
for (node, edges) in mst._adj_list.items():
    mst_cost += sum([weight for (_, weight) in edges])
mst_cost //= 2 # graph is undirected: edges are doubled

print(mst_cost)
