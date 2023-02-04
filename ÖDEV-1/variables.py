# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

x_mo = 3                         #int
y_mo = 3.1                       #float
name_mo = "Mert Öztürk"          #str
is_cool_mo = True               #bool
print(x_mo, y_mo, name_mo, is_cool_mo)

#Multiple assiggnment
x_mo, y_mo, name_mo, is_cool_mo = (6, 6.9, "Mert", True)
print(x_mo, y_mo, name_mo, is_cool_mo)

#Basic Math & Casting

a_mo = x_mo + y_mo

print(f"{type(x_mo)} = {type(a_mo)}")