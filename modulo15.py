import sys
myList = [None] * 10
f=lambda lst,pos,val : lst.__setitem__(pos,val)
f(myList,0,3.4)
f(myList,1,12)
f(myList,2,323)
f(myList,3,444)
for valor in myList:
  print(valor)
