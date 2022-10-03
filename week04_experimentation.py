military = ['army', 'navy', 'airforce', 'marines']
print(military)
# Use indexing to access an element in the list.
# Indexing (from the beginning of the list) starts with 0.
print(military[2])
# Indexing from the end of the list starts with -1.
print(military[-3])
print(military[-1])
print(military[-2])
# We can modify the element at index -2.
# We can overwrite the element with a new value.
military[-2] = 'air force'
print(military)
military.append('national guard')
print(military)
# Let's start a new list that initially has nothing in it.
mountains = []
print(mountains)
mountains.append('Mount Kilimanjaro')
print(mountains)
mountains.append('Mount Kenya')
print(mountains)
# Print the length of the list.
print(len(military))
print(len(mountains))
mountains.append('Mount Meru')
print(mountains)
print(mountains[1])
# Remember to count from 0 rather than 1.
mountains.insert(2, 'mount stanley'.title())
print(mountains)
# Use del to delete:
del mountains[-1]
print(mountains)
# Remove an item by its value rather than its index:
mountains.remove('Mount Stanley')
print(mountains)
# Pop the last element out of the list and use it.
print(f"The second tallest mountain in Africa is {mountains.pop()}.")
print(mountains)
mountains.append('Mount Kenya')
mountains.append('Mount Stanley')
mountains.append('Mount Meru')
print(mountains)
print(f"The tallest mountain in Africa is {mountains.pop(0)}.")
print(mountains)
print(f"The second tallest mountain in Africa is {mountains.pop(0)}.")
print(mountains)
print(len(mountains))
heights = [5199, 5109, 5895, 4562]
print(heights)
# The sort() method changes the order of a list permanently.
heights.sort()
print(heights)
# The sorted() function returns a copy of the list,
# leaving the original list unchanged.
print(mountains)
print(sorted(mountains))
print(mountains)
print(military)
print(sorted(military))
print(military)
print(sorted(military, reverse = True))
print(military)

print('These are the branches:')
for branch in military:
    print('One branch is:')
    print(branch)
print('Those are all the branches.')

print('These are the branches:')
for i in range(len(military)):
    print('One branch is:')
    print(military[i])
print('Those are all the branches.')






