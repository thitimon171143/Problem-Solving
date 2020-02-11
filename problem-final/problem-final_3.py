Alist = ['A','B','C','D','E','F']
who = input('Input Start Person :')
number = int(input('Input number : '))

if who == 'A':
    for i in Alist:
        Alist.pop(number-1)
    print(Alist)