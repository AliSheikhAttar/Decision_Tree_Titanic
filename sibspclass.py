from nodeclass import *
class sibps:
    def children(parent):

        list1 = []
        list2 = []
        list3 = []
        list4 = []
        for i in range(len(parent.exs)):
            if(int(parent.exs[i][4])<=2):
                list1.append(parent.exs[i])
            elif(2<int(parent.exs[i][4])<=4):
                list2.append(parent.exs[i])
            elif(4<int(parent.exs[i][4])<=6):
                list3.append(parent.exs[i])
            elif(6<int(parent.exs[i][4])<=8):
                list4.append(parent.exs[i])
        return [node(None, list1, None, parent), 
                node(None, list2, None, parent), 
                node(None, list3, None, parent), 
                node(None, list4, None, parent)]
