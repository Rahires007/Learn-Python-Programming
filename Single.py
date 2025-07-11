#Single inheritance
class Parent:
    Parent_Name="ABC"
    Sur_Name="XYZ"
class Child(Parent):
    Child_Name="PQR"
    def Test():
        print("\nChild Name :-",C.Child_Name)
        print("\nParent Name :-",C.Parent_Name)
        print("\nSur Name :-",C.Sur_Name)
C=Child
C.Test()
