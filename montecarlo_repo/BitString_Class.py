import numpy as np
import math      
import copy as cp      


class BitString:
    """
    Simple class to implement a config of bits
    """
    def __init__(self, N):
        self.N = N
        self.config = np.zeros(N, dtype=int) 

    def __repr__(self):
        out = ""
        for i in self.config:
            out += str(i)
        return out

    def __eq__(self, other):        
        return all(self.config == other.config)
    
    def __len__(self):
        return len(self.config)

    def on(self):
        """
        Return number of bits that are on
        """
        count = 0
        for i in range(len(self.config)):
            if(self.config[i] == 1):
                count+=1
        
        return count


    def off(self):
        """
        Return number of bits that are on
        """

        count = 0
        for i in range(len(self.config)):
            if(self.config[i] == 0):
                count+=1
        
        return count

    def flip_site(self,i):
        
        for j in range(len(self.config)):
            if(i == j):
                if(self.config[j] == 0):
                    self.config[j] = 1
                else:
                    self.config[j] = 0

        
        """
        Flip the bit at site i
        """
    
    def integer(self):
        """
        Return the decimal integer corresponding to BitString
        """
        num = 0
        for j in range(len(self.config)):
            if(self.config[j] == 1):
                num += 2**(len(self.config)-1-j)
        
        return num
 

    def set_config(self, s:list[int]):
        """
        Set the config from a list of integers
        """

        for i in range(len(self.config)):
            self.config[i] = s[i]

    def set_integer_config(self, dec:int):
        """
        convert a decimal integer to binary
    
        Parameters
        ----------
        dec    : int
            input integer
            
        Returns
        -------
        Bitconfig
        """

        temp = dec
        i = 0
        self.config = np.zeros(len(self))
        while(temp != 0):
            self.config[i] = temp % 2
            i+=1
            temp = temp // 2
        self.config = self.config[::-1]
        return self.config