def my_func(x):
  global y
  x = 5
  y = 6
  print x,y

x=10
y=20
print x,y
my_func(x)
print x,y
