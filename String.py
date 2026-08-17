'''
String :- The collection of character is called String 
String Index always start with zero 

Indexing in string :- StringName[index] , StringName[Start:End]
Slicing in string :- StringName[Start:End:Step]
Start --Start Index
End --End Index
Step --Jump - It is optional & default value of step is +1
It may be +ve or -ve
'''
# Simple String program
Name=input("\nEnter your name...")
print("\nHello\nWelcome...",Name)
print("----------------------------------------")

#String Indexing 
Name="Rahul"
print(Name[0:len(Name)])
'''for i in Name:
    print(i)''' #Indxing
print("----------------------------------------")

#String Slicing & Index Function
'''
1..Index -- Find The Index of character in string 
Parameter :- Character & SubString 
Return :- Index in Integer Value

2..Find -- Find The Index of character in string 
Parameter :- Character & SubString 
Return :- Index in Integer Value

3..Len -- Find The length of string 
Parameter :- String 
Return :- Length of given string in integer value

4..Upper -- Convert any string into uppercase
Parameter :- Not Required
Return :- String in Uppercase

5..Lower -- Convert any string into lowercase
Parameter :- Not Required
Return :- String in lowercase

6..Capitalize -- Convert any string into sentance case & initcap case
Parameter :- Not Required 
Return :- String in initcap case & Sentance case

7..Title -- Convert any string into sentance case & initcap case
Parameter :- Not Required 
Return :- String in initcap case & Sentance case

8..Count -- Count the frequency of any character & substring in given string 
Parameter :- Substring ,Character 
Return :- Frequency of character & Substring in integer value

9..Join -- It Join Given all character to string individually
Parameter :- Character
Return :- String With join given character individually

10..Isalnum --It check Given string is alphanumeric or not
Parameter :- Not Required
Return :- Boolean Value True or False

11..Isdigit --It check given string is digit or not
Parameter :- Not Required
Return :- Boolean Value True or False

12..Isalpha --It check given string is alphabetical or not
Parameter :- Not Required
Return :- Boolean Value True or False


'''
Email=input("Enter Your Email...")
print("Email :- ",Email)
UserName=Email[0:Email.index("@"):1]
print("UserName :-",UserName)
Domain=Email[Email.index("@")+1: :1]
print("Domain :-",Domain)
print("----------------------------------------")

#Upper , Lower ,Title , Len ,Count 
Name=input("Enter Your Name....")
print(len(Name))#Calculate the length of any string
print(Name.lower())#Convert any string into lowercase
print(Name.upper())#Convert any string into uppercase
print(Name.capitalize())#Same work as like Title
print(Name.title())#Convert any string into the Sentance case & Initcap case
print(Name.index("a"))#Find The index of any character 
print(Name.count("a"))#Count Frequency of any character 
print(Name.find("e"))#Find The Index of any character in given string
print(Name.isalnum())#Check Given String is Alphanumeric or not
print(Name.isdigit())#Check Given String is digit or not
print(Name.join("818"))#Join Each & Every character to given string
print(Name.isalpha())#Given String is Alphabetical or not
print(Name.isascii())#Check Given string have ascii or not 
print("----------------------------------------")
