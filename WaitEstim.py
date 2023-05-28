from nodeclass import *
class Est:
    def children(parent):

        list1 = []
        list2 = []
        list3 = []
        list4 = []
        for i in range(len(parent.exs)):
            if((parent.exs[i][9]) == "0-10"):
                list1.append(parent.exs[i])
            elif((parent.exs[i][9]) == "10-30"):
                list2.append(parent.exs[i])
            elif((parent.exs[i][9]) == "30-60"):
                list3.append(parent.exs[i])
            elif((parent.exs[i][9]) == ">60"):
                list4.append(parent.exs[i])
        return [node(None, list1, None, parent), 
                node(None, list2, None, parent), 
                node(None, list3, None, parent), 
                node(None, list4, None, parent)]
