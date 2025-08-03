array = [3, 2, 1, 3]

#====================#
list_dt = list(array)
list_dt[0] = 4
list_dt.append(5)

tuple_dt = tuple(array)
# tuple_dt[0] = 4 <- not allowed, because tuple data type is unchangeble in python.
set_dt = set((1, 2, 3, 1, 2, 3, 4, 1, 1, 1, 1, 1))
dictionary_dt = {
    "en" : "english",
    "de" : "deutsch",
    "ru" : "русский",
    "ua" : "українська",
    }

print(list_dt)
print(tuple_dt)
print(set_dt)

print("=======================")
#print(list_dt)
#for l in list_dt:
#    print(l)

#print(tuple_dt)
#for t in tuple_dt:
#    print(t)

#print(set_dt)
#for s in set_dt:
#    print(s)

#print(dictionary_dt)
#for d in dictionary_dt:
#    print(d)
#    print(dictionary_dt[d])
    
#for k, v in dictionary_dt.items():
#    print(k, v)