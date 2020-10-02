import collections

shoplist = ['apple', 'banana', 'Grape', 'Orange']
print(len(shoplist)) # length of a list
shoplist.append('Rice')
print(shoplist) # print list after adding
shoplist.sort()
 # print the frequency of items in a list
for item in shoplist:
    print(len(item)) # print length of each items in a list

shoplist.insert(2, 'bedana') # insert at index
print(shoplist)
word_count = collections.Counter(shoplist)
print(word_count)