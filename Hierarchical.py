#Hierarchical inheritance
class GrandFather:
    GrandFather_Name="ABC"
    Sur_Name="XYZ"
class Father(GrandFather):
    Father_Name="PQR"
class Uncle(GrandFather):
    Uncle_Name="RST"
class GrandSon1(Uncle):
    def Test():
        print("\nUncle Name :-",GS1.Uncle_Name)
        print("\nGrandFather_Name:-",GS1.GrandFather_Name)
        print("\nSur Name :-",GS1.Sur_Name)
class GrandGirl1(Uncle):
    def Test():
        print("\nUncle Name :-",GG1.Uncle_Name)
        print("\nGrandFather_Name:-",GG1.GrandFather_Name)
        print("\nSur Name :-",GG1.Sur_Name)
class GrandSon2(Father):
    def Test():
        print("\nFather Name :-",GS2.Father_Name)
        print("\nGrandFather_Name:-",GS2.GrandFather_Name)
        print("\nSur Name :-",GS2.Sur_Name)
class GrandGirl2(Father):
    def Test():
        print("\nFather Name :-",GG2.Father_Name)
        print("\nGrandFather_Name:-",GG2.GrandFather_Name)
        print("\nSur Name :-",GG2.Sur_Name)
GS1=GrandSon1
GS1.Test()
GS2=GrandSon2
GS2.Test()
GG1=GrandGirl1
GG1.Test()
GG2=GrandGirl2
GG2.Test()
