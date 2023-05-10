from merge_sort import merge_sort
from CFloat import CFloat
from zzt_ff import FFZipZipTree


def first_fit_decreasing(items: list[float], assignment: list[int], free_space: list[float]):
    merge_sort(items)
    first_fit(items, assignment, free_space)



def first_fit(items: list[float], assignment: list[int], free_space: list[float]):
    tree = FFZipZipTree(10000)
    bins = 0

    for item in range(len(items)):
        ff_node = tree.find_first(items[item])
        if ff_node == None:
            tree.insert(bins, 1-items[item])
            free_space.append(1-items[item])
            assignment[item] = bins
            bins += 1
        else:
            bin_num = ff_node.key
            bin_val = ff_node.val.capacity.val - items[item]
            bin_rank = ff_node.rank
            tree.remove(bin_num)
            tree.insert(bin_num, bin_val, bin_rank)
            assignment[item] = bin_num
            free_space[bin_num] -= items[item]
"""
items = [0.54, 0.67, 0.46, 0.57, 0.06, 0.23, 0.83, 0.64, 0.47, 0.03, 0.53, 0.74, 0.36, 0.24, 0.07, 0.25, 0.05, 0.63, 0.43, 0.04]
assignments = [0] * len(items)
free_space = list()

#expected_result = ProblemInstance(items = items, assignments = [0, 1, 0, 2, 1, 1, 3, 4, 5, 1, 5, 6, 2, 4, 2, 6, 3, 7, 8, 3], free_space = [0, 0.01, 0, 0.08, 0.12, 0, 0.01, 0.37, 0.57])
first_fit(items, assignments, free_space)
print(assignments, free_space)
print([0, 1, 0, 2, 1, 1, 3, 4, 5, 1, 5, 6, 2, 4, 2, 6, 3, 7, 8, 3], [0, 0.01, 0, 0.08, 0.12, 0, 0.01, 0.37, 0.57])"""