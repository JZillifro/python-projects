print("lmao")
l = [1,2,3,4,5]
print(l[-1])
l2 = l#this sets l2 as a reference equivalent to l, they reference the same object
print(l == l2)#are the objects equivalent in value?
print(l is l2)#are the two references to the same object?
l2 = list(l)#this clones 1, therefor l2 now references a new object equivalent to l
print(l == l2)
print(l is l2)

