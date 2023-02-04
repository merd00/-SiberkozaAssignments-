# A List is a collection which is ordered and changeable. Allows duplicate members.
top_mo = ["Mert", "Berk", "Ediz", "Ulas","Tuna", "Yğit", "Eren", "Yiğithan", "Mehmet","Can", "Göktuğ"]

#1)Get a value
print("\n\n1)")
print(top_mo[0])
print(len(top_mo))
print("\n\n2)")

#push_back & pop_back
top_mo.append("Melih")
print(top_mo)
top_mo.pop()
print(top_mo)
print("\n\n3)")

#insert & remove
top_mo.remove("Tuna")
top_mo.insert(4,"Melih")
print(top_mo)
print("\n\n4)")

#Sort
top_mo.reverse()
print(top_mo)
top_mo.sort()
print(top_mo)
top_mo.sort(reverse=True)
print(top_mo)