import exceptions
dir(exceptions)

try:
  a = raw_input("Enter a number: ")
  b = raw_input("Enter a number: ")

  #print "Division result is : %f" % a / b
  print "Division result is : ", float(a) / float(b)

except ValueError:
  print 'An improoper cazurro way to put information'
