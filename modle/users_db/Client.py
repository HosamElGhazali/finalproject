from modle.users_db.F1 import F1


class Client(F1):
     def __init__(self,phone_number,id,full_name,age,id_no):
         self.__phone_number = phone_number
         super(Client, self).__init__(id=id, full_name=full_name, age=age, id_no=id_no)

     def get_phone_number(self):
         return self.__phone_number

     def set_phone_number(self, phone_number):
         self.__phone_number = phone_number

     def __repr__(self):
         return f' {super(Client,self).get_id()} , {super(Client,self).get_full_name()} , {super(Client,self).get_age()} , {super(Client,self).get_id_no()} , {self.__phone_number}'
