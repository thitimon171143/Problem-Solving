listA = [8,12,24,3,16,10,41]
listB = ['C','B','F','K','Y','Z','G']
listC = []

sum_B = 0
for i in listB:
    sum_B = sum_B + ord(i)

B_ascii = []
for s in listB:
    ascii_B = ord(s)
    B_ascii.append(ascii_B)
print('listB to ASCII :',B_ascii)

for k,l in listA,B_ascii:
    print(k,l)
    
'''print(listC)'''
print('listA :',sum(listA))
print('listB :',sum_B)
'''print(sum(listC))'''