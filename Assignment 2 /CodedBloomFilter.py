import sys
import random


class CodedBloomFilter:
    # this will initialize the variables as well as check for any wrong input and raise appropriate Error
    def __init__(self, number_of_sets, number_of_elements, number_of_filters, number_of_bits, number_of_hashes):
        self.check_input(number_of_sets, number_of_elements, number_of_filters, number_of_bits, number_of_hashes)

        self.number_of_sets = number_of_sets
        self.number_of_elements = number_of_elements
        self.number_of_filters = number_of_filters
        self.number_of_bits = number_of_bits
        self.number_of_hashes = number_of_hashes
        self.filters = [[0]*number_of_bits for i in range(self.number_of_filters)]
        
        self.random_numbers = self.generate_random_numbers()
        self.length_of_code = number_of_filters

        self.element_lists =  {i: self.get_elements() for i in  range(1,self.number_of_sets+1)}
        #self.codes_list = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
        self.codes_list = self.calculate_set_code()
        

    # static method for checking the inputs before assigning them to any variable
    @staticmethod
    def check_input(*input_string):
        for input_str in input_string:
            if type(input_str) != int:
                raise ValueError("Please enter a valid input")

    # Encode function will encode the elements in the filter
    def encode(self,set_index,element):
        filter_num = 0        
        
        for s_code in self.codes_list[set_index]:
            if s_code == 1:
                hash_indices = self.get_hash_functions(element) #get the indices where the value should be 1 in the selected filter
                for index in hash_indices:
                    self.filters[filter_num][index] = 1 
            filter_num+=1
            
    # Encode function will lookup the elements in the filter
    def lookup(self,element):
        set_lookup = [0]*len(self.filters)
        for filter_index in range(0,len(self.filters)):
            hash_indices = self.get_hash_functions(element) 
            for index in hash_indices:
                if self.filters[filter_index][index] == 0 :
                    break
            else:
                set_lookup[filter_index] = 1
        return set_lookup
    #This function will calculate the list of codes for each set
    def calculate_set_code(self):
        x = [ list(f'{_:0{(self.number_of_filters)}b}') for _ in range(self.number_of_sets+1) ]
        for i in range(len(x)):
            for j in range(len(x[0])):
                x[i][j] = int(x[i][j])
        return x
        
    # this function will generate sets of 1000 elements each, their codes are 001 through 111 respectively (for the demo), encode all sets in 3 filters according to the algorithm, perform lookup on all elements in the 7 sets for the demo question
    def execute(self):
        for set_index in range(1,self.number_of_sets+1):
            for element in self.element_lists[set_index]:
                self.encode(set_index,element)

        count = 0
        for set_index in range(1,self.number_of_sets+1):
            for element in self.element_lists[set_index]:
                s_code = self.lookup(element)
                if s_code == self.codes_list[0]:
                    pass
                elif s_code == self.codes_list[set_index]:
                    count+=1

        print("Number of elements whose lookup results are correct: " , count)

   
     # generate random numbers
    def generate_random_numbers(self):
        return random.sample(range(1, self.number_of_bits * 100), self.number_of_hashes)

    # generate hashfunctions with the following function - > (number XOR i) where i is any random number in the self.random_nums
    def get_hash_functions(self, number):
        return [(int(number) ^ i) % len(self.filters[0]) for i in self.random_numbers]
    # generate random elements  
    def get_elements(self):
        return random.sample(range(1, self.number_of_bits * 100), self.number_of_elements)      

if __name__ == '__main__':
    if len(sys.argv) != 6:
        print("Parameters are incorrect, Please enter the following parameters: number_of_sets, number_of_elements, number_of_filters, number_of_bits, number_of_hashes ")
    else:
        for x in sys.argv[1:]:
            if x.isnumeric():
                continue
            else:
                print("Please enter a valid input")
                break
        else:
            number_of_sets, number_of_elements, number_of_filters, number_of_bits, number_of_hashes = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]) ,int(sys.argv[5])
            c = CodedBloomFilter(number_of_sets, number_of_elements, number_of_filters, number_of_bits, number_of_hashes)
            c.execute()
