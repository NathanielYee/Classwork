'''
# Main First List Example
l = [1, 2, 3, True, ['a', 'b', 'c', ], 'Hello', (3, 4), 99]
print(l[1:4])

# Concatenation Method
var = l + [5, 6, 7]
print(l)

# Append Method
l.append([5, 6, 7])
print(l)

# Negative indexing
print(l[-1])  # last element in list
print(l[-2])  # 2nd to last element

# Create M Variable
m = l
print(m)

# Starting at 3 and onward
var = l[3:]
print(var)

# Name Function
def add_my_name(l):
    l.append("Nate")
# Main
def main():
    my_list = ['a', 'b', 'c']
    add_my_name(my_list)
    print(my_list)
main()


# Dictionaries

# value lookup by key
# Order does not matter
# Keys must be immutable (can't be changed) and unique
D = {}
D['a'] = 1
D['b'] = 2
D['z'] = 99
D['ze'] = 101
print(D[99])
'''
locations = {}
gps = [44, -78]
locations["Northeastern"] = gps
locations
# locations(gps) = 'Northeastern'

# 2d list
arr = [[1, 2, 3], [4, 5 ,6], [7, 8, 9]]
x = arr[1][2]
print(x)

#double assignment
T = (5, 6)
x = T[0]
y = T[1]
x, y = (5,6)
print(x, y, x+y)

# F(x) function
def f(x):
    return x**2, x**3, x**4
print(f(2))

# Sets
# Sets are colletions of keys dictionaries without values
# Values must be unique yes
S = {1, 2, 3, 3, 3}
D = {1:None, 2:None, 3:None}
type(S)
#print(S)
#print(3 in S)
type(D)
#print(D)
#print(3 in D)
T = {3, 4, 5}

# Set operations
# Overlap
print(S & T)
# Unions
print(S | T)
print(S.union(T))

# Set Difference
#elements in S not in T
print(S - T)
#elements in T not in S
print(T - S)

{x for x in Z if x % 2 == 0}