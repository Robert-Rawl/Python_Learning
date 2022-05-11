num1 = 42 #variable declaration, number initialized
num2 = 2.3#variable decleration, decimal initialized
boolean = True#variable declaration, boolean intialized
string = 'Hello World'#variable decloration, string initialized

#variable decloration, list initialized
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#variable decloration, dictionary initialized
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
#variable decloration, tuple initialized
fruit = ('blueberry', 'strawberry', 'banana')
#print to console, type check
print(type(fruit))
#print to console, list access value
print(pizza_toppings[1])

#list add value
pizza_toppings.append('Mushrooms')

#print console, dictionary access value
print(person['name'])

#Dictionary change value
person['name'] = 'George'
#Dictionary change value
person['eye_color'] = 'blue'

#print to console, tuple access data
print(fruit[2])


#conditional if , if evaluation, print to colsole, conditional else, print to console
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

#conditional if ~ elif ~ else, print to console

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

#for loop starts 0 goes up until 5    

for x in range(5):
    print(x)

#for loop starts at 2 and goes up until 5
for x in range(2,5):
    print(x)

#for loop starts at 2 and goes up until 10, increments of 3
for x in range(2,10,3):
    print(x)

#while loop, variable decleration  
x = 0
#printing to console
while(x < 5):
    print(x)
#incrementing x    
    x += 1


#list delete value at end
pizza_toppings.pop()
#list delete value at index
pizza_toppings.pop(1)

#print to console of Dictionary
print(person)
#Dictionary delete value
person.pop('eye_color')
#print to console of Dictionary
print(person)


#for loop through a list
for topping in pizza_toppings:

#conditional if    
    if topping == 'Pepperoni':
        continue
#print to console
    print('After 1st if statement')
#conditional if    
    if topping == 'Olives':
#stops the loop        
        break



#function decleration
def print_hello_ten_times():

#for loop that starts at 0 and goes up until 10    
    for num in range(10):
#print to console        
        print('Hello')
#function call
print_hello_ten_times()

#function decleration
def print_hello_x_times(x):
    #for loop up until a given number
    for num in range(x):
        #print to console
        print('Hello')
#function call with an argument of 4
print_hello_x_times(4)
#funtion decleration with a default parameter
def print_hello_x_or_ten_times(x = 10):
    #for loop until x
    for num in range(x):
        #print to console
        print('Hello')
#function call
print_hello_x_or_ten_times()
#function call with an argument of 4
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)