numbers = [1, 4, 9, 16, 25]

#iterate the list
for i in numbers:
    print(i)

#print uneven numbers
for i in numbers:
    if i % 2:
        print(i)

#range generates a sequence
even = range(0, 10, 2)
for i in even:
    print(i)

#combine with index
even = [2,4,6,8]
for i in range(len(even)):
    print(i, even[i])

# print a range looks interesting, i.e range(0, 10, 2)
even = range(0, 10, 2)
print(even)

# the range is iteratable, thus functions that take iteratables can work on it
print(sum(even))


