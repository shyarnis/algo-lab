# References:
#   https://runestone.academy/ns/books/published//pythonds/Trees/BinaryHeapImplementation.html#binary-heap-implementation

class BinHeap:
    
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def heapify_up(self, i):
        while i//2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i//2], self.heap_list[i] = self.heap_list[i], self.heap_list[i//2]
            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.heapify_up(self.current_size)

    def heapify_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] =  self.heap_list[mc],  self.heap_list[i]
            i = mc
        
    def min_child(self, i):
        if i*2+1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i*2] < self.heap_list[i*2+1]:
                return i*2
            else:
                return i*2+1
    
    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]
        while (i > 0):
            self.heapify_down(i)
            i = i - 1
    
    # Add a function definition within the class which delete a min value from the Heap tree.
    def delete_min_value(self):
        min_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.heapify_down(1)
        return min_value

    # Implement to perform heap sort in the tree.
    def heap_sort(self):
        # sorted = []
        # for _ in range(self.current_size):
        #     sorted.append(self.delete_min_value())
        # return sorted
        return [self.delete_min_value() for _ in range(self.current_size)]

# Create an instance of BinHeap, and insert 5 elements and display the contents.
bh_1 = BinHeap()
bh_1.insert(12)
bh_1.insert(34)
bh_1.insert(21)
bh_1.insert(78)
bh_1.insert(56)
print(bh_1.heap_list)

# Initialize a list with 10 values and build the heap tree for the list.
bh_2 = BinHeap()
list_values = [43, 11, 38, 78, 57, 90, 67, 33, 99, 21]
bh_2.build_heap(list_values)
print(bh_2.heap_list)

# Delete min value from heap tree.
min_value = bh_2.delete_min_value()
print(f"Minimum value from heap tree: {min_value}")

# Implement heap sort.
sorted_list = bh_2.heap_sort()
print(f"Sorted List: {sorted_list}")
