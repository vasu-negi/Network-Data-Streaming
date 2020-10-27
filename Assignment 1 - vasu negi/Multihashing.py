import random
import sys
class MultiHashing:
    #this will initialize the variables as well as check for any wrong input and raise appropriate Error
    def __init__(self,table_size,flows,number_of_hashes):
        self.check_input(table_size,flows,number_of_hashes)
        self.table_size = table_size
        self.flows = flows
        self.number_of_hashes = number_of_hashes
        self.number_of_entries = 0
        self.hash_table = [None] * int(table_size)
        self.flowids = self.get_flow_ids()
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
        for i in hash_table_indices:
            slot_key= self.hash_table[i]
            if slot_key is None or slot_key == key:
                self.hash_table[i] = key
                return True
        return False
    #generate random numbers
    def generate_random_numbers(self):
        return random.sample(range(1, self.table_size*10), self.number_of_hashes)
    #generate hashfunctions with the following function - > (number XOR i) where i is any random number in the self.random_numbers 
    def get_hash_functions(self,number):
        return [(number ^ i)%self.table_size for i in self.random_numbers]
    #generate random flow ids 
    def get_flow_ids(self):
        return random.sample(range(1, self.table_size*10), self.flows)
    #This function will call insert function on every flow id generated 
    def execute(self):
        for _id_ in self.flowids:
            self.insert(_id_)
    #This function will count the number of Entries and also display the list of table entries in a [list].
    def show(self):
        count = 0 
        for x in self.hash_table:
            if x is not None:
                count+=1
        print("Number of entries ->", count)
        print("list of table entries ->", self.hash_table)


#This will take the arguments from the command line,validate the arguments, instantiate the object, and call the execute() and show()
if __name__ == '__main__':
    if len(sys.argv) !=4:
        print("Parameters are incorrect, Please enter the following parameters: table_size,flows,number_of_hashes")
    else:
        for x in sys.argv[1:]:
            if x.isnumeric():
                continue
            else:
                print("Please enter a valid input")
                break
        else:     
            table_size,flows,number_of_hashes= int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
            c = MultiHashing(table_size,flows,number_of_hashes)
            c.execute()
            c.show()