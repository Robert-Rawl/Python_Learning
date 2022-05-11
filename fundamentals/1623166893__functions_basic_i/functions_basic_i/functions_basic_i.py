#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#number_of_food_groups will print a value of 5


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# will print a value of 5 and  number of day in a week silicon or triangle  is undefined and will cause and error


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# will print 5, return 10 wont happen becasue return 5 is first and exits the function.



#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#number_of_finger() wiil print 5, print 10 will not exist because the return statement exits the function.


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#number_of_great_lakes() will print 5 and none because there is no stored value in the function and x is undefined.


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#add() will print 3, 5, 8


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#concatenate(b,c) will print 25 because it concatenating two string values.


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#function will print 100, then return and print 10


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#function will print 7,14,21


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#addition(b,c) will print 8


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# 500,300,500


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#500,300,500


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#500,300,300,


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# foo()will print 1, bar will print 3 then 2


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#1,3,5,10