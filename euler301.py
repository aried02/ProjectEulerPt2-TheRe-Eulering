"""
Paper with code,

nim sum for n, 2n, 3n is parity('a,'b, 'a + 'b + carry) where n = ...'a'b... (base 2) carry is from previous. a simple look shows that any time carry = 1, the nim sum is nonzero.

This means we just need one case of 11 in the string (only way to have a carry at some point)

how many ways to make 11 in a binary string?

build all strings without

numOptions
"""
def numOptions(start, lent):
    if lent==30:
        return 1
    if start == 1:
        return numOptions(0, lent+1)
    return numOptions(0, lent+1) + numOptions(1, lent+1)

print(numOptions(0, 0)) #num of strings wihtout 11, includes 0, covers for 2**30
# I'm sure if i were smart enough I could have calculated above but I'm
# a programmer at heart
# its probably embarrasingly close to a power of 2

# ... its fibonacci
# numOpt(0, len) = numOpt(0, len+1) + numOpt(1, len+1) = 
#                                          numOpt(0,len+1) + numOpt(0, len+2)
# which if u start from 30, go down, and have numOpt(0, 0) = 1, is literally
# numOpt(0, -1) = 1 (the way it is since numOpt(1, 0) = 1 really is numOpt(0,-1)
# just fibonacci from 32 (since fib(1) = 1, fib(2)=1)
# i swear to god im so dumb