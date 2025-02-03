class DestructorExample:
    
    def __init__(self,name):
        self.name=name
        print(f"object {self.name} is created")
        
    def __init__(self,id):
        self.id=id
        print(f"object {self.id} is createddd")
        
    def __del__(self):
        print(f"object {self.id} is destroyed") 
        
obj=DestructorExample("sample")
del obj
obj1=DestructorExample("dhana")