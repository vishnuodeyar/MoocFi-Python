def no_shouting(mylist: list):
  new_list = []
  for i in mylist:
    if i.isupper():
      print("")
    else:
      new_list.append(i)
  return new_list

mylist = ['HELLO', 'WORLD', 'PYTHON', 'test', 'Now']
print(no_shouting(mylist))
  