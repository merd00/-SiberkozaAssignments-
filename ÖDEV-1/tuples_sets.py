# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
numbers_mo = (1,2,3,4,5)

# Single value needs trailing comma
numbers = (1,)

# Get value
print("\n\n"+str(numbers_mo[1])+"\n\n")
del numbers,numbers_mo


# A Set is a collection which is unordered and unindexed. No duplicate members.
meyve_mo = {"portakal", "muz", "elma"}
print(meyve_mo)
print('elma' in meyve_mo)
print(len(meyve_mo))

#add
meyve_mo.add('karpuz')
print(meyve_mo)

#remove
meyve_mo.remove('karpuz')
print(meyve_mo)

#clear
meyve_mo.clear()
print(meyve_mo)