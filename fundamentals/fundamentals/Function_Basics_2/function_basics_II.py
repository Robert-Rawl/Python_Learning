#1.Countdown

def countdown(num):
    array = []
    for i in range(num,-1,-1):
        array.append(i)
    return array

print(countdown(5))

#2. Print and Return 

def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([1,2]))

#3
def first_plus_length(list):
    return list[0] + len(list)
    
print(first_plus_length([10,9,8,7,6,5]))

#4
def value_greater_than_second(list):
    if len(list) < 2:
        return False
    newList = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            newList.append(list[i])
    print (len(newList))
    return newList

print(value_greater_than_second([5,2,3,2,1,4]))
print(value_greater_than_second([3]))

#5
def length_value(size,value):
    output = []
    for i in range(0,size):
        output.append(value)
    return output
    
print(length_value(9,7))
print(length_value(6,1)) 