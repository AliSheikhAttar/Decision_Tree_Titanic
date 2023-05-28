from nodeclass import *
class ticket:
    def children(parent):

        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        list7 = []
        list8 = []

        for i in range(len(parent.exs)):
            if(parent.exs[i][6][0:2]=="PC"):
                list1.append(parent.exs[i])
            else:
                if(parent.exs[i][6]=="24160"):
                    list2.append(parent.exs[i])
                elif(parent.exs[i][6]=="113781"):
                    list3.append(parent.exs[i])
                elif(parent.exs[i][6]=="19924"):
                    list4.append(parent.exs[i])
                elif(parent.exs[i][6]=="19952"):
                    list5.append(parent.exs[i])
                elif(parent.exs[i][6]=="13502"):
                    list6.append(parent.exs[i])
                elif(parent.exs[i][6]=="112050"):
                    list7.append(parent.exs[i])
                elif(parent.exs[i][6]=="11769"):
                    list8.append(parent.exs[i])



        return [node(None, list1, None, parent), 
                node(None, list2, None, parent),
                node(None, list3, None, parent),
                node(None, list4, None, parent),
                node(None, list5, None, parent),
                node(None, list6, None, parent),
                node(None, list7, None, parent),
                node(None, list8, None, parent)]
