squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[-3:]) # slicing returns a new list
print(squares + squares[-3:])
print(len(squares))


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits)
print(fruits.count('apple'))
print(fruits.count('banana'))
print(fruits.pop())
print(fruits.count('banana'))
fruits.reverse()
print(fruits)

#List Comprehensions
squares = list(map(lambda x: x**2, range(10)))
print(squares)
squares = [x**2 for x in range(20)]
print(squares)
