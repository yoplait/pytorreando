def display_info(name, age, spouse, child1=None, child2=None,
  child3=None):
  print name, age, spouse, child1, child2, child3

display_info(*('bob',37), **{'spouse':'kim','child1':'burt'})
