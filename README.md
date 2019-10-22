# KNN-
Implement Knn on set of words.


EXPLANATION OF PROGRAM:-
words=["age","raju","chacha","bhagat","angel","tanna","aisha","madan","papa","ana","pana","lana","lampat","zam","sal","val"]
above is list of words that is considered as data set on which knn classifier works
clf = KNeighborsClassifier()
this is a inbuilt function which classify centroid where it belongs that is class 1 or class 0 on the basis of similarity from data set


Centroid is:  [[22, 21, 19, 5, 10, 2, 16, 20, 21, 16]]
Corresponding characters are:  v u s e j b p t u p// on the basis of above numeric values 1=a to z=26 characters are printed 
centroid is randomly selected using random library in python
for centroid [1]// for above centroid it belongs to class 1

EXPLANATION OF KNN ALGORITHM:-
K- Nearest Neighbor, popular as K-Nearest Neighbor (KNN), is an algorithm that helps to assess the properties of a new variable with the help of the properties of existing variables
KNN is applicable in classification as well as regression predictive problems.It simply takes the voting of majority of variables and accordingly treats new variables.
basically it takes one input and classify it what type of class to which it belongs by learning from exixting data.


 
