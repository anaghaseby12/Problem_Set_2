#!/usr/bin/env python
# coding: utf-8

# # PROBLEM SET 2
# 

# # Question 1
# 

# Consider the following Python module: a = 0 def b(): global a a = c(a) def c(a): return a + 2 After importing the module into the interpreter, you execute:
# 
# b() b() b() a
# 
# ? What value is displayed when the last expression (a) is evaluated? Explain your answer by indicating what happens in every executed statement.

# In[2]:


a = 0 #intializing a local variable 'a' to 0

def b(): #defining a function b()
    global a #converting the local variable to a global variable
    a = c(a)# calling the function to provide the value of a
    
def c(a): #defning a function c()
    return a+2 #\it returns a value of a+2 each time it is called

b() #function call
b() #function call
b() #function call; each time we called the function b the value of 'a' was increased by 2; We have called 'a' 3 times and thus Value of 'a'= 6;
a #prints the value of a


# # Question 2

# Function fileLength(), given to you, takes the name of a file as input and returns the length of the file:
# 
# fileLength('midterm.py')
# 
# 284
# 
# fileLength('idterm.py')
# 
# Traceback (most recent call last): File "<pyshell#34>", line 1, in fileLength('idterm.py') File "/Users/me/midterm.py", line 3, in fileLength infile = open(filename) FileNotFoundError: [Errno 2] No such file or directory: 'idterm.py' As shown above, if the file cannot be found by the interpreter or if it cannot be read as a text file, an exception will be raised. Modify function fileLength() so that a friendly message is printed instead:
# 
# fileLength('midterm.py')
# 
# 358
# 
# fileLength('idterm.py')
# 
# File idterm.py not found.

# In[41]:


def fileLength(filename):
    try:
        with open(filename, 'r') as file:
            file_data = file.read()
            length_of_file = len(file_data)
        return length_of_file
    except FileNotFoundError:
        print("File", filename, "not found.")


# In[42]:


fileLength('filename')


# In[43]:


fileLength("x3c.html")


# # QUESTION 3
# 

# Write a class named Marsupial that can be used as shown below:
# 
# m = Marsupial() m.put_in_pouch('doll') m.put_in_pouch('firetruck') m.put_in_pouch('kitten') m.pouch_contents()
# 
# ['doll', 'firetruck', 'kitten']

# In[44]:


class Marsupial:
    List = []  
    
    def put_in_pouch(self,content): 
       self.List.append(content) 
        
        
    def pouch_contents(self): 
        return m.List

m = Marsupial() 
m.put_in_pouch("doll") 
m.put_in_pouch("firetruck") 
m.put_in_pouch("kitten") 
m.pouch_contents() 


# Now write a class named Kangaroo as a subclass of Marsupial that inherits all the attributes of Marsupial and also: a. extends the Marsupial init constructor to take, as input, the coordinates x and y of the Kangaroo object, b. supports method jump that takes number values dx and dy as input and moves the kangaroo by dx units along the x-axis and by dy units along the yaxis, and c. overloads the str operator so it behaves as shown below.
# 
# k = Kangaroo(0,0) print(k)
# 
# I am a Kangaroo located at coordinates (0,0)
# 
# k.put_in_pouch('doll') k.put_in_pouch('firetruck') k.put_in_pouch('kitten') k.pouch_contents()
# 
# ['doll', 'firetruck', 'kitten']
# 
# k.jump(1,0) k.jump(1,0) k.jump(1,0) print(k)
# 
# I am a Kangaroo located at coordinates (3,0)

# In[21]:


class Kangaroo(Marsupial):

    def __init__(self,x,y):
        self.new_list = []
        self.new_list.clear ()
        self.x = x
        self.y = y
        
    def  __str__(self):
         return ("I am a Kangaroo located at coordinates ("+str(self.x)+","+str(self.y)+")")

    def jump(self,dx,dy):
        self.x = self.x + dx
        self.y = self.y + dy
    
        
k = Kangaroo(0,0)
print(k)
k.put_in_pouch('doll')
k.put_in_pouch('firetruck')
k.put_in_pouch('kitten')
print(k.pouch_contents())
k.jump(1,0)
k.jump(1,0)
k.jump(1,0)
print(k)


# # Question 4

# Write function collatz() that takes a positive integer x as input and prints the Collatz sequence starting at x. A Collatz sequence is obtained by repeatedly applying this rule to the previous number x in the sequence: x = { 𝑥/2 𝑖𝑓 𝑥 𝑖𝑠 𝑒𝑣𝑒𝑛 3𝑥 + 1 𝑖𝑓 𝑥 𝑖𝑠 𝑜𝑑𝑑 Your function should stop when the sequence gets to number 1. Your implementation must be recursive, without any loops.

# In[22]:


