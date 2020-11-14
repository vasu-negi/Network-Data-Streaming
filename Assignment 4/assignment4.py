import sys
import random
import math
import matplotlib.pyplot as plt

class VirtualBitmap:
    # this will initialize the variables as well as check for any wrong input and raise appropriate Error
    def __init__(self, n, m, l,flows):
        self.check_input(n, m, l)
        self.flows = flows
        self.n = n
        self.m= m
        self.l = l
        self.B = [0] * m
        self.R =  self.generate_random_numbers(l)
        self.vb = -1
       
        

    # static method for checking the inputs before assigning them to any variable
    @staticmethod
    def check_input(*input_string):
        for input_str in input_string:
            if type(input_str) != int:
                raise ValueError("Please enter a valid input")
    
    
    def record(self,flow):
        
        random_numbers = self.generate_random_numbers(int(flow.number_of_packets))
        
        virtual_bitmap_index = [self.virtualBitmapIndex(i,flow) for i in random_numbers]
        physical_bitmap_index = [self.physicalBitMapIndex(i,flow) for i in virtual_bitmap_index]

        for index in physical_bitmap_index:
            self.B[index] = 1
    
    def query(self,flow):
        count_vf = 0
        for index in range(len(self.R)):
            if self.B[self.physicalBitMapIndex(index,flow)]==0:
                count_vf +=1
                
        vf = count_vf/len(self.R)

        if self.vb == -1:
            countvb= 0 
            for bit in self.B:
                if bit == 0:
                    countvb +=1
            self.vb = countvb/len(self.B)
        return (len(self.R) * (math.log(self.vb)- math.log(vf)))

    def run(self):
        for flow in self.flows:
            self.record(flow)
        file_ = open("output.txt", "w")
        for flow in self.flows:
            file_.write( str( flow.number_of_packets + "," + str(self.query(flow))+ "\n"))
        file_.close()
        


    # generate random numbers
    def generate_random_numbers(self,numbers):
        return random.sample(range(1, (2**32 - 1)), numbers)

    # generate hashfunctions with the following function - > (number XOR i) where i is any random number in the self.random_nums
    def get_hash_functions(self, number):
        return [(int(hash(number) ^ i)) for i in range(number)]

    def physicalBitMapIndex(self,index,flow):
        return abs((hash(flow.flowid) ^ self.R[index]) % len(self.B))
    
    def virtualBitmapIndex(self,element,flow):
        return abs(abs(hash(flow.flowid) ^ element) % len(self.R))

   #recording the sizes of all flows in the counters,query to evaluate estimated sizes of all flows,
   #query for all flows, and calculate  the average error of all flows.
   # Also, Print the (flowid, estimated size, true size) of the largest estimated sizes.


            

class Flow:
    def __init__(self,flow):
        x,y = flow.split()
        self.flowid = x
        self.number_of_packets = y
        
if __name__ == '__main__':
    n, m, l = 8507,500000,500
    flows = []
    with open('project4input.txt') as input:
        n = int(input.readline())
        for i in range(n):
            flows.append(Flow(input.readline()))
    c = VirtualBitmap(n, m,l,flows)

    c.run()  
