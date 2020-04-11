# knowledge_graph_with_networkx
This is an attempt to represent knowledge by associating, and it gives what a concept is related to and how strong the connection is. It is not representing the relationship between concepts. Also, the association is trainable with neural networks.
This knowledge graph is based on networkx module.

## requirement
```
networkx
```

## usage
Creating a new knowledge graph and save
```
>>> know=knowledge()
>>> know.connect("Newton", "Isaac Newton")
>>> print(know.graph["Newton"])
{'Isaac Newton': {'w': 1}}
>>> print(know.associate("Newton"))
{'Isaac Newton'}
>>> know.save("knowledge.nx")
```