def collatz(n): # define a function collatz() to print the collatz sequence
    if(n == 1):
        print(1)
        return
    print(int(n))
    
    if(n % 2 == 0):
        n = n / 2
    else:
        n = n * 3 + 1
        
    return (collatz(n))
collatz(1)


# In[23]:


collatz(10)


# # QUESTION 5

# Write a recursive method binary() that takes a non-negative integer n and prints the binary representation of integer n.

# In[24]:


def binary(input): 
    if input<0: 
        return ("Enter postive integer")
    
    elif input >=1: 
        return ((10*binary(int(input/2))) + (input%2))
        
    else: 
        return 0
binary(0)


# In[25]:


binary(1)


# In[26]:


binary(3)


# # QUESTION 8

# Write SQL queries on the below database table that return: a) All the temperature data. b) All the cities, but without repetition. c) All the records for India. d) All the Fall records.

# In[27]:


import sqlite3
conn = sqlite3.connect('weather3.db')
c = conn.cursor()
c.execute('''CREATE TABLE weather(City TEXT,Country TEXT,Season TEXT,Temperature REAL,Rainfall REAL)''')
data = [('Mumbai', 'India', 'Winter', 24.8, 5.9),
                ('Mumbai', 'India', 'Spring', 28.4, 16.2),
                ('Mumbai', 'India', 'Summer', 27.9, 1549.4),
                ('Mumbai', 'India', 'Fall', 27.6, 346.0),
                ('London', 'United Kingdom', 'Winter', 4.2, 207.7),
                ('London', 'United Kingdom', 'Spring', 8.3, 169.6),
                ('London', 'United Kingdom', 'Summer', 15.7, 157.0),
                ('London', 'United Kingdom', 'Fall', 10.4, 218.5),
                ('Cairo', 'Egypt', 'Winter', 13.6, 16.5),
                ('Cairo', 'Egypt', 'Spring', 20.7, 6.5),
                ('Cairo', 'Egypt', 'Summer', 27.7, 0.1),
                ('Cairo', 'Egypt', 'Fall', 22.2, 4.5)]
c.executemany('INSERT INTO weather VALUES (?, ?, ?, ?, ?)', data)
conn.commit()
conn.close()


# In[29]:


import sqlite3
conn = sqlite3.connect('weather3.db')
c = conn.cursor()
c.execute('SELECT Temperature FROM weather')
temperature_data = c.fetchall()
print(temperature_data)


# In[30]:


c.execute("SELECT * FROM weather WHERE Country = 'India'")
india_records = c.fetchall()
print(india_records)


# In[31]:


c.execute("SELECT * FROM weather WHERE Season = 'Fall'")
fall_records = c.fetchall()
print(fall_records)


# In[32]:


c.execute("SELECT City, Country, Season FROM weather WHERE Rainfall BETWEEN 200 AND 400 GROUP BY City, Country, Season")
rainfall_records = c.fetchall()
print(rainfall_records)


# In[33]:


c.execute("SELECT City, Country FROM weather WHERE Season = 'Fall' GROUP BY City, Country HAVING AVG(Temperature) > 20 ORDER BY AVG(Temperature) ASC")
fall_temp_records = c.fetchall()
print(fall_temp_records)


# In[34]:


c.execute("SELECT SUM(Rainfall) AS Total_Rainfall FROM weather WHERE City = 'Cairo'")
cairo_rainfall = c.fetchone()[0]
print(cairo_rainfall)


# In[35]:


c.execute("SELECT Season, SUM(Rainfall) AS Total_Rainfall FROM weather GROUP BY Season")
season_rainfall = c.fetchall()
print(season_rainfall)


# # Question 9

# Suppose list words is defined as follows: words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'] Write list comprehension expressions that use list words and generate the following lists:
# a) ['THE', 'QUICK', 'BROWN', 'FOX', 'JUMPS', 'OVER', 'THE',
# 'LAZY', 'DOG']
# b) ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the',
# 'lazy', 'dog']
# c) [3, 5, 5, 3, 5, 4, 3, 4, 3] (the list of lengths of words in list
# words).
# d) [['THE', 'the', 3], ['QUICK', 'quick', 5], ['BROWN',
# 'brown', 5], ['FOX', 'fox', 3], ['JUMPS', 'jumps', 5],
# ['OVER', 'over', 4], ['THE', 'the', 3], ['LAZY', 'lazy',
# 4], ['DOG', 'dog', 3]] (the list containing a list for every word of list
# words, where each list contains the word in uppercase and lowercase and the
# length of the word.)
# e) ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the',
# 'lazy', 'dog'] (the list of words in list words containing 4 or more
# characters.)

# In[36]:


words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
print([word.upper() for word in words])


# In[37]:


print([word.lower() for word in words])


# In[38]:


print([len(word) for word in words])


# In[39]:


print([[word.upper(), word.lower(), len(word)] for word in words])


# In[40]:


print([word for word in words if len(word) >= 4])


# In[ ]:




