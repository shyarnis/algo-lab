class BinHeap:
    
    def __init__(self):
        # self.heap_list = [0]      # first element of heap_list will be zero
        # self.heap_list = []
        self.heap_list = [0]
        self.current_size = 0

    def heapify_up(self, i):
        while i//2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i//2], self.heap_list[i] = self.heap_list[i], self.heap_list[i//2]
            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        # self.current_size = self.current_size + 1     # remove +1, gives IndexError: list index out of range
        # self.current_size = self.current_size
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
        self.heap_list = [0] + a_list[:]      # first element of heap_list will be zero
        # self.heap_list = a_list             # IndexError: list index out of range
        while (i > 0):
            self.heapify_down(i)
            i = i - 1

#################################################################################
# Create an instance of BinHeap, and insert 5 elements and display the contents.#
#################################################################################
bin_hp_5 = BinHeap()
bin_hp_5.insert(20)
bin_hp_5.insert(84)
bin_hp_5.insert(45)
bin_hp_5.insert(96)
bin_hp_5.insert(18)
print(bin_hp_5.heap_list)

#########################################################################
# Initialize a list with 10 values and build the heap tree for the list.#
#########################################################################
bin_hp_10 = BinHeap()
# list_values = [45, 21, 34, 90, 69, 33, 56, 12, 88]
list_values = [9, 5, 3, 4, 8, 7, 2, 12, 10, 6]
bin_hp_10.build_heap(list_values)
print(bin_hp_10.heap_list)
