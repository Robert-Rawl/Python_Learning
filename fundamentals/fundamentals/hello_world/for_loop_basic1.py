#1.Basic
for x in range(151):
    print(x)

#2.Multiples of 5
for x in range(5,1001,5):
    print(x)

#3.Counting the Dojo Way
for x in range(1,101):
    if x % 10 == 0:
        print("coding dojo")
    elif x % 5 == 0:
        print("coding")
    else:
        print(x)

#4Whoa!
sum = 0
for x in range(1,500001,2):
    sum += x
print(sum)

#5 Countdown by 4's

for x in range(2018,0,-4):
    print(x)

#6 Flexible Counter

lowNum = 2
highNum = 9
mult = 3

for x in range(lowNum, highNum + 1):
    if x % mult == 0:
        print(x)


