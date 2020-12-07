import sys
import random
import math


class VirtualBitmap:
    # this will initialize the variables as well as check for any wrong input and raise appropriate Error
    def __init__(self, n, m, l, flows):
        self.check_input(n, m, l)
        self.flows = flows
        self.n = n
        self.m = m
        self.l = l
        self.B = [0] * m
        self.R = self.generate_random_numbers(l)
        self.value_for_v_b = -10

    # static method for checking the inputs before assigning them to any variable
    @staticmethod
    def check_input(*input_string):
        for input_str in input_string:
            if type(input_str) != int:
                raise ValueError("Please enter a valid input")
    #records each flow 
    def record(self, flow):
        random_numbers = self.generate_random_numbers(int(flow.number_of_packets))
        virtual_bitmap_index = [self.generate_virtual_bitmap_indices(i, flow) for i in random_numbers]
        physical_bitmap_index = [self.generate_physical_bitmap_indices(i, flow) for i in virtual_bitmap_index]
        for index in physical_bitmap_index:
            self.B[index] = 1
    #queries for each flow
    def query(self, flow):
        count_v_f = 0
        for i in range(len(self.R)):
            if self.B[self.generate_physical_bitmap_indices(i, flow)] == 0:
                count_v_f += 1

        vf = count_v_f / len(self.R)

        if self.value_for_v_b == -10:
            count_v_b = 0
            for bit in self.B:
                if bit == 0:
                    count_v_b += 1
            self.value_for_v_b = count_v_b / len(self.B)
        return (len(self.R) * (math.log(self.value_for_v_b) - math.log(vf)))
    #records each flow and then queries and writes the data into the file
    def execute(self):
        for flow in self.flows:
            self.record(flow)

        file_ = open("output.txt", "w")
        for flow in self.flows:
            file_.write(str(flow.number_of_packets + "," + str(self.query(flow)) + "\n"))
        file_.close()

    # generate random numbers
    def generate_random_numbers(self, numbers):
        return random.sample(range(1, (2**32 - 1)), numbers)

    def generate_physical_bitmap_indices(self, a, flow):
        return abs((hash(flow.flowid) ^ self.R[a]) % len(self.B))

    def generate_virtual_bitmap_indices(self, x, flow):
        return abs(abs(hash(flow.flowid) ^ x) % len(self.R))


class Flow:
    def __init__(self, flow):
        x, y = flow.split()
        self.flowid = x
        self.number_of_packets = y


if __name__ == '__main__':
    n, m, l = 8507, 500000, 500
    flows = []
    with open('project4input.txt') as input:
        n = int(input.readline())
        for i in range(n):
            flows.append(Flow(input.readline()))
    c = VirtualBitmap(n, m, l, flows)
    c.execute()
