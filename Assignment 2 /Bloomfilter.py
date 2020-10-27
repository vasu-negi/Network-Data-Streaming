import sys
import random


class BloomFilter:
    # this will initialize the variables as well as check for any wrong input and raise appropriate Error
    def __init__(self, number_of_elements, number_of_bits, number_of_hashes):
        self.check_input(number_of_elements, number_of_bits, number_of_hashes)
        self.number_of_elements = number_of_elements
        self.number_of_bits = number_of_bits
        self.bitmap = [0] * number_of_bits
        self.elements = self.get_elements()
        self.number_of_hashes = number_of_hashes
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
            slot_key= self.bitmap[i]
            if slot_key == 0:
                return False #element not in the bitmap
        return True

    # This function will encode the key into the filter
    def encode(self,key):
        hash_table_indices = self.get_hash_functions(key)
        for i in hash_table_indices:
            self.bitmap[i] = 1
    
    # generate random numbers
    def generate_random_numbers(self):
        return random.sample(range(1, self.number_of_bits * 100), self.number_of_hashes)

    # generate hashfunctions with the following function - > (number XOR i) where i is any random number in the self.random_nums
    def get_hash_functions(self, number):
        return [(int(number) ^ i) % self.number_of_bits for i in self.random_numbers]
    # generate random elements
    def get_elements(self):
        return random.sample(range(1, self.number_of_bits * 100), self.number_of_elements)

    # This function will generate elements (denoted as set A) randomly, encode them in the filter, look up them in the filter 
    def execute1(self):
        elements_list = self.get_elements()
        for key in elements_list:
            self.encode(key)
        count = 0
        
        for key in elements_list:
            if self.lookup(key): #count incremented by 1 
                count +=1 
        return count

    # This function will generate another set of  elements randomly (denoted as set B) and look up them in the filter.  
    def execute2(self):
        count = 0
        elements_list2 = self.get_elements()
        for key in elements_list2:
            if self.lookup(key):
                count +=1 
                # self.list1.append(key)#key not in bitmap, encode the key and print it 
        return count
        
     
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Parameters are incorrect, Please enter the following parameters: number_of_elements,number_of_bits,number_of_hashes")
    else:
        for x in sys.argv[1:]:
            if x.isnumeric():
                continue
            else:
                print("Please enter a valid input")
                break
        else:
            number_of_elements, number_of_bits, number_of_hashes = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
            c = BloomFilter(number_of_elements, number_of_bits,number_of_hashes)
            
            print("number of elements in A found in the filter:" + str(c.execute1()) )
            print("number of elements in B found in the filter:" + str(c.execute2()) )