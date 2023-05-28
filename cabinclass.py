from nodeclass import *
import numpy as np
class cabin:
    def children(parent: node):

        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        for i in range(len(parent.exs)):
            if(parent.exs[i][8] !=""): 
                if(parent.exs[i][8][0] == "A"):
                    list1.append(parent.exs[i])
                elif(parent.exs[i][8][0] == "B"):
                    list2.append(parent.exs[i])
                elif(parent.exs[i][8][0] == "C"):
                    list3.append(parent.exs[i])
                elif(parent.exs[i][8][0] == "D"):
                    list4.append(parent.exs[i])
                elif(parent.exs[i][8][0] == "E"):
                    list5.append(parent.exs[i])
                else:
                    list6.append(parent.exs[i])


        return [node(None, list1, None, parent), 
                node(None, list2, None, parent), 
                node(None, list3, None, parent), 
                node(None, list4, None, parent),
                node(None, list5, None, parent),
                node(None, list6, None, parent)]

