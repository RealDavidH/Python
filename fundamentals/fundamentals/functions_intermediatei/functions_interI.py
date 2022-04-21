# Update values in dictionaries and lists
from curses import keyname


x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x)
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)

#Iterate Through a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def dict_students(student_dict):
    for i in range(0, len(student_dict)):
        print(f"First name - {student_dict[i]['first_name']}, Last name - {student_dict[i]['last_name']}")

dict_students(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)

#Get Values From a List of Dictionaries
def interateDictionary(key_name, students):
    print(key_name)
    for i in range(0, len(students)):
        print(students[i][str(key_name)])
interateDictionary('first_name', students)
interateDictionary('last_name', students)

#Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def list_Values():
    for i in dojo:
        print(f"{i}:")
        temp = dojo[i]
        for j in range(0, len(temp)):
            print(temp[j])
list_Values()


