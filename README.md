# knowledge_graph_with_networkx
This is an attempt to represent knowledge by associating and relationship. knowledge_associate gives  what a concept is related to and how strong the connection is. Knowledge_reationship gives the relationship between concepts. 

## requirement
```
matplotlib
networkx
```

## usage
2 types of knowledge graphs are available. Knowledge_associate represents just connections between concepts.
```
>>> from knowledge_graph import knowledge_associate as know1
>>> know1=know1.associate()
>>> know1.connect("Newton", "Isaac Newton")
>>> print(know1.associate("Newton"))
{'Isaac Newton'}
>>> print(know1.graph["Newton"])
{'Isaac Newton': {'w': 1}}
>>> know1.save("knowledge.know1")
```
Here is the other way of representing knowledge. It represents the relationship between concepts.
```
>>> from knowledge_graph import knowledge_relation as know2
>>> know2.connect("clock", "is", "a mechanical or electrical device for measuring time")
>>> know2.knowledge("clock")
clock is a mechanical or electrical device for measuring time
>>> know2.save("knowledge.know2")
```
