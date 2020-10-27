import random
import sys
from collections import Counter


class Dlefthashing:
    # this will initialize the variables as well as check for any wrong input and raise appropriate Error
    def __init__(self, size_of_table, flows, number_of_segments):
        self.check_input(size_of_table, flows, number_of_segments)
        self.size_of_table = size_of_table
        self.flows = flows
        self.number_of_segments = number_of_segments
        self.number_of_entries = 0
        self.segment_size_of_table = self.size_of_table // number_of_segments
        self.hash_table = [None] * int(size_of_table)
        self.flowids = self.get_flow_ids()
        self.random_numbers = self.generate_random_numbers()
    # static method for checking the inputs before assigning them to any variable

    @staticmethod
    def check_input(*input_string):
        for input_str in input_string:
            if type(input_str) != int:
                raise ValueError("Please enter a valid input")
    # insert function will insert the flow id to the Hash Table

    def insert(self, key):
        hash_table_indices = self.get_hash_functions(key)
        for i in hash_table_indices:
            slot_key = self.hash_table[i]
            if slot_key is None or slot_key == key:
                self.hash_table[i] = key
                return True
        return False
    # generate random numbers

    def generate_random_numbers(self):
        return random.sample(range(1, self.size_of_table * 10), self.number_of_segments)
    # generate hashfunctions with the following function - > (number XOR i) where i is any random number in the self.random_nums

    def get_hash_functions(self, number):
        return [(((number ^ self.random_numbers[i]) % (self.segment_size_of_table)) + i * self.segment_size_of_table) for i in range(len(self.random_numbers))]
    # generate random flow ids

    def get_flow_ids(self):
        return random.sample(range(1, self.size_of_table * 10), self.flows)

    #This function will call insert function on every flow id generated 
    def execute(self):
        for _id_ in self.flowids:
            self.insert(_id_)
    # This function will count the number of Entries and also display the list of table entries in a [list].

    def show(self):
        count = 0
        for x in self.hash_table:
            if x is not None:
                count += 1
        print("Number of entries ->", count)
        print("list of table entries ->", self.hash_table)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Parameters are incorrect, Please enter the following parameters: size_of_table,flows,number_of_segments")
    else:
        for x in sys.argv[1:]:
            if x.isnumeric():
                continue
            else:
                print("Please enter a valid input")
                break
        else:

            size_of_table, flows, number_of_segments = int(
                sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
            c = Dlefthashing(size_of_table, flows, number_of_segments)
            c.execute()
            c.show()
