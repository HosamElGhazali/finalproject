from utils.Utils import Constants


class Order:
    def __init__(self,id,date,client_id,book_id,status:Constants,librarian_id):
        self.__id=id
        self.__date=date
        self.__client_id=client_id
        self.__book_id=book_id
        self.__status=status
        self.__librarian_id=librarian_id
    def get_id(self):
        return self.__id
    def set_id(self,id):
        self.__id=id

    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date

    def get_client_id(self):
        return self.__client_id

    def set_client_id(self, client_id):
        self.__client_id = client_id

    def get_book_id(self):
            return self.__book_id

    def set_book_id(self, book_id):
            self.__book_id = book_id

    def get_status(self):
         return self.__status

    def set_status(self, status):
         self.__status = status
    def get_librarian_id(self):
        return self.__librarian_id
    def set_librarian_id(self,librarian_id):
        self.__librarian_id=librarian_id

    def __repr__(self):
         return f'    {self.__id}   ,    {self.__client_id}      ,      {self.__librarian_id}      ,    {self.__book_id}   ,              {self.__status}                        ,  {self.__date}           '


