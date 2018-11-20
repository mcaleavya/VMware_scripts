#!/usr/bin/python
# Copyright (c) 2018 Allan McAleavy
# Licensed under the Apache License, Version 2.0 (the "License")

from collections import OrderedDict
import json
from sys import argv
cluster = argv[1]
fname = argv[2]

def fmt(d):
    l = []
    for (k,v) in d.items():
        j = OrderedDict()
        j['name'] = k
        if isinstance(v, dict):
            j['children'] = fmt(v)
        elif isinstance(v, list):
            for (k,v) in v:
                j[k] = v
        l.append(j)
    return l

# Build OrderedDict
d1 = OrderedDict()
row=[]

with open(fname) as f:
    for l in f:
        r = l.split(":")
        row = r[0].split(",")
        # Extract the columns you want to use as "leaves"
        leaves = [row[-1]]
        for l in leaves: row.remove(l)
        # Build a dictionary based on remaining row elements
        ctx = d1
        for e in row:
            if e not in ctx: ctx[e] = OrderedDict()
            ctx = ctx[e]

       # Re-insert leaves
        for l in leaves:
            ctx[l] =  [("size" , r[1].strip())]

d2 = {"name": cluster, "children": fmt(d1)}
j = json.dumps(d2, indent=4)
