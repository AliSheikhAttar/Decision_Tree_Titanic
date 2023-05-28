from nodeclass import *
class pclass:
    def children(parent):

        list1 = []
        list2 = []
        list3 = []
        for i in range(len(parent.exs)):
            if(parent.exs[i][0]==1):
                list1.append(parent.exs[i])
            elif(parent.exs[i][0]==2):
                list2.append(parent.exs[i])
            elif(parent.exs[i][0]==3):
                list3.append(parent.exs[i])
        return [node(None, list1, None, parent), 
                node(None, list2, None, parent), 
                node(None, list3, None, parent)]
