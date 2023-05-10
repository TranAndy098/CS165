from merge_sort import merge_sort
from CFloat import CFloat

def best_fit_decreasing(items: list[float], assignment: list[int], free_space: list[float]):
	merge_sort(items)
	best_fit(items, assignment, free_space)
        
def best_fit(items: list[float], assignment: list[int], free_space: list[float]):
    pass