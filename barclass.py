from nodeclass import *
class Bar:
    def children(parent):

        list1 = []
        list2 = []
        for i in range(len(parent.exs)):
            if(parent.exs[i][1]=="Yes"):
                list1.append(parent.exs[i])
            elif(parent.exs[i][1]=="No"):
                list2.append(parent.exs[i])
        return [node(None, list1, None, parent), 
                node(None, list2, None, parent)]
