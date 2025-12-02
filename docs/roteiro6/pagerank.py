import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import time
from collections import defaultdict

import networkx as nx

G = nx.DiGraph()

with open("soc-Epinions1.txt") as f:
    for line in f:
        if line.startswith("#"):
            continue
        a, b = map(int, line.split())
        G.add_edge(a, b)
