"""
This knowledge graph is used for association, and it represents how strong the association is.
It is not representing the relationship between concepts.
The association is trainable with neural networks.
This knowledge graph is based on networkx module.

Example:
>>> know=knowledge
>>> k_net=know.load("knowledge_graph.nx")
>>> k_net["Newton"] # w: weight
AtlasView({'science': {'w': 1}, 'Isaac Newton': {'w': 1}})


"""


import json
import networkx as nx
import numpy as np

import matplotlib.pyplot as plt


class knowledge:
    def create():
        k_net = nx.Graph()
        return k_net
    
    def connect(k_net, a, b):
        k_net.add_edge(*(a, b))
        k_net[a][b]["w"]=1
        return k_net

    def weight_plus(k_net, a, b):
        try:
            w=k_net[a][b]["w"]
        except:
            k_net[a][b]["w"]=1
            w=1
        k_net[a][b]["w"]=w+1
        return k_net

    def delete_connection(k_net, a, b):
        k_net.remove_edge(a, b)
        return k_net

    def delete_concept(k_net, a):
        k_net.remove_node(a)
        return k_net

    def save(k_net, filename):
        nx.write_graphml(k_net, filename)
        return None

    def load(filename):        
        return nx.read_graphml(filename)
    

    def associate(k_net, a):
        try:
            return set(k_net[a])
        except:
            return set([])

    def intersection(k_net, a, b):
        set1=know.associate(k_net, a)
        set2=know.associate(k_net, b)

        return set1.intersection(set2)

    def plot(k_net):
        nx.draw(k_net, with_labels=True)
        plt.show()
        return None

    def summary(k_net):
        print("number of concepts: %d" % (len(k_net)))
        print("number of connections:", len(k_net.edges))
        return None


def load_knowledge():
    know=knowledge
    k_net=know.load("knowledge_graph.npy")
    
    return k_net


know=knowledge

#k_net=know.load("knowledge_graph.nx")


# know.save(k_net, "knowledge_graph")
