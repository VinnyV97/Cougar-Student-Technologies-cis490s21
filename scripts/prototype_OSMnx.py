import osmnx as ox
import networkx as nx
import numpy as np
from shapely.geometry import mapping
from IPython.display import Image
from collections import defaultdict
%matplotlib inline
ox.config(log_console=True, use_cache=True)
ox.__version__

G = ox.graph_from_point((33.118054, -117.078971), dist = 50, network_type = 'all') 
ox.plot_graph(G)
nodes,edges = ox.graph_to_gdfs(G)
list = G.nodes
coord = []
for i in list:
    lat = str(G.nodes[i]['y'])
    long = str(G.nodes[i]['x'])
    point = lat + ',' + long 
    coord.append(point)
    
print(coord)