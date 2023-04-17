def solve(binary):
    decimal = 0
    for i in range(len(binary)):
        if binary[i] == "1":
            decimal = decimal + 2 ** (len(binary) - 1 - i)    #2^index
    if binary[0] == "1":            #check if negative binary
        decimal = decimal - 2**len(binary)
    return decimal

def start():
    binary = input("Enter a binary string: ")
    decimal = solve(binary)
    print("Decimal value:", decimal)