num1 = 42 #variable declaration
num2 = 2.3 #variable declaration
boolean = True #Data type boolean
string = 'Hello World' #Data type String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #
fruit = ('blueberry', 'strawberry', 'banana') #
print(type(fruit)) #Print all of fruit
print(pizza_toppings[1]) #print index 1 of pizza toppings
pizza_toppings.append('Mushrooms') #Add mushrooms to pizza toppings
print(person['name']) #prints John
person['name'] = 'George' #Variable declaration
person['eye_color'] = 'blue' #Variable declarartion 
print(fruit[2]) #print index 2 of fruit

if num1 > 45:
    print("It's greater") #conditional If 
else:
    print("It's lower") #conditional else

if len(string) < 5: 
    print("It's a short word!") #if length of string is less than 5. Print 
elif len(string) > 15:
    print("It's a long word!") #else if length of string is greater than 15. Print
else:
    print("Just right!") #else Print

for x in range(5): #for loop that goes 0-4
    print(x)
for x in range(2,5): #for loop that goes 2-4
    print(x)
for x in range(2,10,3): #for loop that adds 3 each time it runs
    print(x)
x = 0
while(x < 5): #while loop
    print(x)
    x += 1

pizza_toppings.pop() #pop function
pizza_toppings.pop(1) #pop function. pops index 1 of pizza_topping

print(person) #print
person.pop('eye_color') #pop eye color
print(person) #print object person

for topping in pizza_toppings: #forloop checks all toppings for pepperoni, then checks all for olives
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times(): #function 
    for num in range(10): #for loop
        print('Hello') 

print_hello_ten_times() #function call

def print_hello_x_times(x): #function 
    for num in range(x): #forloop
        print('Hello') 

print_hello_x_times(4) #function call providing 4

def print_hello_x_or_ten_times(x = 10): #function 
    for num in range(x): #for loop
        print('Hello') 

print_hello_x_or_ten_times() #function call with no variable 
print_hello_x_or_ten_times(4) #function call with 4 as variable 


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