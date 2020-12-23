import sys
import random
class CuckooHashing:
    #this will initialize the variables as well as check for any wrong input and raise appropriate Error
    def __init__(self, size_of_table,flows,number_of_hashes,cukoo_steps):
        self.check_input(size_of_table,flows,number_of_hashes,cukoo_steps)
        self.flows = flows
        self.size_of_table = size_of_table
        self.cuckoo_steps = cukoo_steps
        self.hash_table = [None] * size_of_table
        self.flow_ids = self.get_flow_ids()
        self.number_of_hashes = number_of_hashes
        self.random_numbers = self.generate_random_numbers()
        
    #static method for checking the inputs before assigning them to any variable
    @staticmethod
    def check_input(*input_string):
        for input_str in input_string:
            if type(input_str) != int:
                raise ValueError("Please enter a valid input")
    #insert function will insert the flow id to the Hash Table  
    def insert(self,key):
        hash_table_indices = self.get_hash_functions(key)
        for i in range(self.number_of_hashes):
            if self.hash_table[hash_table_indices[i]] is None:
                self.hash_table[hash_table_indices[i]] = key
                return True
        for i in range(self.number_of_hashes):
            if self.move(hash_table_indices[i],self.cuckoo_steps) is True:
                self.hash_table[hash_table_indices[i]] = key
                return True
        return False
    #This function will check if the other keys can be moved into other slots
    def move(self, x,s):
        if s == 0:
            return False
        key_at_x = self.hash_table[x]
        hash_table_indices = self.get_hash_functions(key_at_x)
        for i in range(self.number_of_hashes):
            if hash_table_indices[i] != x and self.hash_table[hash_table_indices[i] ] is None:
                self.hash_table[hash_table_indices[i]] = key_at_x
                return True
        for i in range(self.number_of_hashes):
            if hash_table_indices[i] != x and self.move( hash_table_indices[i],s-1):
                self.hash_table[hash_table_indices[i]] = key_at_x
                return True
        return False

    #generate random numbers
    def generate_random_numbers(self):
        return random.sample(range(1, self.size_of_table*10), self.number_of_hashes)
        
    #generate hashfunctions with the following function - > (number XOR i) where i is any random number in the self.random_nums 
    def get_hash_functions(self, string):
        return [(int(string) ^ i)%self.size_of_table for i in self.random_numbers]
    #generate random flow ids 
    def get_flow_ids(self):
        return random.sample(range(1, self.size_of_table*10), self.flows)
       
    #This function will call insert function on every flow id generated 
    def execute(self):
        for _id_ in self.flow_ids:
            self.insert(_id_)

    #This function will count the number of Entries and also display the list of table entries in a [list].
    def show(self):
        count = 0 
        for x in self.hash_table:
            if x is not None:
                count+=1
        print("Number of entries ->", count)
        print("list of table entries ->", self.hash_table)

if __name__ == '__main__':
    if len(sys.argv) !=5:
        print("Parameters are incorrect, Please enter the following parameters: size_of_table,flows,number_of_hashes,cukoo_steps")
    else:
        for x in sys.argv[1:]:
            if x.isnumeric():
                continue
            else:
                print("Please enter a valid input")
                break
        else:     
            size_of_table,flows,number_of_hashes,cukoo_steps = int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
            c = CuckooHashing(size_of_table,flows,number_of_hashes,cukoo_steps)
            c.execute()
            c.show()
