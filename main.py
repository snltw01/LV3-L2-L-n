# class Animal:
#     # construtor:khởi tạo(Hàm khởi tạo phương thức trong tham số của __init__)#breakpoint
#     def  __init__(self,_name='IDK',_species='error'):
#         self.name=_name
#         self.species=_species

#     def Display_info(self):
#         return f'{self.name} is  a {self.species}'
# # hàm kế tạo
# class Person(Animal):
#     def __init__(self,_name,_species,_job):
#         super().__init__(_name,_species)
#         self.job=_job
    
#     def Display_info(self):
#         ParentClass=super().Display_info()

#         return f'{ParentClass} and is a {self.job}'

  

# dog=Animal('Ben','dog')
# print(dog.name)
# print(dog.species)
# print(dog.Display_info())


# person=Person('Jinnie','human','student')
# print(person.Display_info())