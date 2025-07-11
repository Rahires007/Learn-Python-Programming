#Multilevel inheritance
class GrandFather:
    GrandFather_Name="ABC"
    Sur_Name="XYZ"
class Father(GrandFather):
    Father_Name="PQR"
class Child(Father):
    def Test():
        print("\nFather Name :-",C.Father_Name)
        print("\nGrandFather Name :-",C.GrandFather_Name)
        print("\nSur Name :-",C.Sur_Name)
C=Child
C.Test()
