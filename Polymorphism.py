#Polymorphism
class Parent:
    def complete_graduation():
        print("\n In MBBS college")
class Child(Parent):
    def complete_graduation():
        print("\n In BCS college")
C=Child
C.complete_graduation()
