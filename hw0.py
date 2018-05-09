list = []
list2 = []
ch = '';
f = open('test1.txt', 'r')
for i in f.read():
    list.append(i)
#print(len(list))
#print(list)
for j in list:
    if j == ' ' or j == '\n':
        list2.append(ch)
        ch = ''
    else:
        ch += j
#print(list2)
print(list2.count('NTU'))
#add this line

