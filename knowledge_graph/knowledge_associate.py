"""
This knowledge graph is used for association, and it represents how strong the association is.
It is not representing the relationship between concepts.
The association is trainable with neural networks.
This knowledge graph is based on networkx module.
"""


import json
import networkx as nx
import numpy as np

import matplotlib.pyplot as plt
import pickle

class associate:
    def __init__(self):
        self.graph = nx.Graph()

    def connect(self, a, b):
        self.graph.add_edge(*(a, b))
        self.graph[a][b]["w"]=1

    def weight_plus(self, a, b):
        try:
            w=self.graph[a][b]["w"]
        except:
            self.graph[a][b]["w"]=1
            w=1
        self.graph[a][b]["w"]=w+1

    def delete_connection(self, a, b):
        self.graph.remove_edge(a, b)

    def delete_concept(self, a):
        self.graph.remove_node(a)

    def save(self, filename):
        f = open(filename, 'wb')
        pickle.dump(self.graph, f)
        f.close()

    def load(self, filename):
        f = open(filename, 'rb')
        self.graph = pickle.load(f)
        f.close()
    

    def associate(self, a):
        try:
            return set(self.graph[a])
        except:
            return set([])

    def intersection(self, a, b):
        set1=know.associate(a)
        set2=know.associate(b)

        return set1.intersection(set2)

    def plot(self):
        nx.draw(self.graph, with_labels=True)
        plt.show()
        return None

    def summary(self):
        print("number of concepts: %d" % (len(self.graph)))
        print("number of connections:", len(self.graph.edges))
        return None


if __name__=="__main__":
    know=associate()

    know.connect("Newton", "Isaac Newton")

    print(know.graph["Newton"])
    print(know.associate("Newton"))

    know.save("knowledge.know1")
