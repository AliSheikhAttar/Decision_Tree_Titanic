from nodeclass import *

class Pat:
    def children(parent):

        list1 = []
        list2 = []
        list3 = []
        for i in range(len(parent.exs)):
            if(parent.exs[i][4]=="None"):
                list1.append(parent.exs[i])
            elif(parent.exs[i][4]=="Some"):
                list2.append(parent.exs[i])
            elif(parent.exs[i][4]=="Full"):
                list3.append(parent.exs[i])
        return [node(None, list1, None, parent), node(None, list2, None, parent), node(None, list3, None, parent)] 