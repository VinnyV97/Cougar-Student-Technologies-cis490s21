import osmnx as ox
import networkx as nx
import numpy as np
from shapely.geometry import mapping
from IPython.display import Image
from collections import defaultdict
%matplotlib inline
ox.config(log_console=True, use_cache=True)
ox.__version__

"""
This script demonstrates the uses of OSMnx in the context of our project
and shows three different ways to generate a map

 - from a city
 - from a lat/long
 - from an address

The dist variable will create a map within the value in meters 
the network type states what map type will be generated
For more information on features refer to the user manual
To run this script, see users manual to get OSMnx running on your machine
"""

G = ox.graph_from_place(San Marcos, California, USA, network_tpye = 'all')                                      # will create a map of San Marcos
# G = ox.graph_from_point((33.118054, -117.078971), dist = 50, network_type = 'all')                            # will create a map of Escondido
# G = ox.graph_from_address(333 S Twin Oaks Valley Rd, San Marcos, CA 92096), dist = 50, network_type = 'all')  # will create a map of CSUSM 

ox.plot_graph(G)
nodes,edges = ox.graph_to_gdfs(G)
list = G.nodes

# creates a list, pulls the lat & long of each node and places it in the list
coord = []
for i in list:
    lat = str(G.nodes[i]['y'])
    long = str(G.nodes[i]['x'])
    point = lat + ',' + long 
    coord.append(point)
    
print(*coord) 
