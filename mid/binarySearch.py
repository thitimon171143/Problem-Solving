sequential_list = [1,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
def seq(value):
    found = False
    for i in range(len(sequential_list)):
        print(i,sequential_list[i])
        if sequential_list[i] == value:
            found = True
            break
    return found,i

print(seq(37))