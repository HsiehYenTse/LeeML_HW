#HW0-Q1
list1 = []
list2 = []
ch = ''
f = open('test1.txt', 'r')
for i in f.read():
    list1.append(i)
#print(len(list))
#print(list)
for j in list1:
    if j == ' ' or j == '\n':
        list2.append(ch)
        ch = ''
    else:
        ch += j
#print(list2)
#print(list2.count('NTU'))
list3 = []
list3.append(list2[0])
for m in list2:
    if(list3.count(m) == 0):
        list3.append(m)
#print(list3)

num = 0;
for i in list3:
    print(i, num, list2.count(i))
    num += 1


