import sys
import random


class CountingBloomFilter:
    # this will initialize the variables as well as check for any wrong input and raise appropriate Error
    def __init__(self, number_of_elements, number_of_elements_to_remove,  number_of_elements_to_be_added, number_of_counters,number_of_hashes):
        self.check_input( number_of_elements, number_of_elements_to_remove,  number_of_elements_to_be_added, number_of_hashes)
        self.number_of_elements = number_of_elements
        self.number_of_elements_to_be_added = number_of_elements_to_be_added
        self.number_of_elements_to_remove = number_of_elements_to_remove
        self.number_of_hashes = number_of_hashes
        self.number_of_counters = number_of_counters
        self.filter = [0] * number_of_counters
        self.random_numbers = self.generate_random_numbers()

    # static method for checking the inputs before assigning them to any variable
    @staticmethod
    def check_input(*input_string):
        for input_str in input_string:
            if type(input_str) != int:
                raise ValueError("Please enter a valid input")
    # lookup function to check where the key is in the filter
    def lookup(self,key):
        hash_table_indices = self.get_hash_functions(key)
        for i in hash_table_indices:
            slot_key= self.filter[i]
            if slot_key < 1:
                return False #element not in the filter
        return True
   
    # This function will encode the key into the filter
    def encode(self,key):
        hash_table_indices = self.get_hash_functions(key)
        for i in hash_table_indices:
            self.filter[i] += 1
    #This function will remove the key from the filter
    def remove(self,key):
        hash_table_indices = self.get_hash_functions(key)
        for i in hash_table_indices:
            self.filter[i] -= 1

    # generate random numbers
    def generate_random_numbers(self):
        return random.sample(range(1, self.number_of_counters * 100), self.number_of_hashes)

    # generate hashfunctions with the following function - > (number XOR i) where i is any random number in the self.random_nums
    def get_hash_functions(self, number):
        return [(int(number) ^ i) % self.number_of_counters for i in self.random_numbers]
    # generate random elements
    def get_elements(self,number):
        return random.sample(range(1, self.number_of_counters * 100), number)

    #This function generate elements (denoted A) randomly, encode them in the filter, remove "number_of_elements_to_remove" elements in A from the filter, add other "number_of_elements_to_be_added "randomly generated elements in the filter, and look up all original elements from A in the filter.
    def execute(self):
        elements = self.get_elements(self.number_of_elements)
        #encode origial elements in set A
        for key in elements:
            self.encode(key)
        #remove "elements of set A from the filter"
        for key in elements[:self.number_of_elements_to_remove+1]:
            self.remove(key)

        #generate elements for number equal to "number_of_elements_to_be_added"
        elements2 = self.get_elements(self.number_of_elements_to_be_added)
        #adding new elements in the filter
        for key in elements2:
            self.encode(key)

        count = 0
        for key in elements:
            if self.lookup(key):
                count +=1
        return count 
      
if __name__ == '__main__':
    if len(sys.argv) != 6:
        print("Parameters are incorrect, Please enter the following parameters: number_of_elements, number_of_elements_to_remove,  number_of_elements_to_be_added, number_of_counters,number_of_hashes")
    else:
        for x in sys.argv[1:]:
            if x.isnumeric():
                continue
            else:
                print("Please enter a valid input")
                break
        else:
            number_of_elements, number_of_elements_to_remove,  number_of_elements_to_be_added, number_of_counters,number_of_hashes =  int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]) ,int(sys.argv[5])
            c = CountingBloomFilter( int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]) ,int(sys.argv[5]))
            print("Number of elements in the filter: " + str(c.execute()) )