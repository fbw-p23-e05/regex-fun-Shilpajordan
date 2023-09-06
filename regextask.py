
import re
# Task 1. Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

""" pattern = re.compile('^[a-zA-Z0-9]')
string ='2htjfght'
test = re.match(pattern,string)

if test:
    print('The string matches the pattern')
else:
    print("The string doesn't match the pattern")     """


# Task 2. Write a Python program that matches a string that has an a followed by zero or more b's.    

""" pattern = 'ab*'
string = 'cvabb23 abb '
test = re.search(pattern,string)
if test:
     print('The text is  a match')  
else:
     print('The text is not a match')     """


# Task 3. Write a Python program that matches a string that has an a followed by one or more b's.
""" pattern = '^ab+'
string = 'abc'
test = re.search(pattern,string)
if test:
    print('The text is  a match')  
else:
    print('The text is not a match') """


# Task 4 Write a Python program that matches a string that has an a followed by zero or one 'b'

""" pattern = 'ab?'
string = 'ab'
test = re.search(pattern,string)
if test:
    print('The text is  a match')  
else:
    print('The text is not a match')  """


# Task  5 Write a Python program that matches a string that has an a followed by three 'b'.

""" pattern = 'ab{3}' # or 'a?bbb'
string = 'aabbbb'
test = re.search(pattern,string)
if test:
    print('The text is  a match')  
else:
    print('The text is not a match')   """


# Task 6 Write a Python program that matches a string that has an a followed by two to three 'b'

""" pattern = 'ab{2,3}' 
string = 'cabb'
test = re.search(pattern,string)
if test:
    print('The text is  a match')  
else:
    print('The text is not a match')   
 """


# Task 7 Write a Python program to find sequences of lowercase letters joined by an underscore.
""" 
pattern = '[a-z]+_[a-z]+' 
string = 'adf_fgh_hil'
test = re.search(pattern,string)
if test:
    print('The string is  a match')  
else:
    print('The string is not a match')    """


# Task 8 Write a Python program to find the sequences of one upper case letter followed by lower case letters.
 
""" pattern = '[A-Z]+[a-z]+' 
string = 'Python'
test = re.search(pattern,string)
if test:
    print('The string is  a match')  
else:
    print('The string is not a match')     """


# Task 9 Write a Python program that matches a string that has an 'a' followed by anything ending in 'b'
""" pattern = 'a.*b$' 
string = 'acccnnnnn123db'
print(re.search(pattern,string)) """



# Task 10 Write a Python program that matches a word at the beginning of a string

""" pattern = '^\w+' 
string = 'The quick brown fox jumps ove rthe lazy dog'
string2 =' The quick brown fox jumps ove rthe lazy dog'
print(re.search(pattern,string)) 
print(re.search(pattern,string2)) 
 """
   

# Task 11 Write a Python program that matches a word at the end of a string, with optional punctuation

""" pattern = '\w+\S*$' 
string = 'The quick brown fox jumps ove the lazy dog '
string2 =' The quick brown fox jumps ove the lazy dog.'
print(re.search(pattern,string)) 
print(re.search(pattern,string2))  """


# Task 12 Write a Python program that matches a word containing 'z'

""" pattern = '\w+(z)\w' 
string = 'The quick brown fox jumps ove the lazy dog '
string2 =' python excercise'
print(re.search(pattern,string)) 
print(re.search(pattern,string2))  """



# Task 13 Write a Python program that matches a word containing 'z', not the start or end of the word.

""" pattern = '\Bz\B' 
string = 'The quick brown fox jumps ove the lazy dog '
string2 =' python exercise laz'
print(re.search(pattern,string)) 
print(re.search(pattern,string2))  """



# Task 14 Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores

""" pattern = '^[a-zA-Z0-9_]*$' # $ because to check if the sentence ends with any of the following condition
string = 'The quick brown fox jumps over the lazy dog '
string2 ='Python_Exercise_1'
print(re.search(pattern,string)) 
print(re.search(pattern,string2))  
 """

# Task 15 Write a Python program that starts each string with a specific number.

""" pattern = '^8' 
string = ' 2-200-235-000 '
string2 ='8-200-236-000'
print(re.search(pattern,string)) 
print(re.search(pattern,string2))   """


# Task 16 Write a Python program to remove leading zeros from an IP address.

""" ip = ' 216.200.230.196 '
string = re.sub('[0]','',ip)

print(string)
 """