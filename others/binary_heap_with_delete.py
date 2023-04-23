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
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
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

    ##########################################################################################
    # Add a function definition within the class which delete a min value from the Heap tree.#
    ##########################################################################################
    def delete_min_value(self):
        self.current_size -= 1
        self.heap_list.pop()

    
    # Extract min value and return a new Heap Tree
    def extract_min_value(self):
        min_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.heapify_down(1)
        return min_value
    
########################
# Binary Heap Instance.#
########################
bin_heap = BinHeap()
list_values = [45, 21, 34, 90, 69, 33, 56, 12, 88]
bin_heap.build_heap(list_values)

# Deletion.
print(bin_heap.heap_list)
bin_heap.delete_min_value()
print(bin_heap.heap_list)

# Extraction.
min_value = bin_heap.extract_min_value()
print(f"The minimum value of heap is {min_value}")
print(bin_heap.heap_list)