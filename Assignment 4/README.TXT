NETWORK DATA STREAMING
VASU NEGI
UFID: 8495-3933

PROJECT-4


In order to run these programs on *nix based/MAC system, follow the instructions below:
* Go to project directory in terminal
* Type the command in the following way:

    python3 file_name

##########Virtual Bitmap##############

Run: python3 VirtualBitmap.py

 
For Demo, following values are taken: n, m, l = 8507, 500000, 500

Functions:
   
1. def query(self, flow):
   Queries the bitmap for each flow and returns the calculated value.
2. def record(self, flow):
   Records each flow into the bitmap
3. def generate_random_numbers(self):
   generate random numbers
5. generate_physical_bitmap_indices(self, a, flow)
   generate index with the following function - > (flowid XOR self.R[a]) 
6. def execute(self):
   records each flow and then queries and writes the data into the file 
7. def generate_virtual_bitmap_indices(self, x, flow):
   Generates index with the following function -> (flowid XOR x)

Output:

1. Output.txt contains the output for the program, where each line defines flow's actual and estimated spread separated by ",". 

2. virtualbitmap.pdf contains the plot for the output where the x-axis is the true spread and y-axis is the estimated spread.



