# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name_mo = "Mert"
age_mo = 22

print("Hello, my name is "+ name_mo + " and I am "+ str(age_mo))

# String Formatting

print("Hello, my name is {name} and I am {age}".format(name=name_mo,age=age_mo))
print(f"Hello, my name is {name_mo} and I am {age_mo}")

# String Methods

str_mo = "adın ne senin GÜL mü DİKEN mi?"


print(str_mo.capitalize()+" -->1\n")

print(str_mo.upper()+" -->2\n")

print(str_mo.lower()+" -->3\n")

print(str_mo.swapcase()+" -->4\n")

print(f"{len(str_mo)}\t\t\t\t\t -->5\n")

print(str_mo.replace("adın","lale")+" -->6\n")

print(f"{str_mo.count('n')} \t\t\t\t\t -->7\n")

print(str(str_mo.startswith("ad"))+" \t\t\t\t\t -->8\n")

print(str(str_mo.endswith("mi?"))+" \t\t\t\t\t -->9\n")

print(str(str_mo.split())+" -->10\n") 

print(str(str_mo.find('e',1))+" \t\t\t\t\t -->11\n")

print(str(str_mo.isalpha())+" \t\t\t\t\t -->12\n")

print(str(str_mo.isalnum())+" \t\t\t\t\t -->13\n")

print(str(str_mo.isnumeric())+" \t\t\t\t\t -->14\n")