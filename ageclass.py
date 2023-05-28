from nodeclass import *
class age:
    def children(parent):

        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        for i in range(len(parent.exs)):
            if(parent.exs[i][3]!= ""):
                if(int(parent.exs[i][3])<20):
                    list1.append(parent.exs[i])
                elif(20<=int(parent.exs[i][3])<40):
                    list2.append(parent.exs[i])
                elif(40<=int(parent.exs[i][3])<60):
                    list3.append(parent.exs[i])
                elif(60<=int(parent.exs[i][3])<80):
                    list4.append(parent.exs[i])
                elif(80<=int(parent.exs[i][3])):
                    list5.append(parent.exs[i])

        return [node(None, list1, None, parent),
                node(None, list2, None, parent), 
                node(None, list3, None, parent), 
                node(None, list4, None, parent), 
                node(None, list5, None, parent)]

