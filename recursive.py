num = int(input('Input Number : '))
def fac(num) :
    if num > 1 :
        factorial = num*fac(num-1)
    else :
        factorial = 1
    return factorial

print(fac(num))