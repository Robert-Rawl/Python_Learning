x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)
#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
students[0]['last_name'] = 'Bryant'
print(students[0]['last_name'])
#Change the last_name of the first student from 'Jordan' to 'Bryant'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'][0])
#In the sports_directory, change 'Messi' to 'Andres'
z[0]['y'] = 30

print(z)
#Change the value 20 in z to 30

#2
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterate_dictionary(list):
    for i in range(0, len(list)):
        output = ""
        for key,val in list[i].items():
            output += f" {key} ~ {val},"
        print(output)
        
iterate_dictionary(students)

#3.Get Values From A list of Dictionaries

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary2(key_name, some_list):
    for i in range(0,len(some_list)):
        for key,val in some_list[i].items():
            if key == key_name:
                print(val)

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


#4 Iterate Through a Dictionary with List Values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key,val in some_dict.items():
        print('')
        print(f"{len(val)} {key.upper()}")
        for i in range(0,len(val)):
            print(val[i])

printInfo(dojo)
