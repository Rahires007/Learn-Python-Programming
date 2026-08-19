'''
Keyword :- The reserve word which meaning is predefined in programming 
there are mainly 35 keywords in python version above than 3.13
but in python version 3.7 contain 33 keyword
'''
import keyword
List=keyword.kwlist
count=0
print("Keyword List in python....")
print("------------------------------------")
for Key in List:
    print(Key)
    count+=1
print("-------------------------------------")
print("No Of Keyword :-",count)