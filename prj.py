import pandas 
import numpy as np
import math  
import sys
from nodeclass import *
from alternativeclass import *
from barclass import *
from frisatclass import *
from hungryclass import *
from patronsclass import *
from rainingclass import *
from reservationclass import *
from WaitEstim import *


csv_data = pandas.read_csv("resturant.csv")





def CalculateSurviveds(node):
    y = len(list(filter(lambda x: x[-1]=="Yes", node.exs)))
    n = len(node.exs)-y
    return y,n




def entropy(children):
    result = 0
    totalcount = 0
    for j in range(len(children)):
        totalcount += len(children[j].exs)
    for i in range(len(children)):
        y,n = CalculateSurviveds(children[i])
        if(y==0 or n==0):
            result +=0
            continue
        result += (y/(y+n))*(math.log2((n+y)/y))*(len(children[i].exs)/totalcount)
    return result
    
def entropy1(children):
    result = 0
    totalcount = 0
    for j in range(len(children)):
        totalcount += len(children[j].exs)
    for i in range(len(children)):
        y,n = CalculateSurviveds(children[i])
        if(y==0):
            result +=0
            continue
        result += (y/(y+n))*(math.log2((n+y)/y))*(len(children[i].exs)/totalcount)
    return result
    


def gini_index(children):
    result = 0
    totalcount = 0
    for j in range(len(children)):
        totalcount += len(children[j].exs)
    for i in range(len(children)):
        y,n = CalculateSurviveds(children[i])
        if(y==0):
            result +=0
            continue
        result += ((y/(y+n))*(1-(y/(y+n))) + (n/(y+n))*(1-(n/(y+n))))*(len(children[i].exs)/totalcount)
    return result







def whichQuestion(node, Questions, ent_gini):
    min_etp = sys.maxsize
    question = None
    for q in Questions:
        if(entropy(q.children(node))<=min_etp):
            question = q
            min_etp = ent_gini(q.children(node))


    node.attribute = question
    node.children = question.children(node)
    return node


    
def survived(node):
    y,n = CalculateSurviveds(node)
    if(y>n):
        return True
    return False

def NoNeed2Question(node, accuracy):
    y,n = CalculateSurviveds(node)
    if(y/(y+n)>=accuracy or n/(y+n)>=accuracy):
        return True
    return False


# def cut(node):
#     if(node.children != None):
#         for child in node.children:
#             harraas(child)
#     else:
#         if(node.parent != None):
#             return node
#         if(entropy([node.parent]) - entropy(node.parent.children) < 0.009):
#             node.parent.children = None
#         node.parent.state = survived(node.parent)


def tree(node , Questions, ent_gini, accuracy):
    if(len(node.exs)==0):
        node.state = survived(node.parent)
        return None
    elif(len(Questions)==0):
        node.state = survived(node)
        return None
    elif(NoNeed2Question(node, accuracy)):
        node.state = survived(node)
        return None
    node = whichQuestion(node, Questions,ent_gini)
    for x in node.children:
        tree(x, list(filter(lambda x: x!=node.attribute, Questions)),ent_gini , accuracy)
    return node



def printree(node):
    if(node.state!=None):
        print(node.state)
        return None
    else:
        print(node.attribute)
        for child in node.children:
            printree(child)




def machine(treenode, person):
    lists = treenode.attribute.children(node(None, [person], None, None))
    index = 0
    for i in range(len(lists)):
        if(len(lists[i].exs)!= 0):
            index = i
            break
    if(treenode.children[index].state== None):
        return machine(treenode.children[index], person)
    else:
        return treenode.children[index].state
    

        
def trainTest(data, porpotion):
    total = len(data)
    index = int(porpotion*total)
    return [data[:index] , data[index::]]




Questions = [Alt, Bar, Fri, Hun, Pat, Rain, Res, Est]

porpotion = 0.8
trainNtest = trainTest(csv_data.values.tolist(), porpotion)

train_data = trainNtest[0]
test_data = trainNtest[1]



root = node(None,train_data,None,None)



root = tree(root, Questions, entropy, 0.9)

# root = cut(root)

# printree(root)


person = csv_data.values[0]
alive = None
if(person[-1]=="Yes"):
    alive = True
else:
    alive = False
print(f"Answer : {machine(root,person)}\nthe actual was : {alive}")





def accuracy(test_data, root):
    total = len(test_data)
    trues = 0
    for data in test_data:
        state = None
        if(machine(root, data) == True):
            state = "Yes"
        else:
            state = "No"
        if(state == data[-1]):
            trues+=1
    return trues/total


print(f"accuracy : {round(accuracy(train_data, root)*100,3)} % ")

