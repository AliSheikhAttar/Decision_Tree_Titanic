from nodeclass import *
class fare:
    def children(parent):

        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        for i in range(len(parent.exs)):
            if(parent.exs[i][7] != ""):
                if(float(parent.exs[i][7])<=120):
                    list1.append(parent.exs[i])
                elif(120<float(parent.exs[i][7])<=240):
                    list2.append(parent.exs[i])
                elif(240<float(parent.exs[i][7])<=360):
                    list3.append(parent.exs[i])
                elif(360<float(parent.exs[i][7])<=480):
                    list4.append(parent.exs[i])
                elif(480<float(parent.exs[i][7])):
                    list5.append(parent.exs[i])
        return [node(None, list1, None, parent), 
                node(None, list2, None, parent), 
                node(None, list3, None, parent), 
                node(None, list4, None, parent), 
                node(None, list5, None, parent)]

