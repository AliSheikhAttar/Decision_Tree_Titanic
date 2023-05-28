from nodeclass import *

class embarked:
    def children(parent):

        list1 = []
        list2 = []
        list3 = []
        for i in range(len(parent.exs)):
            if(parent.exs[i][9]=="S"):
                list1.append(parent.exs[i])
            elif(parent.exs[i][9]=="C"):
                list2.append(parent.exs[i])
            elif(parent.exs[i][9]=="Q"):
                list3.append(parent.exs[i])
        return [node(None, list1, None, parent), node(None, list2, None, parent), node(None, list3, None, parent)]


        