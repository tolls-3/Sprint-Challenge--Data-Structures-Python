from binary_search_tree import BinarySearchTree
import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

Bst_names = BinarySearchTree(names_1[0])

for name in names_1[1:]:
    Bst_names.insert(name)

# Return the list of duplicates in this data structure
duplicates = [name for name in names_2 if Bst_names.contains(name)]
print(duplicates)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
set_names = set(names_1)
another_duplicates = set_names.intersection(names_2)


end_time2 = time.time()
print(f"{len(another_duplicates)} another_duplicates:\n\n{', '.join(another_duplicates)}\n\n")
print(f"runtime: {end_time2 - start_time} seconds")

