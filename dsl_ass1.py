# -*- coding: utf-8 -*-
"""dsl-ass1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Zx81EH0-1k6BFlkkuFmxKPJi5Azxb10V
"""

''' In Second year Computer Engineering class of M students, set A of students play cricket and
    set B of students play badminton. Write C/C++ program to find and display-
    i. Set of students who play either cricket or badminton or both
    ii. Set of students who play both cricket and badminton
    iii. Set of students who play only cricket
    iv. Set of students who play only badminton
    v. Number of students who play neither cricket nor badminton '''

print ("-----------DSL Ass1----------")
grpA=["Shraddha","Kavita","Poonam"] #Cricket
grpB=["Shraddha","Poonam","Isha"]#badminton
grpC=["Shraddha","Gauri","Kirti"]#football
la=len(grpA)
lb=len(grpB)
lc=len(grpC)

#part A
resultlista=[]
print("List of students who play both cricket and badminton")
for i in range(la):
    for j in range(lb):
        if(grpA[i]==grpB[j]):
            resultlista.append(grpA[i])
print(resultlista)

#part B
resultlistb=[]
print("List of students who play either cricket or badminton but not both ")
for i in range(lb):
    for j in range(la):
        if(grpB[i]==grpA[j]):
            flag=1
    if(flag==0):
        resultlistb.append(grpB[i])
    flag=0;

for i in range(la):
    for j in range(lb):
        if(grpA[i]==grpB[j]):
            flag=1;
    if(flag==0):
        resultlistb.append(grpA[i])
    flag=0;

print(resultlistb)

#part c
resultlistc=[]
print("List of students who play neither cricket nor badminton")
for i in range(lc):
    for j in range(la):
        if(grpC[i]==grpA[j]):
            flag=1;
            break;
        flag=0;
    for k in range(lb):
        if(grpC[i]==grpB[k]):
            flag=1;
            break;
        flag=0;
    if(flag==0):
        resultlistc.append(grpC[i])
    flag=0;
print(resultlistc)

#part d
print("List of students who play cricket and football but not badminton")

resultlistd=[]
for i in range(la):
    for j in range(lc):
        if(grpA[i]==grpC[j]):
            resultlistd.append(grpA[i])
#print(resultlistd)
ld=len(resultlistd)
resultliste=[]
for k in range(lb):
    for var in range(ld):
        if(grpB[k]==resultlistd[var]):
            flag=1;
    if(flag==0):
        resultliste.append(resultlistd)
print(resultliste)