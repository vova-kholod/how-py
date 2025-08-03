#indexes:  0  1  2  3
list_dt = [0, 1, 2, 3]
print(list_dt)

list_dt[0] = 4
print(list_dt)

list_dt.append(5)
print(list_dt)

list_dt.sort()
print(list_dt)

list_dt.sort(reverse = True)
print(list_dt)

list_dtt = ["aplle"]
print(list_dtt)

list_dk = [12, 42, 31, 14]
list_dk.reverse()
print(list_dk)

my_list = [1, 2, 3]
my_list.append(list(('apple', 'car', 'orange')))
print(my_list)

me_list = [1]
me_list.clear()
print(me_list)

mo_list = [1]
x = mo_list.copy()
print(x)

ma_list = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3]
q = ma_list.count(2)
print(q)

num = [1, 2, 3, 4]

nuum = [5, 6, 7, 8, 9]

num.extend(nuum)

print(num)

mu_list = [1, 2, 3, 4]
w = mu_list.index(4)
print(w)

mi_list = ["apple", "car", "orange"]
mi_list.insert(2, "banana")
print(mi_list)

mo_list = ["apple", "car", "banana", "orange"]
popped = mo_list.pop(1)

print(mo_list)

mq_list = ["apple", "car", "banana", "orange"]
mq_list.remove("car")
print(mq_list)

mw_list = ["a", "b", "c", "d", "e"]
mw_list.reverse()
print(mw_list)

mr_list = [2, 3, 1, 7, 5, 4, 0, 9, 6]
mr_list.sort()
print(mr_list)

mp_list = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
mp_list.sort()
print(mp_list)