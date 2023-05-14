from merge_sort import merge_sort
from CFloat import CFloat
from zzt_bf import BFZipZipTree

def best_fit_decreasing(items: list[float], assignment: list[int], free_space: list[float]):
    merge_sort(items)
    best_fit(items, assignment, free_space)
        
def best_fit(items: list[float], assignment: list[int], free_space: list[float]):
    tree = BFZipZipTree(10000)
    bins = 0
    zero = CFloat(1-1)
    temp = CFloat(1-1)

    for item in range(len(items)):
        print()
        print("____________________________________________________________________________________")
        print(item)
        print("____________________________________________________________________________________")
        if tree.root != None:
            print("begining root", tree.root.key.val, tree.root.rank)
        else:
            print("no root")
        bf_node = tree.find_best(items[item])
        if bf_node != None:
            print(items[item], bf_node.key.val, bf_node.val.bin, bf_node.key.val- items[item])
        else:
            print(items[item], bins, 1- items[item])
            
        print()
        
        if bf_node == None:
            duplicate_node = tree.find_best(1-items[item])
            temp.val = 1-items[item]
            if (duplicate_node != None and duplicate_node.key == temp):
                print("adding bin to existing node with bin list")
                duplicate_node.val.bin.append(bins)
                duplicate_node.val.bin.sort()
            else:
                tree.insert([bins], 1-items[item])
            free_space.append(1-items[item])
            assignment[item] = bins
            print("just insert")
            tree.print()
            print("bin:", bins)
            bins += 1
        else:
            bin_bin = bf_node.val.bin
            rank = bf_node.rank
            bin_capacity = bf_node.key.val
            tree.remove(bf_node.key)
            if len(bin_bin) > 1:
                tree.insert(bin_bin[1:], bin_capacity, rank)
            
            bin_capacity -= items[item]
            assignment[item] = bin_bin[0]
            free_space[bin_bin[0]] -= items[item]
            print("just removed")
            tree.print()
            temp.val = bin_capacity
            if (temp > zero):
                duplicate_node = tree.find_best(bin_capacity)
                if (duplicate_node != None and duplicate_node.key == temp):
                    print("adding bin to existing node with bin list with insert here")
                    duplicate_node.val.bin.append(bin_bin[0])
                    duplicate_node.val.bin.sort()
                else:
                    print("adding becasue not full")
                    tree.insert([bin_bin[0]], bin_capacity)
            
                print("just insert")
                tree.print()
            print("bin:", bin_bin[0])
        print("ending root",tree.root.key.val, tree.root.rank)
        print()

def best_fit_old(items: list[float], assignment: list[int], free_space: list[float]):
    for item in range(len(items)):
        placed = False
        smallest = CFloat(1.0)
        place = -1
        for bin in range(len(free_space)):
            if CFloat(free_space[bin]) >= CFloat(items[item]):
                difference = CFloat(free_space[bin]-items[item])
                if smallest > difference:
                    place = bin
                    smallest = difference
                    placed = True



        if placed == False:
            assignment[item] = len(free_space)
            free_space.append(1-items[item])
        else:
            assignment[item] = place
            free_space[place] = smallest.val


"""
items = [0.54, 0.67, 0.46, 0.57, 0.06, 0.23, 0.83, 0.64, 0.47, 0.03, 0.53, 0.74, 0.36, 0.24, 0.07, 0.25, 0.05, 0.63, 0.43, 0.04]
sorted_i = [0.83, 0.74, 0.67, 0.64, 0.63, 0.57, 0.54, 0.53, 0.47, 0.46, 0.43, 0.36, 0.25, 0.24, 0.23, 0.07, 0.06, 0.05, 0.04, 0.03]
assignments = [0] * len(items)
free_space = list()

#expected_result = ProblemInstance(items = items, assignments = [0, 1, 2, 3, 4, 5, 6, 7, 7, 6, 5, 3, 1, 2, 4, 2, 4, 4, 0, 4], free_space = [0.13, 0.01, 0.02, 0, 0, 0, 0, 0])
best_fit_decreasing(items, assignments,free_space)
print(merge_sort(items))
print([0, 1, 2, 3, 4, 5, 6, 7, 7, 6, 5, 3, 1, 2, 4, 2, 4, 4, 0, 4], [0.13, 0.01, 0.02, 0, 0, 0, 0, 0])
print(assignments, free_space)
"""
def is_equal(v1: list[float], v2: list[float]) -> bool:
	for a, b in zip(v1, v2):
		if abs(a - b) > 1e-6:
			return False

	return True
import random
n = 15000



items = []

d = {}
for _ in range(n):
    items.append(round(random.uniform(0.01,0.99),2))


"""

items = [0.28, 0.26, 0.49, 0.75, 0.65, 0.65, 0.7, 0.49, 0.51, 0.46, 0.78, 0.88, 0.49, 0.57, 0.69, 0.28, 0.24, 0.79, 0.83, 0.66, 0.9, 0.73, 0.67, 0.93, 0.04, 0.74, 0.57, 0.52, 0.59, 0.48, 0.34, 0.1, 0.88, 0.54, 0.26, 0.86, 0.95, 0.57, 0.42, 0.21, 0.72, 0.97, 0.92, 0.94, 0.34, 0.21, 0.28, 0.16, 0.85, 0.81]
a = [0, 0, 1, 2, 3, 4, 5, 1, 6, 0, 7, 8, 6, 9, 10, 5, 2, 11, 12, 13, 14, 15, 16, 17, 17, 18, 19, 20, 21, 20, 13, 14, 22, 23, 18, 24, 25, 26, 9, 11, 27, 28, 29, 30, 3, 7, 27, 12, 31, 32]
f = [0, 0.02, 0.01, 0.01, 0.35, 0.02, 0.0, 0.01, 0.12, 0.01, 0.31, 0, 0.01, 0, 0, 0.27, 0.33, 0.03, 0.0, 0.43, 0.0, 0.41, 0.12, 0.46, 0.14, 0.05, 0.43, 0.0, 0.03, 0.08, 0.06, 0.15, 0.19]
"""
#print(items)

assignments = n * [0]
free_space = list()

best_fit(items, assignments, free_space)
#print(free_space)
#print(assignments)


assignments1 = n * [0]
free_space1 = list()




best_fit_old(items, assignments1, free_space1)
#print(assignments1)
#print(free_space1)

for i in range(n):
    if (assignments[i] != assignments1[i]):
        d[i] = (items[i], assignments1[i], assignments[i])

print(d)
print(assignments == assignments1)
print(is_equal(free_space, free_space1))


"""


for i in range(n):
    if (assignments[i] != a[i]):
        d[i] = (items[i], a[i], assignments[i])
print(a)
print(f)
print(d)

print(assignments == a)
print(is_equal(free_space, f))
"""
