market_list_1 = {"tomato", "cucumber", "carot", "cabage"}
market_list_2 = {"salad", "tomato", "bread", "garlik"}

market_list_1.difference_update(market_list_2)

print(market_list_1)
print(market_list_2)

set_1 = {"apple", "orange", "banana"}

set_1.add("cucumber")

print(set_1)

set_2 = {"apple", "orange", "banana", "potato", "tomato", "cucumber"}
set_2.clear()
print(set_2)

set_3 = {"apple", "orange", "banana", "potato", "tomato", "cucumber"}
x = set_3.copy()
print(x)

set_4 = {"apple", "orange", "banana"}
set_5 = {"potato", "tomato", "cucumber", "apple"}

z = set_4.difference(set_5)
print(z)

set_6 = {"apple", "orange", "banana"}
set_7 = {"potato", "tomato", "cucumber", "apple"}
set_6.difference_update(set_7)
print(set_6)

set_8 = {"apple", "orange", "bnana"}
set_8.discard("bnana")
print(set_8)

set_9 = {"apple", "banana", "orange"}
set_10 = {"ptato", "tomato", "cucumber", "apple"}
c = set_9.intersection(set_10)
print(set_9)

set_11 = {"apple", "banana", "orange"}
set_12 = {"potato", "tomato", "cucumber", "apple"}
set_11.intersection_update(set_12)
print(set_11)

set_13 = {"apple", "banana", "orange"}
set_14 = {"potato", "tomato", "cucumber"}
set_13.isdisjoint(set_14)
print(set_13)

set_15 = {"a", "b", "c"}
set_16 = {"f", "e", "d", "c", "b"}
w = set_15.issubset(set_16)
print(w)

set_17 = {"apple", "banana", "orange"}
set_18 = {"potato", "tomato", "cucumber"}
e = set_17.symmetric_difference(set_18)
print(e)

set_19 = {"apple", "banana", "orange"}
set_20 = {"potato", "tomato", "cucumber", "apple"}
set_19.symmetric_difference_update(set_20)
print(set_19)

set_21 = {"apple", "banana", "orange"}
set_22 = {"tomato", "cucumber", "apple"}

t = set_21.union(set_22)

print(t)

set_23 = {"apple", "banana", "orange"}
set_24 = {"tomato", "cucumber", "apple"}
set_23.update(set_24)
print(set_23)

