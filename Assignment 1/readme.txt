NETWORK DATA STREAMINGVASU NEGIUFID: 8495-3933	PROJECT-1In order to run these programs on *nix based/MAC system, follow the instructions below:* Go to project directory in terminal * Type the command in the following way: python file_name parameter1 parameter2 parameter3 parameter4(number of parameters depend on the algorithm that you will run)
Multi-hashing Table:Run: python Multihashing.py 1000 1000 3Where the parameters are: number of table entries, number of flows, number of hashes
	
	1. class MultiHashing 
		This is the class that implements the basic methods and variables.
		
		   a. def __init__(self,table_size,flows,number_of_hashes):
			This will initialize the variables as well as check for any wrong input and raise appropriate Error
		   b. def check_input(*input_string):
			This is a static function that validates the input parameters.
		   c. def insert(self,key):
			This insert function will insert the flow id to the Hash Table. 
		   d. def generate_random_numbers(self):
			This function generate random numbers of a given range.
	  	   e. def get_hash_functions(self,number):
			This function generates hash functions with the following function:
			
				(f XOR r), where XOR is a bitwise operator with 0 XOR 0 = 0, 1 XOR 0 = 1, 0 XOR 1 = 1, and 1 XOR 1 = 0.
			
			where r is a random number in the self.random_numbers and f is a flow id

		   f. def get_flow_ids(self):
			This function generate random flow ids 
		   g. def execute(self):
			This function will call insert function on every flow id generated.
		   h. def show(self):
			This function will count the number of Entries and also display the list of table entries in a [list].
		   
			Following is the output result for:number of table entries = 1000, number of flows = 1000, number of hashes = 3Number of Entries: 810

Cuckoo Hash Table:Run: python CuckooHashing.py 1000 1000 3 2 Where the parameters are: number of table entries, number of flows, number of hashes, number of Cuckoo steps	1. class CuckooHashing:
		This is the class that implements the basic methods and variables.
		
		   a. def __init__(self, size_of_table,flows,number_of_hashes,cukoo_steps):
			This will initialize the variables as well as check for any wrong input and raise appropriate Error.
		   b. def check_input(*input_string):
			This is a static function that validates the input parameters.
		   c. def insert(self,key):
			This insert function will insert the flow id to the Hash Table.  
		   d. def move(self, x,s):
			This function will check if the other keys can be moved into other slots.
		   e. def generate_random_numbers(self):
			This function generate random numbers of a given range.
	  	   f. def get_hash_functions(self,number):
			This function generates hash functions with the following function:
			
				(f XOR r), where XOR is a bitwise operator with 0 XOR 0 = 0, 1 XOR 0 = 1, 0 XOR 1 = 1, and 1 XOR 1 = 0.
			
			where r is a random number in the self.random_numbers and f is a flow id

		   g. def get_flow_ids(self):
			This function will generate random flow ids 
		   h. def execute(self):
			This function will call insert function on every flow id generated 
		   i. def show(self):
			This function will count the number of Entries and also display the list of table entries in a [list].
Following is the output result for:number of table entries = 1000, number of flows = 1000, number of hashes = 3, number of Cuckoo steps = 2Number of Entries: 939d-left Hash Table:Run: python Dlefthashing.py 1000 1000 4Where the parameters are: number of table entries, number of flows, number of segments


1. class Dlefthashing:
		This is the class that implements the basic methods and variables.
		
		   a. def __init__(self, size_of_table, flows, number_of_segments):
			This will initialize the variables as well as check for any wrong input and raise appropriate Error.
		   b. def check_input(*input_string):
			This is a static function that validates the input parameters.
		   c. def insert(self,key):
			This insert function will insert the flow id to the Hash Table  
		   d. def generate_random_numbers(self):
			This function generate random numbers of a given range.
	  	   e. def get_hash_functions(self,number):
			This function generates hash functions with the following function:
			
				(f XOR r), where XOR is a bitwise operator with 0 XOR 0 = 0, 1 XOR 0 = 1, 0 XOR 1 = 1, and 1 XOR 1 = 0.
			
			where r is a random number in the self.random_numbers and f is a flow id

		   f. def get_flow_ids(self):
			This function will generate random flow ids 
		   g. def execute(self):
			This function will call insert function on every flow id generated 
		   h. def show(self):
			This function will count the number of Entries and also display the list of table entries in a [list].
Following is the output result for:number of table entries = 1000, number of flows = 1000, number of segments = 4Number of Entries: 880