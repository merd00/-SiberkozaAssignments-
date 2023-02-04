# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces
def sayhello(name_mo=" "):
    print(f"Hello {name_mo}")
sayhello("Mert")

#Return value
def getsum(a,b):
    return a+b;
print(getsum(3,4))

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getmult_mo = lambda m,o : m*o
print(getmult_mo(4,6))