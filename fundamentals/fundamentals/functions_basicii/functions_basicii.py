def countdown(Highnum):
    list = []
    for i in range (Highnum, 0, -1):
        list.append(i)
    return list
print(countdown(5))

def print_and_return(list):
    print(list[0])
    return list[len(list)-1]
print(print_and_return([1,4]))

def first_length(list):
    return list[0] + len(list)
print(first_length([1,2,3,4,5]))

def values_great_second(list):
    templist = []
    numsGreaterThan = 0
    if len(list) < 2:
        return False
    for i in range(0, len(list)):
        if list[i] > list[1]:
            numsGreaterThan += 1
            templist.append(list[i])
    return templist, numsGreaterThan 
print(values_great_second([5,2,3,2,1,4]))

def size_value(size, value):
    templist = []
    for i in range(0, size):
        templist.append(value)
    return templist
print(size_value(3,5))