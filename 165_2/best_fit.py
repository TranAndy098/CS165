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
        bf_node = tree.find_best(items[item])
        if bf_node == None:
            duplicate_node = tree.find_best(1-items[item])
            temp.val = 1-items[item]
            if (duplicate_node != None and duplicate_node.key == temp):
                duplicate_node.val.bin.append(bins)
                duplicate_node.val.bin.sort()
            else:
                tree.insert([bins], 1-items[item])
            free_space.append(1-items[item])
            assignment[item] = bins
            bins += 1
        else:
            bin_s = bf_node.val.bin
            rank = bf_node.rank
            bin_capacity = bf_node.key.val
            tree.remove(bf_node.key)
            if len(bin_s) > 1:
                tree.insert(bin_s[1:], bin_capacity, rank)
            bin_capacity -= items[item]
            assignment[item] = bin_s[0]
            free_space[bin_s[0]] -= items[item]
            temp.val = bin_capacity
            if (temp > zero):
                duplicate_node = tree.find_best(bin_capacity)
                if (duplicate_node != None and duplicate_node.key == temp):
                    duplicate_node.val.bin.append(bin_s[0])
                    duplicate_node.val.bin.sort()
                else:
                    tree.insert([bin_s[0]], bin_capacity)
