import sys
import random
import heapq

class CountMin:
    # this will initialize the variables as well as check for any wrong input and raise appropriate Error
    def __init__(self, n, k, w,p,flows):
        self.check_input(n, k, w)
        self.flows = flows
        self.n = n
        self.w = w
        self.counter_matrix = [[0] * w for _ in range(k)]
        self.k = k
        self.p = p 
        self.INTEGER_MAX = (2** 31 - 1)
        self.INTEGER_MIN = -(2**31)
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
            j = j  % self.w
            _min_ = min(self.counter_matrix[i][j],_min_)
        return int(_min_ // self.p) 

    # This function records the size of each flow in counters 
    def recording(self,key):
        hash_table_indices = self.get_hash_functions(key.flowid)
        for i, j in zip(range(self.k), hash_table_indices):
            j = j % self.w
            self.counter_matrix[i][j] += 1
            
    
    # generate random numbers
    def generate_random_numbers(self):
        return random.sample(range(1, self.INTEGER_MAX), self.k)

    # generate hashfunctions with the following function - > (number XOR i) where i is any random number in the self.random_nums
    def get_hash_functions(self, number):
        return [(int( ( hash(number)) ^ i)) for i in self.random_numbers]

    #Record the sizes of all flows in the counter,query to evaluate estimated sizes of all flows,
    #query for all flows, and calculate  the average error of all flows.
    # Also, Print the (flowid, estimated size, true size) of the largest estimated size
    def execute(self):
        for key in self.flows:
            # Sampling done Here
            for _ in range(int(key.number_of_packets)):
                random_num = random.randint(0, self.w * 100)
                if random_num < (self.p * self.w * 100):
                    self.recording(key)

        avg_error = 0 
        #heap = []
        for key in self.flows:
            val = key.number_of_packets
            query_out = self.query(key)
            #heap.append((query_out, key))
            avg_error += abs(query_out - int(val))

        print( "The average error among all flows:", avg_error// self.n , "Sampling Probability:", self.p)
        # largest = sorted(heap, key = lambda x: -x[0])[:100]
        # for val,key in largest:
        #     print(str(key.flowid) + "\t\t" + str(val) + "\t\t" + str(key.number_of_packets))


class Flow:
    def __init__(self,flow):
        x,y = flow.split()
        self.flowid = x
        self.number_of_packets = y
        
if __name__ == '__main__':
        n, k, w = 0,8,3000
        p = 0.8
        flows = []
        with open('project3input.txt') as input:
            n = int(input.readline())
            for i in range(n):
                flows.append(Flow(input.readline()))
        c = CountMin(n, k,w,p,flows)
        c.execute()  