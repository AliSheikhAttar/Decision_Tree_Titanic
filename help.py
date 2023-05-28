import pandas 
import numpy
import math  
import sys
# import pclass


csv_data = pandas.read_csv("titanic.csv")
csv_data = csv_data.fillna("")

x = csv_data.values

# print(len(x))
# for i in range(len(csv_data)):
#     if(int(csv_data.values[i,4])>=8):
#         print(i)

# print(numpy.argmax(x[:,5]))

# print(x[:,6])

# for i in range(len(x)):
#     if(x[i,6][0:2]=="PC"):
#         print(i)
# max = 0
# for t in x:
#     if(float(t[7])>max):
#         max = float(t[7])
#         print(t[7])
# print(max)

# min = sys.maxsize
# for t in x:
#     if(float(t[7])<min):
#         min = float(t[7])
#         print(t[7])
# print(min)

print(x[:,8])
# how many different
# list_differ = []
# for t in x:
#     if(t[8] not in list_differ):
#         list_differ.append(t[8])

# print(len(list_differ))        
# print(list_differ)
# list_differ = []

# for t in x:
#     if(t[8] !="" and t[8][0] not in list_differ ):
#         list_differ.append(t[8][0])

# print(len(list_differ))        
# print(list_differ)
# list_differ = []

# for t in x:
#     if(t[9] !="" and t[9] not in list_differ ):
#         list_differ.append(t[9])

# print(len(list_differ))        
# print(list_differ)
list_differ = [("S",0),("C",0),("Q",0)]
count_s = 0 
count_c = 0
count_q = 0
for t in x:
    if(t[9]=="S"):
        count_s +=1
    elif(t[9]=="C"):
        count_c +=1
    if(t[9]=="Q"):
        count_q +=1
list_differ = [("S",count_s),("C",count_c),("Q",count_q)]
print(list_differ)
