
from knowledge_graph import knowledge_associate as know1
from knowledge_graph import knowledge_relation as know2


if __name__=="__main__":
    know1=know1.associate()
    know2=know2.relationship()

    know1.connect("Newton", "Isaac Newton")

    print(know1.associate("Newton")) # {'Isaac Newton'}


    know2.connect("clock", "is", "a mechanical or electrical device for measuring time")

    know2.knowledge("clock")  # clock is a mechanical or electrical device for measuring time
