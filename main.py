import DecimalToSignedBinary
import pencilAndPaper
import booths

def main():
    inp1 = input("Choose a method between pencil and paper (1) or Booth's method (2): ")
    if(inp1 == "1"):
        print("Pencil and Paper\n")
        inp = input("Choose input type (D/B): ")
        if(inp == 'D'):
            decimal1 = DecimalToSignedBinary.inputs()
            decimal2 = DecimalToSignedBinary.inputs()
            pencilAndPaper.solve(decimal1, decimal2)
        elif(inp == 'B'):
            pencilAndPaper.get()

    
    elif(inp1 == "2"):
        print("Booth's\n")
        inp = input("Choose input type (D/B): ")
        if(inp == 'D'):
            decimal1 = DecimalToSignedBinary.inputs()
            decimal2 = DecimalToSignedBinary.inputs()
            booths.solve(decimal1, decimal2)
        elif(inp == 'B'):
            booths.get()
    
    loop()

def loop():
    x = input("\nWould you like to try again (Y/N): ")
    if x == 'Y':
        main()
    elif x == 'N':
        print("Program ended.") 
    elif x != 'Y':
        loop()

main()