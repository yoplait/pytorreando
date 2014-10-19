import sys
f = lambda *args: sys.stdout.write(" ".join(map(str,args)))
f('hello', 10, 3.4)
