# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

numbers_mo = [00,13,24,31,44,52,69,78,82,96]

for number_mo in numbers_mo:
    if number_mo == 9:
        break
    if number_mo == 5:
        continue
    print(f"Current Number:{number_mo}")

for i in range(5,len(numbers_mo)):
    print(numbers_mo[i])

# While loops execute a set of statements as long as a condition is true.
ct_mo=0
while ct_mo < 10:
    print(f"count:{ct_mo}")
    ct_mo+=1