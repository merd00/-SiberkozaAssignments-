# If/ Else conditions are used to decide to do something based on something being true or false
x_mo = 15
y_mo = 15
z_mo = 30

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
if x_mo>y_mo:
    print("x>y")
elif y_mo>x_mo:
    print("y>x")
else:
    print("x=y")

# Logical operators (and, or, not) - Used to combine conditional statements
if (x_mo == y_mo and z_mo>x_mo) or z_mo>y_mo:
    print(not(True))



# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

numbers_mo=[1,2,3,4,5,6,7]
if 5 in numbers_mo:
    print(True)
if 9 not in numbers_mo:
    print(True)


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
if x_mo is y_mo:
    print(True)