import os

# Python has functions for creating, reading, updating, and deleting files.
test_mo = open("test.txt", "w") 

# Get some info
print("Name: ", test_mo.name)
print("Is closed: ", test_mo.closed)
print("Opening Mode: ", test_mo.mode)

# Write to file
test_mo.write("test")
test_mo.write(" one two tree")
test_mo.close()
print("Is closed: ", test_mo.closed)

# Append to file
test_mo=open("test.txt","a") 
test_mo.write("\nI lOVE you baby!..")
test_mo.close()

# Read from file
test_mo = open("test.txt","r+")
text_mo = test_mo.read(200)
print(text_mo)
test_mo.close()

###os.remove("test.txt")    ->  # Remove file