def arg_passing(tup, lst):
  tup *=3
  lst *=2
  print tup,lst

tup=(1,2,3)
lst=[4,5,6]

arg_passing(tup, lst)

print tup,lst
