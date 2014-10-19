def total_footage(kitchen,masterbedroom,*otherbedroom,**extra):
    print 'hola'
    total = 0
    total += kitchen[0]*kitchen[1]
    total += masterbedroom[0]*masterbedroom[1]
    for bed in otherbedroom:
      total+=bed[0]*bed[1]
    print '1'
    for room in extra.keys():
      total+=extra[room][0]*extra[room][1]
      print 'esta es la habita', room
    print '2'
    return total



print 'executing'
total = total_footage([10,10],[12,14],
  [10,11],[10,12],[10,11],
  dining=[11,12],utility=[9,8],bathroom=[10,6])
print 'total sq feet =', total
