from merge_sort import merge_sort
from CFloat import CFloat
from zzt_bf import BFZipZipTree

def best_fit_decreasing(items: list[float], assignment: list[int], free_space: list[float]):
    merge_sort(items)
    best_fit(items, assignment, free_space)
        
def best_fit(items: list[float], assignment: list[int], free_space: list[float]):
    tree = BFZipZipTree(10000)
    bins = 0

    for item in range(len(items)):
        bf_node = tree.find_best(items[item])
        #if bf_node != None:
            #print(items[item], bf_node.key.val, bf_node.val.bin, bf_node.key.val- items[item])
        #else:
            #print(items[item], bins, 1- items[item])
        if bf_node == None:
            tree.insert(bins, 1-items[item])
            free_space.append(1-items[item])
            assignment[item] = bins
            #print("bin:", bins)
            bins += 1
        else:
            bin_bin = bf_node.val.bin
            bin_rank = bf_node.rank
            tree.remove(bf_node.key)
            bin_capacity = bf_node.key.val - items[item]
            tree.insert(bin_bin, bin_capacity, bin_rank)
            assignment[item] = bin_bin
            free_space[bin_bin] -= items[item]
            #print("bin:", bin_bin)
        #tree.order()



#items = [0.54, 0.67, 0.46, 0.57, 0.06, 0.23, 0.83, 0.64, 0.47, 0.03, 0.53, 0.74, 0.36, 0.24, 0.07, 0.25, 0.05, 0.63, 0.43, 0.04]
#assignments = [0] * len(items)
#free_space = list()

#expected_result = ProblemInstance(items = items, assignments = [0, 1, 2, 3, 4, 5, 6, 7, 7, 6, 5, 3, 1, 2, 4, 2, 4, 4, 0, 4], free_space = [0.13, 0.01, 0.02, 0, 0, 0, 0, 0])
#best_fit_decreasing(items, assignments,free_space)
#print(merge_sort(items))
#print([0, 1, 2, 3, 4, 5, 6, 7, 7, 6, 5, 3, 1, 2, 4, 2, 4, 4, 0, 4], [0.13, 0.01, 0.02, 0, 0, 0, 0, 0])
#print(assignments, free_space)