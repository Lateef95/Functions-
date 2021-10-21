def greet ():
  return 'Hello Muhammed'

#=================================

'''
functions with parameters 
'''

def greet(name):
  '''
  Greets a person passed in as argument name; a name of a person to greet
  '''
  return f'hello {name}, Good morning'
  print(greet('Chipo'))


'''
Arbitrary parameters 
'''

def fruits(*names):
  '''
  Accepts unknown number of fruit name and prints each of them *name: list of fruits 
  '''
  #names are tuples 
  for fruit in names: 
    print (fruit)

fruits ('Banana', 'Apple', 'Pear', 'Grapes')

'''
Keyword parameters 
'''

def greet(name, msg):
  '''
  This function greets a person with a message name: person to greet
  msg: Message to greet with 
  '''

  return f'Hello {name}, {msg}'

  print(greet('Noah' 'Good morning'))
  print(greet(name='Chipo', msg='Good morning!'))


'''
Arbitray Keyword parameters 
'''

def person (**student): 
  print(type(student))
  print(student)
  for key in student:
    print(student[Key])

  person(fname= 'Muhammed', lname= 'Lateef', subject='Python')

  #Dictonairies are used for this function 

'''
Default parameters values
'''

def greet(name='David'):
  return f'hello {name}'

print(greet())
print(greet('Dayana'))

'''
Pass statement 
'''

def greet():
  pass 

'''
Recursion  
'''

def factorial_recursion(n):
  '''
  Multiply a given number by every number less than it doen to 1 in a factorial way
  e.g if (n) is 5 then calculate 5*4*3*2*1 = 120 
  '''

if n == 1:
  return True
else: 
  return n * factorial_recursive(n-1)

print (factorial_recursive(50))
