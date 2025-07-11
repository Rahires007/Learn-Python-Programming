#Function program
def Factorial(Num):
    Fact=1
    Xnum=1
    while(Xnum<=Num):
        Fact=Fact*Xnum;
        Xnum=Xnum+1
    print("\nGiven no =",Num)
    print("\nFactorial=",Fact)
Num=int(input("\nEnter a no..."))
Factorial(Num)
