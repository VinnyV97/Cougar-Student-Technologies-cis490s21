import osmnx as ox
import networkx as nx
import numpy as np
from shapely.geometry import mapping
from IPython.display import Image
from collections import defaultdict
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
ox.config(log_console=True, use_cache=True)
ox.__version__

G = ox.graph_from_place('San Marcos, California, USA', network_type='drive')
nodes,edges = ox.graph_to_gdfs(G)
list = G.nodes

for i in list:
    print(G.nodes[i]['y'])
    print(G.nodes[i]['x'])
    print("\n")