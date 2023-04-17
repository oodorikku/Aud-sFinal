def inputs():
    binary = [0] # initialize list
    decimal = 0
    nums = ''
    decimal = int(input("Decimal: "))
    if decimal < 0: # input is negative
        decToBin(abs(decimal), binary) # get positive of input
        twosComp(binary)
    else: # input is positive
        decToBin(decimal, binary)
    for i in binary:
        nums += str(i)
    return nums

def decToBin(num, binary):
    if num >= 1: # to not exceed maximum recursion depth
        decToBin(num//2, binary)
        binary.append(num%2)

def twosComp(binary):
    foundOne = 0 # boolean
    
    for x in reversed(range(len(binary))):
        if binary[x] == 1 and foundOne == 0:
            foundOne = 1
        elif binary[x] == 1 and foundOne == 1:
            binary[x] = 0
        elif binary[x] == 0 and foundOne == 1:
            binary[x] = 1

