

# List declaration:

squares = [1, 4, 9, 16, 25] #result : [1, 4, 9, 16, 25]



# List have indexes :

squares[0] #result : 1



# List slicing (like the slicing in strings ) :

squares[-3:]  # slicing returns a new list, result : [9, 16, 25]


# Operations on lists :

squares + [36, 49, 64, 81, 100] #result : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



# Lists are mutable :

cubes = [1, 8, 27, 65, 125]
cubes[3] = 64 # result : [1, 8, 27, 64, 125]



# Adding new items to a list :

cubes.append(216) # result : [1, 8, 27, 64, 125, 216]

# Length of a list :

letters = ['a', 'b', 'c', 'd']
len(letters) # result : 4


