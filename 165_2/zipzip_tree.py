# explanations for member functions are provided in requirements.py
# each file that uses a Zip Tree should import it from this file

from __future__ import annotations

from typing import TypeVar
from dataclasses import dataclass
from math import log2
from random import randint

#KeyType = TypeVar('KeyType')
#ValType = TypeVar('ValType')

@dataclass(eq=True, order=True)
class Rank:
    geometric_rank: int
    uniform_rank: int


class Node:
    def __init__(self, key, val, rank: Rank):
        self.key = key
        self.val = val
        self.rank = rank
        self.left = None
        self.right = None

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    


class ZipZipTree:
    def __init__(self, capacity: int):
        self.root = None
        self.capacity = capacity

    def print(self):
        if self.root != None:
            self.root.display()

    def get_random_rank(self) -> Rank:
        flips = 0
        cur_flip = randint(1,2)
        while cur_flip != 2:
            flips += 1
            cur_flip = randint(1,2)
        return Rank(flips, randint(1, int(log2(self.capacity))**3))
    
    def update_node(self, node):
        pass

    def insert(self, key, val, rank: Rank = None):
        
        if rank == None:
            rank = self.get_random_rank()

        x = Node(key, val, rank)
        update_queue = []

        cur = self.root
        prev = self.root

        while cur != None and (rank < cur.rank or (rank == cur.rank and key > cur.key)):
            update_queue.append(cur)
            prev = cur
            cur = cur.left if key < cur.key else cur.right

        if cur == self.root:
            self.root = x
        elif key < prev.key:
            prev.left = x
        else:
            prev.right = x

        update_queue.append(x)

        if cur != None:
            if key < cur.key:
                x.right = cur
            else:
                x.left = cur
            
            prev = x

            while cur != None:
                fix = prev
                
                if cur.key < key:
                    while cur != None and cur.key <= key:
                        update_queue.append(prev)
                        prev = cur
                        cur = cur.right
                else:
                    while cur != None and cur.key >= key:
                        update_queue.append(prev)
                        prev = cur
                        cur = cur.left
                
                if fix.key > key or (fix == x and prev.key > key):
                    fix.left = cur
                else:
                    fix.right = cur

        q = len(update_queue) - 1
        while q > -1:
            self.update_node(update_queue[q])
            #print("i",update_queue[q].key, update_queue[q].val.best_remaining_capacity)
            q -= 1


    def remove(self, key):
        update_queue = []

        cur = self.root
        
        while cur != None and key != cur.key:
            update_queue.append(cur)
            prev = cur
            cur = cur.left if key < cur.key else cur.right
        
        if cur == None:
            q = len(update_queue) - 1
            while q > -1:
                self.update_node(update_queue[q])
                q -= 1
            return
        
        
        left = cur.left
        right = cur.right
        

        if left == None:
            cur = right
        elif right == None:
            cur = left
        elif left.rank >= right.rank:
            cur = left
        else:
            cur = right
        
        if self.root.key == key:
            self.root = cur
        elif key < prev.key:
            prev.left = cur
        else:
            prev.right = cur

        while left != None and right != None:
            if left.rank >= right.rank:
                while left != None and left.rank >= right.rank:
                    update_queue.append(left)
                    prev = left
                    left = left.right
                prev.right = right
            else:
                while right != None and left.rank < right.rank:
                    update_queue.append(right)
                    prev = right
                    right = right.left
                prev.left = left
        q = len(update_queue) - 1
        while q > -1:
            self.update_node(update_queue[q])
            #print("r", update_queue[q].key, update_queue[q].val.best_remaining_capacity)
            q -= 1

    def find(self, key): #return value
        cur = self.root
        while cur != None and key != cur.key:
            if key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
        
        return None if cur == None else cur.val
    
    def size_recur(self, node) -> int:
        if node == None: 
            return 0
        return self.size_recur(node.left) + self.size_recur(node.right) + 1

    def get_size(self) -> int:
        return self.size_recur(self.root)

    def height_recur(self, node) -> int:
        if node == None: 
            return 0
        return max(self.height_recur(node.left), self.height_recur(node.right)) + 1

    def get_height(self) -> int:
        return self.height_recur(self.root) - 1
        

    def get_depth(self, key):
        cur = self.root
        depth = 0
        while cur != None and key != cur.key:
            if key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
            depth += 1
        
        return -1 if cur == None else depth
    
    def __str__(self, node = None):
        if node == None:
            return "NONE"
        else:
            return "[" + str(self.__str__(node.left)) + "[" + str(node.key) + "]" + str(self.__str__(node.right)) +"]"


    # feel free to define new methods in addition to the above
    # fill in the definitions of each required member function (above),
    # and for any additional member functions you define
