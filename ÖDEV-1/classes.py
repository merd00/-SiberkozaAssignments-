# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object
class student_mo:
    def __init__(self,name="Unknown",surname="Unknown",number="Unknown"):
        self.name_mo=name
        self.surname_mo=surname
        self.number_mo=number
    
    def show_mo(self):
        print(f"Name:{self.name_mo}\tSurname:{self.surname_mo}\tNumber:{self.number_mo}\t")
    
    def change_number(self,number):
        self.number_mo=number


student1_mo = student_mo("Mert","Öztürk",200201032)
student2_mo = student_mo("Cenk")
student1_mo.show_mo()
student2_mo.show_mo()
student1_mo.change_number(4895)
student1_mo.show_mo()