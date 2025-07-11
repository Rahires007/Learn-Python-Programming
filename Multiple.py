#Multiple inheritance
class Father:
    Father_Name="ABC"
    Sur_Name="XYZ"
class Mother:
    Mother_Name="PQR"
class Child(Mother,Father):
    def Test():
        print("\nMother Name :-",C.Mother_Name)
        print("\nFather Name :-",C.Father_Name)
        print("\nSur Name :-",C.Sur_Name)
C=Child
C.Test()
