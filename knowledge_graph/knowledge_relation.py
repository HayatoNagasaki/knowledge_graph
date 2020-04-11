"""
Knowldge Graph:
this program is the experiment for representing knowledge for AI
"""

import numpy as np
import pickle


class relationship:
    def __init__(self):
        self.db={}

    def knowledge(self, x):
        try:
            for i in self.db[x]:
                print("%s %s %s" % (x, i[0], i[1]))
        except:
            print("Error: no such knowledge on the database")

    def connect(self, concept, relation, fact):
        try:
            if([relation, fact] in (self.db)[concept]):
                print("It is already in the database")
            else:
                (self.db)[concept].append([relation, fact])
        except:
            (self.db)[concept]=[[relation, fact]]

    def delete_connection(concept, relation, fact):
        try:
            list=(self.db)[concept]
            n=list.index([relation, fact])
            del list[n]
            (self.db)[concept]=list
        except:
            print("Error: no such knowledge on the database")

    def delete_concept(concept):
        try:
            del (self.db)[concept]
        except:
            print("no such concept")
            
    def save(self, filename):
        f = open(filename, 'wb')
        pickle.dump(self.db, f)
        f.close()

    def load(self, filename):
        f = open(filename, 'rb')
        self.db = pickle.load(f)
        f.close()

    def show_all(self):
        if(len(self.db)<=1000):
            print(self.db)
        else:
            print("the database has %d knowledge" % len(self.db))

    def summary(self):
        print("number of knowledge: %d" % len(self.db))
        
if __name__=="__main__":
    know=relationship()

    know.connect("clock", "is", "a mechanical or electrical device for measuring time")

    know.save("knowledge.know2")
