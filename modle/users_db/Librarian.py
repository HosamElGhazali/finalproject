from _ast import Constant

from modle.users_db.F1 import F1


class Librarian(F1):


     def __init__(self,employment_type:Constant,id,full_name,age,id_no):
         self.__employment_type = employment_type
         super(Librarian, self).__init__(id=id,full_name=full_name,age = age,id_no=id_no)

     def get_employment_type(self):
         return self.__employment_type
     def set_employment_type(self,employment_type):
         self.__employment_type=employment_type
