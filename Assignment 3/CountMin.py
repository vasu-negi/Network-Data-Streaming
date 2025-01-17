import sys
import random
import heapq

class CountMin:
    # this will initialize the variables as well as check for any wrong input and raise appropriate Error
    def __init__(self, n, k, w,flows):
        self.check_input(n, k, w)
        self.flows = flows
        self.n = n
        self.w = w
        self.counter_matrix = [[0] * w for _ in range(k)]
        self.k = k
       
        self.random_numbers = self.generate_random_numbers()

    # static method for checking the inputs before assigning them to any variable
    @staticmethod
    def check_input(*input_string):
        for input_str in input_string:
            if type(input_str) != int:
                raise ValueError("Please enter a valid input")

    # Returns the minimum size of the flow in all the counters
    def query(self,key):
        
        hash_table_indices = self.get_hash_functions(key.flowid)
        _min_ = float('inf')
        for i,j in zip(range(self.k), hash_table_indices):
            _min_ = min(self.counter_matrix[i][j],_min_)
        return _min_ 

    # This function records the size of each flow in counters 
    def recording(self,key):
        hash_table_indices = self.get_hash_functions(key.flowid)
        for i, j in zip(range(self.k), hash_table_indices):
            self.counter_matrix[i][j] += int(key.number_of_packets)
            
    
    # generate random numbers
    def generate_random_numbers(self):
        return random.sample(range(1, self.w * 100), self.k)

    # generate hashfunctions with the following function - > (number XOR i) where i is any random number in the self.random_nums
    def get_hash_functions(self, number):
        return [(int((hash(number) & 0xffffffff ) ^ i)) % self.w for i in self.random_numbers]

    #Record the sizes of all flows in the counter,query to evaluate estimated sizes of all flows,
    #query for all flows, and calculate  the average error of all flows.
    # Also, Print the (flowid, estimated size, true size) of the largest estimated size
    def execute(self):
        for key in self.flows:
            self.recording(key)
        avg_error = 0 
        heap = []
        for key in self.flows:
            val = key.number_of_packets
            query_out = self.query(key)
            heap.append((query_out, key))
            avg_error += abs(query_out - int(val))

        print("The average error among all flows:",  avg_error// self.n)
        largest = sorted(heap, key = lambda x: -x[0])[:100]
        for val,key in largest:
            print(str(key.flowid) + "\t\t" + str(val) + "\t\t" + str(key.number_of_packets))


class Flow:
    def __init__(self,flow):
        x,y = flow.split()
        self.flowid = x
        self.number_of_packets = y
        
if __name__ == '__main__':
        n, k, w = 0,3,3000
        flows = []
        with open('project3input.txt') as input:
            n = int(input.readline())
            for i in range(n):
                flows.append(Flow(input.readline()))
        c = CountMin(n, k,w,flows)
        c.execute()  