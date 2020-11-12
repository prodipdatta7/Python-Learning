#Parameters, Unpacking, Variables

(a, b, c) = (1, 2, 3)
# a, b, c = (1, 2 ,3)
# a, b, c = (1, 2 ,3)
# a, b, c = 1, 2, 3
#All of the avobe does the same thing
#One more thing to remember is that the number of variables on the left side must be equal to the number of variables on the right side.
#Violation of this will give ValueError

print(a, b, c)
#unpacking strings
c1, c2, c3 = "abc" 
print(c1, c2, c3)

# unpacking list
l1, l2, l3 = [11, 32, 44] 
print(l1, l2, l3)

# unpacking generators, here gen = [0^2, 1^2, 2^2]
gen = (i ** 2 for i in range(3)) 
g1, g2, g3 = gen ; 
print(g1, g2, g3)

#Unpacking dictionaries (key, values, items)
dict = {'one': 1, 'two': 2, 'three': 3}

# unpacking keys
d1, d2, d3 = dict 
print(d1, d2, d3)

#unpacking values
dv1, dv2, dv3 = dict.values() 
print(dv1, dv2, dv3)

#unpacking items (key, value) pairs
i1, i2, i3 = dict.items()
print(i1, i2, i3)

#unpacking sets
#A small note to consider in unpacking the sets in python is that, the value of the varianle in the left side 
#can be not in the exact order unless the set is ordered
#Ordered set can solve the issue
s1, s2, s3 = {2, 10, -1}
print(s1, s2, s3)
