#All Operation on file
#You must have to create Hello.txt 

#1Read Operation on file....
File=open("Hello.txt","r")
Content=File.read()
print(Content)

#2..Write Operation on file....
File=open("Hello1.txt","w")
File.write("\nHello")

#3...Append operation
File=open("Hello2.txt","a")
File.write("\nWelcome....")
