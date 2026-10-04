class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        prime = [True]*n  # creates a list of size n
        prime [0] = prime[1] = False   #  0 and 1 are not prime 

        i = 2    # we  start checking from   the first prime

        while i*i<n:    # we only need to check up   n root
            if prime[i]:
                for j in range(i*i, n,i):   # this marks multiples of i as non_prime
                    prime[j] = False 
            i += 1
        return sum(prime)
                
        
        