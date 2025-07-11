#Hybrid Inheritance
class GrandFather:
    GrandFather_Name="ABC"
    Sur_Name="XYZ"
class Father(GrandFather):
    Father_Name="RST"
class Sister_Of_Father(GrandFather):
    Sister_Of_Father_Name="PQR"
class Child(Father,Sister_Of_Father):
    def Test():
        print("\nSister of father Name :-",C.Sister_Of_Father_Name)
        print("\nFather Name :-",C.Father_Name)
        print("\nGrandFather Name :-",C.GrandFather_Name)
        print("\nSur Name :-",C.Sur_Name)
C=Child
C.Test()
