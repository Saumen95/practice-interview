shoplist = ['apple', 'banana', 'Grape', 'Orange']
print(len(shoplist))
shoplist.append('Rice')
print(shoplist)
shoplist.sort()
for item in shoplist:
   print len(item.split())
