def compare_crewmates(cm1, cm2):
    return cm1.load < cm2.load

def compare_treasures(t1, t2):
    if (t1[0].arrival_time + t1[1]) != (t2[0].arrival_time + t2[1]):
        return (t1[0].arrival_time + t1[1]) < (t2[0].arrival_time + t2[1])
    return t1[0].id < t2[0].id

class Heap:
    
    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        
        self.comparison_function = comparison_function
        self.heap = init_array[:]
        self.build_heap()
        
    def build_heap(self):
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify_down(i)
        
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)
    
    def extract(self):
        if len(self.heap) == 0:
            return None
        top_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if len(self.heap) > 0:
            self.heapify_down(0)
        return top_value
    
    def top(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]
    
    def heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.comparison_function(self.heap[index], self.heap[parent_index]):
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.heapify_up(parent_index)

    def heapify_down(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index

        if left_child < len(self.heap) and self.comparison_function(self.heap[left_child], self.heap[smallest]):
            smallest = left_child
        if right_child < len(self.heap) and self.comparison_function(self.heap[right_child], self.heap[smallest]):
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)