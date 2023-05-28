from nodeclass import *

class parch:
    def children(parent):

        list1 = []
        list2 = []
        list3 = []
        for i in range(len(parent.exs)):
            if(int(parent.exs[i][5])<=3):
                list1.append(parent.exs[i])
            elif(3<int(parent.exs[i][5])<=6):
                list2.append(parent.exs[i])
            elif(6<int(parent.exs[i][5])<=9):
                list3.append(parent.exs[i])
        return [node(None, list1, None, parent), 
                node(None, list2, None, parent), 
                node(None, list3, None, parent)]
