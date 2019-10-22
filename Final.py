# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:07:26 2019

@author: angel
"""
import random
from sklearn.neighbors import KNeighborsClassifier
words=["age","raju","chacha","bhagat","angel","tanna","aisha","madan","papa","ana","pana","lana","lampat","zam","sal","val"]
convert={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}

list=[]
for t in words:
    p=[0,0,0,0,0,0,0,0,0,0]
    i=0
    for k in t:
        p[i]=convert[k]
        i=i+1
    list.append(p)
p=[]
p=list

clf = KNeighborsClassifier()
output=[1,1,1,0,1,0,0,0,1,1,0,0,0,1,1,1,0,1,0,0,0,1,1,0,0,0] 
output=output[:16]
clf.fit(p,output)
test=[[1,7,5,0,0,0,0,0,0,0]]
print(clf.predict(test))
centroid=[[16,16,16,0,0,0,0,0,0,0]]
centroid1 = []
for _ in range(10):
    centroid1.append(random.randint(1,26))
print("Centroid is: ",[centroid1])
l = []
for i in centroid1:
    l.append(chr(i + 96))
print("Corresponding characters are: ",*l)
print("for centroid",clf.predict([centroid1]))
