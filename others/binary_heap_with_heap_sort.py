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

    ##############################################
    # Implement to perform heap sort in the tree.#
    ##############################################

    def heap_sort(self, a_list):
        pass


########################
# Binary Heap Instance.#
########################
