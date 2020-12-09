import sys
import random
import heapq
import statistics
import numpy as np
import math

class CounterSketch:
    # this will initialize the variables as well as check for any wrong input and raise appropriate Error
    def __init__(self, n, k, w,flows,p):
        self.check_input(n, k, w)
        self.flows = flows
        self.n = n
        self.w = w
        self.p = p
        self.INTEGER_MAX = (2** 31 - 1)
        self.counter_matrix = [[0] * w for _ in range(k)]
        self.k = k
        self.random_numbers = self.generate_random_numbers()

    # static method for checking the inputs before assigning them to any variable
    @staticmethod
    def check_input(*input_string):
        for input_str in input_string:
            if type(input_str) != int:
                raise ValueError("Please enter a valid input")

     # Returns the mediam size of the flow in the counters 
    def query(self,key):
        hash_table_indices = self.get_hash_functions(key.flowid)
        list_of_values = []
        for i,j in zip(range(self.k), hash_table_indices):
            if abs(j // 2**30) == 1:
                j = j % self.w 
                list_of_values.append(self.counter_matrix[i][j])
            else:
                j = j % self.w 
                list_of_values.append(-self.counter_matrix[i][j])
        return int(statistics.median(list_of_values) // self.p )

    # This function will record the size of the flow (flowid) in the counter, depending on the MSB of the hash_value 
    # If the MSB is 1,then we add 
    # Else,we subtract
    def recording(self,key):
        hash_table_indices = self.get_hash_functions(key.flowid)
        for i, j in zip(range(self.k), hash_table_indices):
            if abs(j // 2**30) == 1:
                j = j % self.w
                self.counter_matrix[i][j] += 1
            else:
                j = j % self.w
                self.counter_matrix[i][j] -= 1
    
    # generate random numbers
    def generate_random_numbers(self):
        return random.sample(range(1, (2**32 - 1)), self.k)

    # generate hashfunctions with the following function - > (number XOR i) where i is any random number in the self.random_nums
    def get_hash_functions(self, number):
        return [np.int32((int(hash(number) ^ i))) for i in self.random_numbers]

   #recording the sizes of all flows in the counters,query to evaluate estimated sizes of all flows,
   #query for all flows, and calculate  the average error of all flows.
   # Also, Print the (flowid, estimated size, true size) of the largest estimated sizes.

    def execute(self):
        for key in self.flows:
            for _ in range(int(key.number_of_packets)):
                random_num = random.randint(0, self.INTEGER_MAX)
                if random_num < (self.p * self.INTEGER_MAX):
                    self.recording(key)

        avg_error = 0 
        heap = []
        #total average error 
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
        n, k, w,p = 10000,3,3000,0.1
        flows = []
        with open('project3input.txt') as input:
            n = int(input.readline())
            for i in range(n):
                flows.append(Flow(input.readline()))
        c = CounterSketch(n, k,w,flows,p)
        c.execute()  