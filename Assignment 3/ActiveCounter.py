
import random
class ActiveCounter:
    # this will initialize the variables as well as check for any wrong input and raise appropriate Error
    def __init__(self):
        self.number =  0 
        self.exp = 0 
    
    #This function will increment the counter
    #The counter is only incremented based on the probability calculated based on the exp part
    #If the number n overflows (length of bit array of n > 16), then right shift n and increment e

    def increment(self):
        for _ in range(1000000):
            if self.probability():
                self.number +=1
                if len("{0:b}".format(self.number)) > 16:
                    self.number = self.number >> 1
                    self.exp+=1

    #This function implements the probability of incrementing the counter, as (1 / 2^c.e)
    def probability(self):
        value = 2 ** self.exp
        return random.randint(0,value-1) == 0
        
if __name__ == '__main__':
    c = ActiveCounter()
    c.increment()
    print("Value of active counter:", c.number* (2**c.exp) )
        
